/*
ID: aditya21
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;
char curel='a';
char processrec(vector<vector<int> > table, int b, int c,vector<vector<char> >  &mat, int x, int y);
void processmap(vector<vector<int> > table, int b, int c,vector<vector<char> >  &mat);

int main() 
{
	ifstream fin ("d:\\io\\B-large (1).in");
	ofstream fout ("d:\\io\\B-large.out");

	int a, b, c;
	int i, j, k;
	int p, q, r, x, y, z;
	
	vector<vector<char> > mat;
	vector<char> chrow;
	int cost,max;
	string str1,str2;
	char str[510],ch;
	map<char,int> table;
	vector<int> row;
	
	fin>>a;
	for(i=0;i<a;i++)
	{
		fout<<"Case #"<<(i+1)<<": ";
		cout<<"Case #"<<(i+1)<<": ";
		fin>>str1;
		//str2=str1;
		k = str1.size();
		//sort(str2.begin(),str2.end());
		string::iterator iter = str1.begin();

		str1.insert(iter,'0');
		//cout<<str1<<endl;
		//cout<<str2;
		//fout<<next_permutation(str1.begin(),str1.end());
		next_permutation(str1.begin(),str1.end());
		{
			if(str1[0]=='0')
			{
				str1.erase(0,1);
				fout<<str1<<endl;
			}
			else
				fout<<str1<<endl;
		}

	}
}

/*string calcnext(string &str1, map<char,int> table)
{
int i,j,k,p,q,r;
k = str1.size();
for(i=0; i<k; i++)
{
	if()
}

}*/