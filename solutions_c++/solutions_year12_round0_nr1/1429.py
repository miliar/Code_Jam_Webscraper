#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ifstream fin1("output.txt");
ofstream fout("o.txt");
 
char m[26];

void readM()
{
	int i;
	for(i=0; i<26; ++i)
		fin1>>m[i]>>m[i];
}

int main()
{
	char c[257];
	int i,n,j;
	readM();
	fin>>n;
	fin.getline(c, 256);
	for(i=0; i<n; ++i)
	{
		fout<<"Case #"<<i+1<<": ";
		fin.getline(c, 256);
		for(j=0; j<256 && c[j]!='\0'; ++j)
			if(c[j]>='a' && c[j]<='z')
				fout<<m[c[j]-'a'];
			else
				fout<<c[j];
		fout<<endl;
	}
	return 0;
}