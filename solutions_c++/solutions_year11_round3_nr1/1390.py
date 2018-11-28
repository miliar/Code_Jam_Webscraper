#include<iostream>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<cstdlib>
#include<vector>

using namespace std;

//char ar[100][100];
//bool mark[100][100];
bool solve()
{
	vector<string> vstr;
	int i,j,r,c;
	string str;

	cin>>r>>c;
	
	for(i=1;i<=r;i++)
	{
		cin>>str;
		vstr.push_back(str);
	}	
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			if(vstr[i][j]=='#')
			{
				if((j+1<c && vstr[i][j+1]!='#')||(j+1>=c)) return true;
				
				if((i+1<r && vstr[i+1][j]!='#')||(i+1>=r)) return true;

				if((j+1<c && i+1<r && vstr[i+1][j+1]!='#')||(j+1>=c)||(i+1>=r)) return true;

				vstr[i][j]=vstr[i+1][j+1]='/';
				vstr[i+1][j]=vstr[i][j+1]='\\';
			}
		}
	}
	for(i=0;i<r;i++)cout<<vstr[i]<<endl;

	return false;
}

int main()
{	
	int i,t;

	for(cin>>t,i=1;i<=t;i++)
	{
		printf("Case #%d:\n",i);		
		if(solve())cout<<"Impossible\n";
	}
	return 0;
}
