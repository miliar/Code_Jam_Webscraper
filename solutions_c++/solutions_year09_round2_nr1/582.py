#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <cstring> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <string> 
#include <cmath> 
#include <queue> 
#include <map> 
#include <stack>
#include <set> 

using namespace std; 

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long ll; 

#define sz size() 
#define pb push_back 
#define MAX 0x3FFFFFFF 
#define all(x) (x).begin(),(x).end() 
#define For(i,n) for(int i=0, _n=(n);i<_n;++i) 
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i) 

double ans;
map<string,vector<double> > pr;
map<string,vector<string> > tree;
map<string,int> mm;

void visit(string str)
{
	if(mm[str])
	{
		ans *= pr[str][0];
		if(tree[str][0] != "!!!") 
			visit(tree[str][0]);
	}
	else
	{
		ans *= pr[str][1];
		if(tree[str][1] != "!!!") 
			visit(tree[str][1]);
	}
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tn;
	int ti=0;
	scanf("%d",&tn);
	while(tn--)
	{
		int line;
		scanf("%d ",&line);
		stack<string> s;
		string par="root";
		s.push("root");
		pr.clear();
		tree.clear();
		int state=0,xx=0;
		For(ww,line)
		{
			char p[200];
			char p2[200];
			fgets(p, 128, stdin);
			strcat(p," ");
			int t=0;
			For(i,strlen(p))
			{
				if(p[i]=='(')
				{
					t=xx=0;
				}
				else if(p[i]==')' || p[i]==' ')
				{
					if(t) p2[t]=0;
					if(t && state==1)
					{
						pr[par].push_back(atof(p2));
					}
					if(t && state==2)
					{
						string str=string(p2);
						s.push(str);
						tree[par].push_back(str);
						par=str;
					}
					t=0;
					if(p[i]==')') 
					{
						if(state==1) 
							tree[par].push_back("!!!");
						if(xx) s.pop();
						par=s.top();
						xx=1;
						state=0;
					}
				}
				else if(p[i]>='0' && p[i]<='9' || p[i]=='.')
				{
					state=1;
					p2[t++]=p[i];
				}
				else if(p[i] >= 'a' && p[i] <= 'z')
				{
					state=2;
					p2[t++]=p[i];
				}
			}
		}
		if(tree["root"].size() == 1) tree["root"].push_back("!!!");
		int nn;
		printf("Case #%d:\n", ++ti);
		scanf("%d",&nn);
		while(nn--)
		{
			char name[128];
			int n;
			scanf("%s %d",name,&n);
			mm.clear();
			For(i,n) 
			{
				char p[128];
				scanf("%s",p);
				mm[string(p)] = 1;
			}
			mm["root"]=1;
			string cur="root";
			ans = 1;
			//ans *= pr["root"][0];
			visit("root");
			printf("%lf\n", ans+1e-12);
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