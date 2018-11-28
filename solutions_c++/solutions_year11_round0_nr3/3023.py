#include<iostream>
#include<stdio.h>
using namespace std;
int flag[20];
int a[20];
int n;
int ans=0;
void dfs(int i)
{
	if(i<n)
	{
		flag[i]=0;
		dfs(i+1);
		flag[i]=1;
		dfs(i+1);
	}
	else
	{
        int j,x=0,y=0,s=0,s2=0;
		for(j=0;j<n;j++)
		{
           if(flag[j]==0)
		   {
			   x=x^a[j];
			   s+=a[j];
		   }
		   else
		   {
			   y=y^a[j];
			   s2+=a[j];
		   }
		}
		if(x==y&&s>ans&&s!=0&&s2!=0)
		{
			ans=s;
		}
		//cout<<s<<endl;
	}
}
int main()
{
	freopen("s.txt","w",stdout);
	int t,i,k=0;
	cin>>t;
	while(t--)
	{
		ans=0;
      k++;
	  cin>>n;
	  for(i=0;i<n;i++)
		  scanf("%d",&a[i]);
	  memset(flag,0,sizeof(flag));
	  dfs(0);
	  printf("Case #%d: ",k);
	  if(ans==0)
          cout<<"NO"<<endl;
	  else
          cout<<ans<<endl;
	}
	return 0;
}