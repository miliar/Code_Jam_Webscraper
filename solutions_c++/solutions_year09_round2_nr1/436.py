#include <cstdio>
#include <vector>
#include <string>

using namespace std;

#define MAXP 10000

struct Point
{
	double w;
	string fea;
	Point(){fea="";}
};

Point P[MAXP];
vector<int> g[MAXP];
char s[10000];
int que[2000000];
int qh,qr;
int buildTree()
{
	qh=qr=0;
	que[qr++]=0;
	int ls=strlen(s);
	int p=0;
	int num=0;
	while (p<ls)
	{
		if (s[p]=='(')
		{
			p++;
			double w;
			sscanf(s+p,"%lf",&w);
			num++;
			P[num].w=w;
			while (isdigit(s[p])||s[p]=='.') p++;
			while (s[p]==' ') p++;
			if (islower(s[p]))
			{
				while (islower(s[p])) 
				{
					P[num].fea+=s[p];
					p++;
				}
			}
			while (s[p]==' ') p++;
			int pre=que[qr-1];
			g[pre].push_back(num);
			que[qr++]=num;
		}
		else if (s[p]==')')
		{
			p++;
			qr--;
		}
		else p++;

	}
	return num;
}

string f[10000];
double ans;
int nn;
void DFS(int k)
{
	int i;
	ans*=P[k].w;
	if (P[k].fea=="") return ;
	bool flag=false;
	for (i=1;i<=nn;i++)
	{
		if (f[i]==P[k].fea)
		{
			flag=true;
			break;
		}
	}
	if (flag==true) return DFS(g[k][0]);
	else return DFS(g[k][1]);
}

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,L,i,j,k,A;
	scanf("%d",&t);
	getchar();
	int cn=0;
	while (t--)
	{
		cn++;
		for (i=0;i<=1000;i++) 
		{
			g[i].clear();
			P[i].fea="";
			P[i].w=0.0;
		}
		scanf("%d",&L);
		getchar();
		int p=0;
		while (L--)
		{
			gets(s+p);
			while (s[p]!=0) p++;
			s[p++]=' ';
			s[p]=0;
		}
		int num=buildTree();
		printf("Case #%d:\n",cn);
		scanf("%d",&A);
		for (i=1;i<=A;i++)
		{
			char name[100];
			scanf("%s",name);
			scanf("%d",&nn);
			for (j=1;j<=nn;j++)
			{
				f[j]="";
				char tmp[100];
				scanf("%s",tmp);
				int ltmp=strlen(tmp);
				for (k=0;k<ltmp;k++) f[j]+=tmp[k];
				
			}
			ans=1.0;
			DFS(1);
			printf("%.7lf\n",ans);
		}
	}
}
/*
2
3
(0.5 cool
  ( 1.000)
  (0.5 ))
2
anteater 1 cool
cockroach 0
13
(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)
3
beaver 2 furry freshwater
trout 4 fast freshwater fishy rainbowy
dodo 1 extinct
*/
