#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <queue>
#include <set>
#include <cmath>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int inf=(1<<30);
#define mset(a,x) memset(a,x,sizeof(a))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
#define dbg(x) cerr<<#x<<" : "<<x<<endl
struct node {
	   int son[2];
	   int cnt;
       double p;
	   string pv;
};

string name[1005];

node adj[1005];

map<string, map<string, bool> > Map;

char str[1001][1001];

int n, m;
int tot;

void con(int &x, int &y, int id) {
    // printf("%d %d %d\n", x, y, id);
	 if (x >= n) return;
	 while (str[x][y]==' ' || str[x][y]=='\n') {
	        y++;
			if (str[x][y]==0) {
			    x++;
				y=0;
			}
			if (x >= n) return;
	 }
	 if (str[x][y] == '(') {
		 string tmp;
		 while (!((str[x][y]>='0' && str[x][y]<='9') || str[x][y]=='.')) {
		        y++;
			    if (str[x][y]==0) {
			        x++;
				    y=0;
			    }
		 }
	     while ((str[x][y]>='0' && str[x][y]<='9') || str[x][y]=='.') {
		        tmp.push_back(str[x][y]);
				y++;
			    if (str[x][y]==0) {
			        x++;
				    y=0;
			    }
		 }
		 stringstream line(tmp);
		 line >> adj[id].p;
	 }
	 //puts("flag");
	 char ch;
	 while (true) {
			if (x >= n) break;
			ch = str[x][y];
	        if (ch == ')')
				break;
			if (ch == '(') {
				adj[id].son[adj[id].cnt++] = ++tot;
			    con(x, y, tot);
			}
			if (ch >= 'a' && ch <= 'z')
			    adj[id].pv.push_back(ch);
			y++;
	        if (str[x][y]==0) {
	            x++;
		        y=0;
	        }
	 }
	 
}
double go(int id, int num, double p) {
       if (adj[id].cnt == 0) {
	       return p*adj[id].p;
	   }
	   else {
	       if (Map[name[num]][adj[id].pv]) {
		       return go(adj[id].son[0], num, p*adj[id].p);
		   }
		   else {
		       return go(adj[id].son[1], num, p*adj[id].p);
		   }
	   }
}
int main() 
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T, cnt=0;
    scanf("%d", &T);
	while (T--) {
		   Map.clear();
		   tot = 1;
		   for (int i = 0; i < n; i++) {
		        adj[i].son[0] = adj[i].son[1] = 0;
				adj[i].cnt = 0;
				adj[i].p = 0;
				adj[i].pv = "";
		   }
		   scanf("%d", &n);
		   getchar();
	       for (int i = 0; i < n; i++)
			    gets(str[i]);
		   cin >> m;
		   string str2;
           for (int i = 0; i < m; i++) {
		        int x;
				cin >> name[i] >> x;
				
				for (int j = 0; j < x; j++) {
				     cin >> str2;
					 Map[name[i]][str2] = true;
				}
		   }
		   int px=0, py=0;
		   con(px, py, 1);
		   printf("Case #%d:\n", ++cnt);
		   for (int i = 0; i < m; i++) {
		        printf("%.7lf\n", go(1, i, 1.0));
		   }
 	}
    return 0;
}
