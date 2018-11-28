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

#define maxn 510
#define datat int
#define ansdatat int

int f[maxn][maxn],ans, n, m;

char chs[1000];

string  s,sw = "welcome to code jam";

int main(){
	
 	int tttt;
	scanf("%d", &tttt);
    getline(cin,s);
	int ttt = 0;
	while (tttt-->0){
          ttt++;
          //scanf("%s", chs);
          getline(cin,s);
          memset(f,0,sizeof(f));
          f[0][0] = 1;
          n = sw.size();
          m = s.size();
//          cout<<sw<<endl;
//          cout<<s<<endl;
          for (int i = 1;i<=n;i++)
          for (int j = 1;j<=m;j++)
          if (sw[i-1] == s[j-1]){
              f[i][j] = 0;
              for (int k = 0;k<j;k++){
                  f[i][j] = (f[i][j] + f[i-1][k])%10000;
              }
          }
          ans = 0;
          for (int j = 1;j<=m;j++)
              ans = (ans+f[n][j])%10000;
          
          printf("Case #%d: %04d\n", ttt, ans);
    }

	

	return 0;
};

