#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>


using namespace std;


int main()
{
    ifstream fin("c:\\input.txt");
    ofstream fout("c:\\output.txt");
	int cases;
	fin>>cases;
	int numn = 1;
	while(cases--)
	{
		string num;
		vector <int>myvec;
		vector <int> sorted;
		fin>>num;
		for(int i = 0; i <(int)num.length(); i++)
		{
			myvec.push_back(num[i]-'0');
			sorted.push_back(num[i]-'0');
		}
		
		sort(sorted.begin(), sorted.end());
		prev_permutation(sorted.begin(), sorted.end());
		if(myvec == sorted)
		{
			int min = 9;
			int mini = 0;
			for(int i = 0; i < (int)sorted.size(); i++)
			{
				if(sorted[i] < min && sorted[i] != 0)
				{
					min = sorted[i];
					mini = i;
				}
			}
			sorted.erase(sorted.begin()+mini);
			

			sort(sorted.begin(), sorted.end());
			sorted.insert(sorted.begin(),0);
			sorted.insert(sorted.begin(),min);
			fout<<"Case #"<<numn++<<": ";
		for(int i = 0; i < (int)sorted.size(); i++)
			fout<<sorted[i];
		fout<<endl;
		}
		else
		{
		next_permutation(myvec.begin(),myvec.end());
		fout<<"Case #"<<numn++<<": ";
		for(int i = 0; i < (int)myvec.size(); i++)
			fout<<myvec[i];
		fout<<endl;
		}







	}
    fin.close();
    fout.close();
    return 0;
}