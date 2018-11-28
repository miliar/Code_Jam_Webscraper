#include <iostream>
using namespace std;

bool b[16][27];
char c;
char a[5001][16];
char x[28*16];
int l,d,n,i,j,k,t;
bool ok,kh;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for (i=1; i<=d; i++)
	{
		scanf("%s",a[i]);
	}
	for (i=1; i<=n; i++)
	{
		memset(b,false,sizeof(b));
		k=0;
		scanf("%s",x);
		t=0;
		kh=false;
		for (j=0; ; j++)
		{
			if (!kh) t++;
			if (t>l) break;
			if (x[j]=='(') kh=true;
			if (x[j]!='(' && x[j]!=')') b[t][x[j]-96]=true;
			if (x[j]==')') kh=false;
		}
		for (j=1; j<=d; j++)
		{
			ok=true;
			for (t=1; t<=l; t++)
			{
				if (!b[t][a[j][t-1]-96]) {ok=false; break;}
			}
			if (ok) k++;
		}
		printf("Case #%d: %d\n",i,k);
	}


//	system("pause");
	return 0;
}
