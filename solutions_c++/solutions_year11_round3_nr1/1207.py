#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<cctype>
#include<list>
#include<set>
using namespace std;
bool blue (char tile[60][60],int i,int j)
{
	tile[i][j]='/';
	if(tile[i][j+1]=='#') tile[i][j+1]='\\';
	else return false;
	if(tile[i+1][j]=='#') tile[i+1][j]='\\';
	else return false;
	if(tile[i+1][j+1]=='#') tile[i+1][j+1]='/';
	else return false;
	return true;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,r,c,cas=0;
	cin>>t;
	while(t--)
	{
		char tile[60][60];
		cas++;
		cin>>r>>c;
		for(int i=0;i<r;i++)
			cin>>tile[i];
		bool ok=true;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(tile[i][j]=='#')
					ok=blue(tile,i,j);
				if(!ok) break;
			}
			if(!ok) break;
		}
		cout<<"Case #"<<cas<<":\n";
		if(!ok) cout<<"Impossible\n";
		else
		{
			for(int i=0;i<r;i++)
				cout<<tile[i]<<endl;
		}
	}
	return 0;
}

