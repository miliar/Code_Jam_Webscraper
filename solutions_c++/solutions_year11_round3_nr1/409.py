#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<numeric>
#include<cmath>

#include<fstream>

using namespace std;

vector<string> A(vector<string> s)
{
	int i,j;
	int row,col;
	vector<string> empty;

	row=s.size(),col=s[0].size();

	for(i=0;i<row;++i)
	{
		for(j=0;j<col;++j)
		{
			if(s[i][j]=='#')
			{
				if(i+1>=row || j+1>=col || s[i][j+1]!='#' || s[i+1][j]!='#' || s[i+1][j+1]!='#')
					return empty;
				else
					s[i][j]='/',s[i][j+1]='\\',s[i+1][j]='\\',s[i+1][j+1]='/';
			}
		}
	}


	return s;
}

void main()
{
	int i,j,num,row,col;
	string s;
	vector<string> v,ret;
	ifstream fin("C:\\Users\\dark\\Desktop\\gcj2011\\A-large\\A-large.in");
	ofstream fout("C:\\Users\\dark\\Desktop\\gcj2011\\A-large\\A-small.txt");
	
	fin>>num;

	for(i=1;i<=num;++i)
	{
		v.clear();

		fin>>row>>col;

		for(j=0;j<row;++j)
		{
			fin>>s;
			v.push_back(s);
		}

		ret=A(v);

		fout<<"Case #"<<i<<": "<<endl;

		if(ret.size()==0)
			fout<<"Impossible"<<endl;
		else
		{
			for(j=0;j<ret.size();++j)
				fout<<ret[j]<<endl;
		}

//		fout<<A(n,k)<<endl;
	}

/*	int i;
	string s[]={".##..",".####",".####",".##.."};
	vector<string> vs(s,s+4);

	vector<string> ret=A(vs);

	for(i=0;i<ret.size();++i)
		cout<<ret[i]<<endl;*/
}
