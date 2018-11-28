/**
 *  Qualification Round of Google Code Jam 2009
 *  \author Ñî·«
 */
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int L,D,N;
ifstream filein("A.in");
ofstream fileout("out.in");
int test(string * language,string pattern);

int main()	{
	filein >> L >> D >> N;
	string *language=new string[D];
	string *pattern=new string[N];
	for(int i=0;i<D;i++)	{
		filein >> language[i];
	}
	for(int i=0;i<N;i++)	{
		filein >> pattern[i];
	}
	int num;
	for(int k=0;k<N;k++)	{
		num=test(language,pattern[k]);
		fileout <<"Case #"<<k+1<<": "<<num<<endl;

	}
	
}

int test(string * language,string pattern)	{
	int num=0;
	string *set=new string[L];
	int len=pattern.length();
	int q=0;
	for(int i=0;i<len;q++)	{
		if(pattern[i]=='('){
			for(int j=1;i+j<len;j++)	{
				if(pattern[i+j]==')')	{
					set[q]=pattern.substr(i+1,j-1);
					i+=j+1;
					break;
				}
			}
		}
		else {
			set[q]=pattern[i];
			i++;
		}
	}
	for(int i=0;i<D;i++)
	{
		for(int j=0;j<L;j++)	{
			if(string::npos==set[j].find(language[i][j])){
				break;
			}
			if(j==L-1)
				num++;
		}
	}
	return num;
}