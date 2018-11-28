#include <fstream>
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

unsigned long long ttW(string numar)
{
	int nr_letters = 0;
	unsigned long long decodificare[61];
	int cifra_c=0;
	unsigned long long timeToWar = 0;
	
	if(numar.size() == 1) return 1;
	
	for(unsigned int i=0;i<numar.size();i++)
	{
		if(numar[i] != '#')
		{
			nr_letters++;
			for(unsigned int j=i+1;j<numar.size();j++)
			{
				if(numar[j] == numar[i])
				{
					numar[j] = '#';
					decodificare[j] = cifra_c;
				}
			}
			numar[i] = '#';
			decodificare[i] = cifra_c;
			cifra_c++;
		}
	}
	for(unsigned int i=0;i<numar.size();i++)
	{
		if(decodificare[i] == 0)
		{
			decodificare[i] = -1;
		}
	}
	for(unsigned int i=0;i<numar.size();i++)
	{
		if(decodificare[i] == 1)
		{
			decodificare[i] = 0;
		}
	}
	for(unsigned int i=0;i<numar.size();i++)
	{
		if(decodificare[i] == -1)
		{
			decodificare[i] = 1;
		}
	}
	//baza e nr_letters
	if(nr_letters == 1) nr_letters++;
	
	int putere = numar.size()-1; 
	long double baza = nr_letters;
	for(unsigned int i=0;i<numar.size();i++)
	{
		unsigned long long temp = decodificare[i]*pow(baza, putere);
		
		timeToWar += temp;
		putere--;
	}
	//cout << "time to war" << timeToWar << endl;

	return timeToWar;
}
int main () {

	fstream fin, fout;
	int N;
	unsigned long long timeToWar = 0;
	string numar, decodificare;
	
	fin.open ("input.in", fstream::in );
	fout.open ("output.out", fstream::out);

	//rezolvare
	
	fin >> N; 
	getline (fin, numar);
	
	for(int i=0;i<N;i++)
	{
		getline (fin, numar);
		
		timeToWar = ttW(numar);
		//in distinct am baza care ma intereseaza
		//incep sa impart cifrele 
		
		
		fout << "Case #" << i+1 << ": " << timeToWar << endl;;
	}
	
	//end rezolvare
		
	fin.close();
	fout.close();
	cout << "Gata!!!";
	return 0;
}
