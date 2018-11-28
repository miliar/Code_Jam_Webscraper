#include <iostream>
#include <algorithm>
using namespace std;

double cb;
int l[1000],r[1000];
bool b[1000];
string s[1000];
string e[101];
double x[1000];
int db[1000];
int i,j,k,m,n,p,t,top,w;
bool ok;
char c;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> t;
	for (p=1; p<=t; p++)
	{
		cin >> k;
		memset(b,false,sizeof(b));
		top=0;
		m=0;
		i=0;
		while (1)
		{
			while (scanf("%c",&c))
			{
				if (c=='(') break;
				if (c==')') break;
				if (c=='\r' || c=='\n') i++;
			}
//			if (i>=k) break;
			
			if (c==')') {top--; if (top==0) break;}
			else
			{

			m++;
			if (!b[db[top]]) {b[db[top]]=true; l[db[top]]=m;} else r[db[top]]=m;
			top++;
			db[top]=m;
			scanf("%lf",&cb);
			x[m]=cb;
			s[m]="";
			while (scanf("%c",&c))
			{
				if (c==')') break;
				if (c=='\r' || c=='\n') {i++; break;}
				if (c>='a' && c<='z') s[m]=s[m]+c;
			}
			if (c==')') top--;
			
//			if (i>=k) break;
			if (top==0) break;
			}
		}
		cout << "Case #" << p << ": \n";
		scanf("%d",&n);
		for (i=1; i<=n; i++)
		{
			cin >> e[0];
			cin >> k;
			for (j=1; j<=k; j++)
				cin >> e[j];
			w=1;
			cb=1.0;
			while (1)
			{
				cb=cb*x[w];
				if (s[w]=="") break;
				ok=false;
				for (j=1; j<=k; j++)
					if (e[j]==s[w]) {ok=true; break;}
				if (ok) w=l[w]; else w=r[w];
			}
			printf("%.7lf\n",cb);
		}
	}

//	system("pause");
	return 0;
}
