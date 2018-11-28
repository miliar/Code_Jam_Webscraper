#include<iostream>
#include<string>
#include<fstream>
using namespace std;
void main()
{
	string code=" ynficwlbkuomxsevzpdrjgthaq";
	string normal=" abcdefghijklmnopqrstuvwxyz";
	ifstream fin("A-small-attempt0.in");
	ofstream fout("out.txt");
	int cases;
	fin>>cases;
	string n;
	getline(fin,n);
	for(int c=1;c<=cases;c++)
	{
	string q;
	getline(fin,q);
	fout<<"Case #"<<c<<": ";
	for(int i=0;i<q.length();i++)
	{
		fout<<normal[code.find(q[i])];
		
	}
	fout<<"\n";
	}
	fout.close();
	fin.close();
	
}
