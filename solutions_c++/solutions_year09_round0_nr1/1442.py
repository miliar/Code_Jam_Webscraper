#include <fstream>
#include <iostream>
#include <string>
using namespace std;


void ini_dic(string corect[], string deinitializat[], int d)
{
	for(int i=0;i<d;i++)
	{
		deinitializat[i] = corect[i];
	}
}
int main () {

	fstream fin, fout;
	int l, d, n;
	string words[5000];
	string old_match[5000];//aici tin minte la fiecare iteratie daca e match pentru masca actuala;
	string new_match[5000];//aici tin minte la fiecare iteratie daca e match pentru masca actuala;
	string tc[500];
	
	int old_size, new_size;

	fin.open ("input.in", fstream::in );
	fout.open ("output.out", fstream::out);

	fin >> l >> d >> n; 
  
	for(int i=0;i<d;i++)
	{
		fin >> words[i];
		old_match[i] = words[i];
	}	
	for(int i=0;i<n;i++)
		fin >> tc[i];
		
	old_size = d;	
	
	//ini_dic(old_match, new_match, old_size);
	//new_size = old_size;
	
	//rezolvare
	int na = 0;
	
	for(int i=0;i<n;i++)
	{
		//rezolv tc[i]
		string decautat(tc[i]);
		string substring[15];

		int pos = 0;
		
		for(int j=0;j<l;j++)
		{
			if(decautat[pos] == '(')
			{
				pos++;
				while(decautat[pos] != ')')
				{
					substring[j] += decautat[pos];
					pos++;
				}
				pos++;
			}else{
				substring[j] = decautat[pos];
				pos++;
			}
				
		}
		/*
		for(int j=0;j<l;j++)
		{
			cout << substring[j] << " << ";
		}
		cout << endl;
		*/
		na = 0;//cate cuvinte am in dictionar pentru patternul curent
		for(int j=0;j<l;j++)
		{
			if (old_size == 0) break;
			new_size = 0;
			for(int k=0;k<old_size;k++)
			{			
				int pos = old_match[k].find_first_of(substring[j],j);
				if(pos == j)
				{
					 new_match[new_size] = old_match[k];
					 new_size++;
				}
			}
			
			ini_dic(new_match, old_match, old_size);
			old_size = new_size;
			
		}
		
		fout << "Case #" << i+1 << ": " << new_size << endl;
		ini_dic(words, old_match, d);
		old_size = d;
		
	}
	
	//end rezolvare
		
	fin.close();
	fout.close();
	cout << "Gata!!!";
	return 0;
}
