#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string zeropad(int k)
{
	stringstream ss;
	ss<<k;
	string str = ss.str();
	while(str.size() < 4)	str = "0" + str;
	return str;
}

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small.txt");
	
	int nPaths[500][19];
	
	string sent;
	int ssz, sdex;
	
	const char * str = "welcome to code jam";
	
	int N;
	fin>>N;
	getline(fin, sent);
	
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<500; j++)	for(int k=0; k<19; k++)	nPaths[j][k] = 0;
		//the second # is the index of the letter you're looking for
		
		getline(fin, sent);
		
		ssz = sent.size();
		if(sent.find('w') == string::npos)	sdex = ssz+1;
		else	sdex = sent.find('w');
		for(; sdex<ssz; sdex++)	for(int index=0; index<18; index++)
		{
			if(str[index] == sent[sdex])
			{
				if(0 == index)	nPaths[sdex][index] += 1;
				if(0 != nPaths[sdex][index])	for(int s2=sdex+1; s2<ssz; s2++)	if(sent[s2] == str[index+1])
					nPaths[s2][index+1] = (nPaths[s2][index+1] + nPaths[sdex][index]) % 10000;
			}
		}
		int total=0;
		for(sdex=0; sdex<ssz; sdex++)	total = (total + nPaths[sdex][18]) % 10000;
		fout<<"Case #"<<i+1<<": "<<zeropad(total)<<"\n";
	}
	
	return 0;
}
