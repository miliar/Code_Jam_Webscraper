#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) ((a)*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
	int pos;
	int ind;
	node(int pos,int ind):pos(pos),ind(ind) {
	}
};
typedef vector<node> vn ; 
int cases,g,n;
queue<node> q[2];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
		int ret=0;
		printf("Case #%d: ",g+1);
		scanf("%d ",&n);
		for(i=0;i<2;i++)
			while(!q[i].empty())
				q[i].pop();
		for(i=0;i<n;i++)
		{
			char c[10];
			int x;
			scanf("%s %d",&c,&x);
			if(c[0]=='O')
				q[0].push(node(x,i));
			else
				q[1].push(node(x,i));
		}
		int pos[2];
		pos[0] = pos[1] = 1;
		while(!q[0].empty() || !q[1].empty() ) {
			int cur;
			if(q[0].empty())
				cur=1;
			else if(q[1].empty())
				cur=0;
			else
				cur = q[0].front().ind < q[1].front().ind ? 0 :1;
			int extra = abs(q[cur].front().pos-pos[cur]) + 1;
			pos[cur]= q[cur].front().pos;
			ret+=extra;
			if(!q[!cur].empty()) {
				int d=  abs(q[!cur].front().pos-pos[!cur]);
				if(d <= extra)
					pos[!cur]=q[!cur].front().pos;
				else {
					if(pos[!cur] < q[!cur].front().pos)
						pos[!cur]+=extra;
					else 
						pos[!cur]-=extra;
				}


			}
			q[cur].pop();
		}
		printf("%d\n",ret);
	}

	return 0;
}