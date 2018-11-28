#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<cmath>
#include<algorithm>

using namespace std;

vector<int> gr[1010]; 
int np[1100];

void dfs(int n)
{
	np[n]++;
	if (np[n]==1)
	{
		for (int i=0;i<gr[n].size();i++)
		{
			dfs(gr[n][i]);
		}
	}
}

void main(){
#ifdef MY_TEST_VAR
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif


   int T;
   scanf("%d",&T);
   for (int I=1;I<=T;I++)
   {
	   bool ok=0;
	   int n,m,x;
	   scanf("%d",&n);
	   for (int i=1;i<=n;i++)
	   {
		   scanf("%d",&m);
		   for (int j=0;j<m;j++)
		   {
			   scanf("%d",&x);
			   gr[i].push_back(x);
		   }
	   }
	   for (int i=1;i<=n&&!ok;i++)
	   {
			dfs(i);
			for (int j=1;j<=n;j++)
			{
				if (np[j]>1) ok=1;
				np[j]=0;
			}
	   }
	   printf("Case #%d: ",I);
	   if (ok)
		   printf("Yes\n");
	   else
		   printf("No\n");

	   for (int i=1;i<=n;i++)
		   gr[i].clear();
   }

}