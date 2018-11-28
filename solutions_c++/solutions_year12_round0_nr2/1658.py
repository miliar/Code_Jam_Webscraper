#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cassert>
#include<ctime>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>


#define PB push_back
#define M 100
#define N 500010
#define MOD 1000000007
#define MAX 18450000
#define MAX 18450000
//#define NMAX 101
//#define SRT 11
#define SRT 4300
#define LL long long
#define LLMAX 0x7fffffffffffffffLL

int max_score(int n,bool surp)
{
	if(surp)
	{
		if(n<2)
		return -1;
		return (n+4)/3;
	}
	return (n+2)/3;
}

int maxg(int arr[],int end,int ind,int surp,int mscore)
{
	int mynormscore,mysurpscore,k,rb1,rb2;
	if(end-ind<surp)
	return -1;
	
	if(ind==end-1)
	{
		k= max_score(arr[ind],surp);
		if(k==-1)
		{
		//printf("end %d ind %d surp %d mscore %d return -1\n",end,ind,surp,mscore);
		return -1;
		}
		if(k>=mscore)
		{
		//printf("end %d ind %d surp %d mscore %d return 1\n",end,ind,surp,mscore);
		return 1;
		}
		//printf("end %d ind %d surp %d mscore %d return 0\n",end,ind,surp,mscore);
		return 0;
		
		
	}
	if(surp>=1)
{	
	mysurpscore=max_score(arr[ind],1);
	if(mysurpscore !=-1)
	{
		rb1=maxg(arr,end,ind+1,surp-1,mscore);
	} else rb1=0;
	
	
	if(mysurpscore >= mscore)
	{
		if(rb1!=-1)
		rb1++;
		
	}
	if(rb1==-1)
	rb1=0;
}	else rb1=0;
	
	mynormscore=max_score(arr[ind],0);
	rb2=maxg(arr,end,ind+1,surp,mscore);
	if(mynormscore>=mscore)
	{
		if(rb2!=-1)
		rb2++;
	}
	if(rb2==-1)
	rb2=0;
	//printf("end %d ind %d surp %d mscore %d return %d\n",end,ind,surp,mscore,rb1>rb2?rb1:rb2);
	return rb1>rb2?rb1:rb2;
}

int ans[1000][1000];
int main()
{
	int tc,ti,n,s,p,arr[1000],i,t1,t2,j,k;
	scanf("%d",&tc);
	for(ti=1;ti<=tc;++ti)
	{
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;++i)
		scanf("%d",&arr[i]);
		
		i=max_score(arr[0],0);
		if(i>=p)
		ans[0][0]=1;
		else
		ans[0][0]=0;
		
		for(i=1;i<n;++i)
		{
			j=max_score(arr[i],0);
			//printf("j is %d\n",j);
			if(j>=p)
			ans[0][i]=ans[0][i-1]+1;
			else
			ans[0][i]=ans[0][i-1];
			
			//printf("ans[0][%d] is %d\n",i,ans[0][i]);
		}
		
		i=max_score(arr[0],1);
		if(i>=p)
		ans[1][0]=1;
		else
		ans[1][0]=0;
		for(j=2;j<=p;++j)
		{
			ans[j][0]=-1;
		}
		
		for(i=1;i<=s;++i)
		{
			for(j=1;j<n;++j)
			{
				k=max_score(arr[j],1);
				if(k==-1)
				{
					t1=ans[i][j-1];
				} else {
					t1=ans[i-1][j-1];
				}
				if(k>=p)
				{
					if(t1!=-1)
					{
						t1++;
					}
				}
				k=max_score(arr[j],0);
				t2=ans[i][j-1];
				if(k>=p)
				{
					if(t2!=-1)
					{
						t2++;
					}
				}
				
				ans[i][j]=t1>t2?t1:t2;
				//printf("%6d",ans[i][j]);
			}
			//puts("\n");
			
		}
		/*for(i=0;i<=s;++i)
		{
			for(j=0;j<n;++j)
			{
				printf("%4d",ans[i][j]);
			}
			puts("");
		}*/
		printf("Case #%d: %d\n",ti,ans[s][n-1]);
	}
	return 0;
}