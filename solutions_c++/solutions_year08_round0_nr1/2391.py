/*
Language:C++
*/

#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<vector>

using namespace std;

int main()
{
	ofstream fout("A-large.out");
	ifstream fin("A-large.in");

	string as;
	getline(fin,as,'\n');
	int a=atoi(as.c_str());


	for(int i=0;i!=a;i++)
	{

		string bs;
		getline(fin,bs);
		int b=atoi(bs.c_str());

		map <string,int> name;
		for(int j=0;j!=b;j++)
		{
			string n;
			getline(fin,n,'\n');
			name.insert(pair<string,int>(n,0));
		}

		string cs;
		getline(fin,cs,'\n');
		int c=atoi(cs.c_str());

		int d=0,time=0;
		vector<string> search(c);
		for(int k=0;k!=c;k++)
		{
			string s;
			getline(fin,s,'\n');
			search[k]=s;
		}

		for(int m=0;m!=c;m++)
		{
			string l=search[m];
			if(name[l]==0){
				name[l]++;
				d++;
			}

			if(d==b){
				d=0;
				map<string,int>::iterator iter;
				for(iter=name.begin();iter!=name.end();iter++)
				{
					iter->second=0;
				}
				m--;
				time++;
			}
		}
		fout<<"Case #"<<i+1<<": "<<time<<endl;
	}

	return 0;
}