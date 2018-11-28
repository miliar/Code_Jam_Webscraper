#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>

using namespace std;

//BEIGINTEMPLATE
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(
typedef long long int64;//NOTES:int64
const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps
template <class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template <class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
typedef pair<int,int> ipair;//NOTES:ipair
//ENDTMPLATE

const int maxD=5010;
const int maxL=20;

string dic[maxD];
string w;
int L,D,N,ans;
int g[maxL],next[maxL*maxL],num;
char ev[maxL*maxL];

void insert(int u,char v)
{
	next[++num]=g[u]; g[u]=num; ev[num]=v;	
}

void solve()
{
	memset(g,0,sizeof(g));
	memset(next,0,sizeof(next));
	memset(ev,0,sizeof(ev));
	num=0;
	int i,j=0;
	for(i=1;i<=L;i++)
	{
		if(w[j]!='(')
		{
			insert(i,w[j++]);
			continue;
		}
		j++;
		while(w[j]!=')')insert(i,w[j++]);
		j++;
	}

	ans=0;
	int k;
	bool flag;
	for(i=1;i<=D;i++)
	{
		for(j=0;j<L;j++)
		{
			flag=false;
			for(k=g[j+1];k;k=next[k])
				if(ev[k]==dic[i][j]){
					flag=true; break;
				}
			if(!flag)break;
		}
		if(flag)ans++;
	}
	printf("%d\n",ans);
}

int main()
{
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("A-test.in","r",stdin);
	//freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j;
	char tmp[maxL*maxL];
	scanf("%d%d%d",&L,&D,&N);gets(tmp);
	for(i=1;i<=D;i++)
	{
		gets(tmp);
		dic[i]=tmp;
	}
	for(i=1;i<=N;i++)
	{
		gets(tmp);
		w=tmp;
		printf("Case #%d: ",i);
		solve();
	}
	fclose(stdout);
//	freopen("CON","r",stdin);
//	system("PAUSE");
	return 0;
}