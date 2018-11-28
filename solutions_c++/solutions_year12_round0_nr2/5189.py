#include <iostream>
#include <cstdio>

using namespace std;

int t,n,s,p,a[100],ans;
FILE *fp=fopen("output.txt", "w");
int main()
{
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n>>s>>p;
		ans=0;
		for(int j=0;j<n;j++)
		{
			cin>>a[j];
			
			if(a[j]/3>1&&a[j]/3+(a[j]%3?1:0)>=p||a[j]/3==0&&1-(a[j]==0?1:0)>=p)
				ans++;
			else if(s>0&&(a[j]!=0&&a[j]%3==0&&a[j]/3+1>=p||a[j]%3==1&&a[j]/3+1>=p||a[j]%3==2&&a[j]/3+2>=p)) 
			{
				s--;
				ans++;
			}
		}
		fprintf(fp,"Case #%d: %d\n", i,ans);
		
	}
	return 0;
}