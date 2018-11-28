#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <string.h>
#include <cstring>

using namespace std;

int t;

int is_good(string p)
{
	int n=p.length();
	int i;

	if (n==0) return 0;

	for (i=0; i<n; i++)
		if (p[i]=='.') return 0; else
			if (p[i]=='('||p[i]==')') return 0; else
				if (p[i]-'a'>=0&&p[i]-'a'<26) return 0;

	return 1;
}

string tek;
string x;

int d[10000];
int g[10000];
int stk[10000];
double pp[10000];
string xp[10000];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d\n",&t);

	int mx=0;

	for (int tt=1; tt<=t; tt++)
	{
		memset(d,0,sizeof(d));
		memset(pp,0,sizeof(pp));
		memset(g,0,sizeof(g));
		for (int i=0; i<1000000; i++)
			xp[i]="";
		int n;
		scanf("%d\n",&n);

		tek=""; x="";
		while (!is_good(x))
		{
			tek+=x;
			cin>>x;
		}
		
		int xx=0;
		int p=x.length();

		int i,j;

		for (i=0; i<p; i++)
			xx*=10, xx+=x[i]-'0';

		int nn=tek.length();

		int ver=0;
		for (i=0; i<nn; i++)
			if (tek[i]=='(')
			{
				ver++;
				stk[ver]=i;

				double k=0;
				int tk=i+1;
				int poin=0; double stp=10.0;
				while ((tek[tk]-'0'>=0&&tek[tk]-'0'<=9)||tek[tk]=='.')
				{
					if (tek[tk]=='.') poin=1; else
					if (poin==0) k*=10.0, k+=tek[tk]-'0'; else
					{
						k+=(double)(tek[tk]-'0')/stp;
						stp*=10.0;
					}	

					tk++;
				}

				if (tek[tk]!=')')
				{
					while (tek[tk]!='(')
					{
						xp[i]+=tek[tk];
						tk++;
					}
				}

				pp[i]=k;
			} else
				if (tek[i]==')')
				{
					ver--;
					d[stk[ver+1]]=i;
					g[stk[ver+1]]=ver+1;
				}

				tek+='(';

		/*for (i=0; i<nn; i++)
			if (d[i]!=0)
			printf("%d %d %.7lf %d ",i,d[i],pp[i],g[i]), cout<<xp[i]<<endl;
*/
		printf("Case #%d:\n",tt);
		for (i=1; i<=xx; i++)
		{
			cin>>x;
			int m;
			scanf("%d",&m);

			string ss[200];

			for (j=1; j<=m; j++)
				cin>>ss[j];

			int pwt=0;
			int dwt=1;
			double res=1;

			while (pwt<nn&&dwt==1)
			{
				if (tek[pwt]=='(')
				{
					int fk=0;
					if (xp[pwt]=="")
					{
						res*=pp[pwt];
						dwt=0;
					} else
					{
						res*=pp[pwt];
					
						for (j=1; j<=m; j++)
							if (ss[j]==xp[pwt])
							{
								pwt++;
								while (tek[pwt]!='(') pwt++;
								fk=1;
								break;
							}

						if (fk==0)
						{
							pwt++;
							while (tek[pwt]!='(') pwt++;
						}

						if (fk==0&&tek[d[pwt]+1]=='(') pwt=d[pwt]+1; else
							if (fk==0) dwt=0;
					}
				}
			}

			printf("%.7lf\n",res);
		}

		//cout<<tek;
		mx=max(mx,nn);
	}

	//printf("%d\n",mx);

	return 0;
}