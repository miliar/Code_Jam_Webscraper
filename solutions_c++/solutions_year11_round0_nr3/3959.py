#include<stdio.h>
#include<cstring>
#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include <fstream>
using namespace std;
int posa,posb;
int a[16];
int sum;
int ans;
bool vis[16];
int n;
void dfs(int cur )
{
	if(cur>n)
	{
		int s=0,ss=0;
		for(int i=1;i<=n;i++)if(vis[i])
		{
			s+=a[i];
			ss=ss^a[i];
		}
		int sss=0;
		for(int i=1;i<=n;i++)if(!vis[i])sss=sss^a[i];
		if(s!=sum&&ss==sss&&s>ans)ans=s; 
		return ;
	}
	vis[cur]=1;
	dfs(cur+1);
	vis[cur]=0;
	dfs(cur+1);
}
int main() 
{
	ofstream outfile("C:\\test.txt"); 
	int t;
	cin>>t;
	int ca=0;
	while(t--)
	{
		 ca++;
		 ans=0;
		 cin>>n;
		 sum=0;
		 for(int i=1;i<=n;i++)cin>>a[i],sum+=a[i];
		 memset(vis,0,sizeof(vis));
		 dfs(1);
		 if(ans==0)
		 {
			outfile<<"Case #"<<ca<<": NO"<<endl;
 		 }
 		 else outfile<<"Case #"<<ca<<": "<<ans<<endl;
	}
	 outfile.close();
} 