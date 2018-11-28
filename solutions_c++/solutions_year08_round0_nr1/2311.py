#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 1010
#define datat int
#define ansdatat int

int n,m,x[maxn],f[maxn][maxn],g[maxn];
int inf = 100000;

int main(){
	
//	freopen("a.txt", "r", stdin);
	
	int ttt;
    scanf("%d", &ttt);
    string s;
	for (int ti = 0;ti<ttt;ti++){
        scanf("%d", &m);
        getline(cin,s);
        map<string,int> ha;
        for (int i = 1;i<=m;i++){
            getline(cin, s);
            ha[s] = i;
        }
        
        scanf("%d", &n);
        getline(cin,s);
        for (int i = 1;i<=n;i++){
            getline(cin, s);
            x[i] = ha[s];
        }
        
        g[1] = 0;
        for (int i = 1;i<=m;i++)
            if (x[1] != i) 
               f[1][i] = 0;
            else
               f[1][i] = inf;
            
        for (int i = 2;i<=n;i++){
            g[i] = inf;
            for (int j = 1;j<=m;j++)
            if (x[i] == j) f[i][j] = inf;
            else{
                 f[i][j] = f[i-1][j];
                 if (f[i][j] > g[i-1]+1)
                     f[i][j] = g[i-1]+1;
                 if (g[i] > f[i][j])
                     g[i] = f[i][j];
                 
                 
            }
            //cout<<i<<" "<<g[i]<<endl;
        }
        
        printf("Case #%d: %d\n", ti+1, g[n]);
        
        
    }
	

	

	return 0;
};

