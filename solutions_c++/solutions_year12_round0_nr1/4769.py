#include<iostream>
#include<fstream>
#include<string>
using namespace std;
char table2[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
string s;
void Read()
{
	
    ifstream fin("A-small-attempt5.in"); 
	ofstream f("A-small-attempt5.out");
	int nn;
	fin>> nn;
	getline(fin,s);
	//cout<<nn;
	int i=0;
    for(int mm=0;mm<nn;mm++)
    {    
		getline(fin,s);
		int x=s.size() ; 
        f<<"Case #"<<mm+1<<": ";
		for(int j=0;j<x;j++)
		{
			if(32==s[j])
			{
				f<<" ";
				continue;
			}
			int xxx=(int )s[j]-97;
			if(xxx>=25)
				xxx%=26;
			f<<table2[(xxx)];
		}
		f<<endl;
    }
	
}
int main()
{
	Read();
	//system("pause");
	return 0;
}