#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cctype>
#include <cstring>
#include <cmath>

#include <vector>

#include <queue>
#include <stack>

#include <algorithm>

using namespace std;

struct team{
	double p;
	double w;
	double wp;
	double owp;
	double oowp;
	double ans;
} st[110];

int main()
{
	//freopen("A-small-attempt0.in","r",stdin); freopen("A-small-out.txt","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large-out.txt","w",stdout);
	
	int t,k;
	int mat[110][110];
	int n,i,j;
	char ch;
	
	cin>>t;
		
	for(k=1;k<=t;k++)
	{
		cin>>n;
		
		getchar();
		
		for(i=0;i<n;i++)
		{
			st[i].p=0;
			st[i].w=0;
			for(j=0;j<n;j++)
			{
				ch=getchar();
				if(ch=='.') mat[i][j]=-1;
				else 
				{
					if(ch=='1') 
					{
						mat[i][j]=1;
						st[i].w++;
					}
					else mat[i][j]=0;
					
					st[i].p++;
				}
			}
			
			st[i].wp=st[i].w/st[i].p;
			
			getchar();
		}
		
		for(i=0;i<n;i++)
		{
			st[i].owp=0;
			
			if(st[i].p==0) continue;
			
			for(j=0;j<n;j++)
			{
				if(mat[i][j]!=-1)
				{
					if(st[j].p==1) continue;
					
					if(mat[i][j]==1)
					{
						st[i].owp+=st[j].w/(st[j].p-1);
					}
					else st[i].owp+=(st[j].w-1)/(st[j].p-1);
				}
			}
			
			st[i].owp/=st[i].p;
		}
		
		for(i=0;i<n;i++)
		{
			
			st[i].oowp=0;
			
			if(st[i].p==0) continue;
			
			for(j=0;j<n;j++)
			{
				if(mat[i][j]!=-1)
				{
					st[i].oowp+=st[j].owp;
				}
			}
			
			st[i].oowp/=st[i].p;
		}
			
		//for(i=0;i<n;i++) { for(j=0;j<n;j++) cout<<mat[i][j]<<" "; cout<<endl; }
		
		cout<<"Case #"<<k<<":"<<endl;;
		
		for(i=0;i<n;i++)
		{
			st[i].ans=.25*st[i].wp+.5*st[i].owp+.25*st[i].oowp;
			printf("%.12lf\n",st[i].ans+1e-13);
		}
			
	}

	return 0;
}





