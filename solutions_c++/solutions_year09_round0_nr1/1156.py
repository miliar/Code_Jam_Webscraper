#include<cstdio>
#include<cstring>

using namespace std;

char a[5010][20];
char x[100];
bool v[501][16][26];
int k,l,n;

int ok(char c[],int pz)
{
for(int j=0;j<l;j++)
	if(!v[pz][j+1][c[j]-'a'])
		return 0;
return 1;
}

void rd()
{
scanf("%d%d%d",&l,&k,&n);

int i,j=0,p=0;
for(i=1;i<=k;i++)
	scanf("%s",a[i]);
	
for(i=1;i<=n;i++)
	{
	scanf("%s",x);
	
	int N=strlen(x);
	j=0,p=0;
	while(j<N)
		{
		p++;
		if(x[j]=='(')
			{
			j++;
			for(;x[j]!=')';j++)
				v[i][p][x[j]-'a']=1;
			j++;
			}
		else
			v[i][p][x[j]-'a']=1,j++;
		}
		
	int R=0;
	for(j=1;j<=k;j++)
		if(ok(a[j],i))
			R++;
	
	printf("Case #%d: %d\n",i,R);
	}
}

int main()
{
freopen("input","r",stdin);
freopen("output","w",stdout);

rd();


return 0;
}
