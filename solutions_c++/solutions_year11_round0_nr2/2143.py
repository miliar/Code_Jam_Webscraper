#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

char cb[26][26];
char s[110];
int op[26][26];
int c,d,n;

void getdata(void);

int main()
{
	freopen("in.txt","w",stdout);
	freopen("test.txt","r",stdin);
	int ca,i,j,t,x,z,mmin;
	bool o;
	scanf("%d",&ca);
	for (z=1;z<=ca;z++)
	{
		getdata();
		printf("Case #%d: ",z);
		for (i=2,t=1;i<=n;i++)
		{
			if (t==0)
				s[++t]=s[i];
			else if (cb[s[i]-'A'][s[t]-'A']!=0)
				s[t]=cb[s[i]-'A'][s[t]-'A'];
			else
			{
				mmin=99999;
				for (j=t;j>0;j--)
				{
					if (op[s[j]-'A'][s[i]-'A']==0)
					{
						mmin=j;
						break;
					}
				}
				if (mmin!=99999)
				{
					t=0;
				}
				else
				{
					s[++t]=s[i];
				}
			}
		}
		//==================
		putchar('[');
		for (i=1;i<=t;i++)
		{
			if (i>1) printf(", ");
			printf("%c",s[i]);
		}
		printf("]\n");
	}
	return 0;
}

void getdata(void)
{
	int i;
	char c1,c2,c3;
	memset(cb,0,sizeof(cb));
	memset(op,-1,sizeof(op));
	scanf("%d",&c);
	for (i=0;i<c;i++)
	{
		scanf(" %c %c %c",&c1,&c2,&c3);
		cb[c1-'A'][c2-'A']=c3;
		cb[c2-'A'][c1-'A']=c3;
	}
	scanf("%d",&d);
	for (i=0;i<d;i++)
	{
		scanf(" %c %c",&c1,&c2);
		op[c1-'A'][c2-'A']=0;
		op[c2-'A'][c1-'A']=0;
	}
	scanf("%d",&n);
	for (i=1;i<=n;i++)
		scanf(" %c",&s[i]);
}