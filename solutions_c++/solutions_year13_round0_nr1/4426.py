#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include<stack>
#include<vector>
#include<cstring>
#include<set>
#include<map>
typedef long long int LL;
typedef unsigned long long int ULL;
#define sf(a) read_int(a)
#define pf(a) printf("%d",a);
#define sz(a) int((a).size())
#define all(c) c.begin(),c.end() //all elements of a container
#define rall(c) c.rbegin(),c.rend() 
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //traversing a container..works for any type of container
#define present(container, element) (container.find(element) != container.end())    //used for set...return 1 if el is ps 0 otherwise
#define cpresent(container, element) (find(all(container),element) != container.end())  //same as present...but is for vectors
using namespace std;
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(x) ((x) > 0 ? (x) : -(x))
#define REP(i, n) for (int i = 0 ; i < (n) ; i ++)
#define FOR(i, s, n) for (int i = (s) ; i < (n) ; i ++)
#define SET(v, val) memset(v, val, sizeof(v))
inline void read_int (int &n)
{
	n = 0;
	int i = getchar_unlocked();
	while (i < '0' || i > '9')
		i = getchar_unlocked();

	while (i >= '0' && i <= '9')
	{
		n = (n << 3) + (n << 1) + (i - '0');
		i = getchar_unlocked();
	}

}
typedef struct ptr
{
	int x,o,t;
}stud;
int main()
{
	int n,ans=0;
	char c;
	sf(n);
	while(n--)
	{
		ans++;
		stud row[4],col[4],diag[2];
		char ch[4][4];
		int i,j,nflag=0;
		for(i=0;i<2;i++)
			diag[i].x=diag[i].o=diag[i].t=0;
		for(i=0;i<4;i++)
			row[i].x=row[i].o=row[i].t=col[i].x=col[i].o=col[i].t=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>ch[i][j];
				if(ch[i][j]=='X')
				{
					row[i].x+=1;
					col[j].x+=1;
					if(i==j)
						diag[0].x+=1;
					else if(i+j==3)
						diag[1].x+=1;
				}
				else if(ch[i][j]=='O')
				{
					row[i].o+=1;
					col[j].o+=1;
					if(i==j)
						diag[0].o+=1;
					else if(i+j==3)
						diag[1].o+=1;
				}
				else if(ch[i][j]=='T')
				{
					row[i].t+=1;
					col[j].t+=1;
					if(i==j)
						diag[0].t+=1;
					else if(i+j==3)
						diag[1].t+=1;
				}
				else if(ch[i][j]=='.')
					nflag=1;
			}
		}
		string s1="X won",s2="O won",s3="Game has not completed",s4="Draw";
		if(row[0].x+row[0].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(row[0].o+row[0].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(row[1].x+row[1].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(row[1].o+row[1].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(row[2].x+row[2].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(row[2].o+row[2].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(row[3].x+row[3].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(row[3].o+row[3].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(col[0].x+col[0].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(col[0].o+col[0].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(col[1].x+col[1].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(col[1].o+col[1].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(col[2].x+col[2].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(col[2].o+col[2].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(col[3].x+col[3].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(col[3].o+col[3].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(diag[0].x+diag[0].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(diag[0].o+diag[0].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(diag[1].x+diag[1].t==4)
		{
			printf("Case #%d: %s\n",ans,s1.c_str());
			continue;
		}
		else if(diag[1].o+diag[1].t==4)
		{
			printf("Case #%d: %s\n",ans,s2.c_str());
			continue;
		}
		else if(nflag==1)
		{
			printf("Case #%d: %s\n",ans,s3.c_str());
			continue;
		}
		else 
		{
			printf("Case #%d: %s\n",ans,s4.c_str());
			continue;
		}
	}
	return 0;
}
