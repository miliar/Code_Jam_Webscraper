#include<cstdio>
#include<string>
#include<algorithm>
#include<map>
using namespace std;
FILE *in=fopen("un2.in","r");
FILE *out=fopen("un2.out","w");
#define  CLS(a,b) memset(a,b,sizeof(a))
void readline(char str[])
{
	int i=0;
	char c;
	while(1)
	{
		if(fscanf(in,"%c",&c)==EOF || c=='\n')
		{
			str[i]=0;
			break;
		}
		str[i]=c;
		i++;
	}
}
map<string,int> ind;
int arr[1001];
int n,s,q;
int best[1001][101];
int solve(int p,int c)
{
	if(p==q)return 0;
	int &ret=best[p][c];
	if(ret!=-1)
		return ret;
	ret=1<<29;
	int i;
	if(p!=0 && c!=arr[p])
		ret=min(ret,solve(p+1,c));

	for(i=0;i<s;i++)
		if(arr[p]!=i)
		{
			ret=min(ret,solve(p+1,i)+1);
		}
	return ret;
}
int main()
{
	int i,j,k;
	char name[200];
	fscanf(in,"%d",&n);
	for(i=0;i<n;i++)
	{
		ind.clear();
		fscanf(in,"%d\n",&s);
		for(j=0;j<s;j++)
		{
			readline(name);
			ind[name]=j;
		}
		fscanf(in,"%d\n",&q);
		for(j=0;j<q;j++)
		{
			readline(name);
			arr[j]=ind[name];
		}
		CLS(best,-1);
		k=solve(0,0);
		if(k==0)k=1;
		fprintf(out,"Case #%d: %d\n",i+1,k-1);
	}
	return 0;
}