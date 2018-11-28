#include <cstdio>
const int N=2010,M=17;
int t[N],line[N],n;
bool find=false;
bool check(int h,int k)
{
	int Max=line[k+1],p=k+1;
	for(int i=k+2;i<=n;i++)
		if(line[i]>Max && Max<=h)
			Max=line[i],p=i;
		else if(line[i]>Max && (Max-h)*(i-k) < (line[i]-h)*(p-k))
			Max=line[i],p=i;
	return t[k]==p;
}
void DFS(int k)
{
	if(k==0)
	{
		find=true;
		return;
	}
	for(int i=M;i>=1;i--)
	{
		if(check(i,k))
		{
			line[k]=i,DFS(k-1);
			if(find)return;
		}
	}
}
int main()
{
	int T,w=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(int i=1;i<n;i++)
			scanf("%d",&t[i]);
		line[n]=0;
		//for(int i=1;i<n;i++)
		//	if(t[i]==n)line[n]=16;
		//if(!line[n])line[n]=1;
		find=false;
		for(int i=M;i>=1;i--)
		{
			line[n]=i;
			DFS(n-1);
			if(find)break;
		}
		printf("Case #%d:",w++);
		if(find)
		{
			for(int i=1;i<=n;i++)
				printf(" %d",line[i]);
			puts("");
		}
		else puts(" Impossible");
	}
}
