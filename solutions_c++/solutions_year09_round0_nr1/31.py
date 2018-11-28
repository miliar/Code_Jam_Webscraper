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

#define maxn 5010
#define maxl 5010
#define maxd 5010
#define datat int
#define ansdatat int

int l,d,n,ans, tt,mark[maxl][30];
char word[maxd][maxl], now[maxl];

int main(){
	
	scanf("%d%d%d", &l, &d, &n);
	for (int i = 1;i<=d;i++){
       scanf("%s", word[i]);
    }
    
    for (int i = 1;i<=n;i++){
        tt++;
        ans = 0;
        scanf("%s", now);
        string s = now;
        for (int j = 0;j<l;j++){
            if (s[0] == '('){
               s.erase(0,1);
               while (s[0] != ')'){
                 mark[j][s[0]-'a'] = tt;
                 s.erase(0,1);
               }
               s.erase(0,1);
            }
            else{
                 mark[j][s[0]-'a'] = tt;
                 s.erase(0,1);
            }
        }
        for (int j = 1;j<=d;j++){
            bool yes = true;
            for (int k = 0;k<l;k++)
            if (mark[k][word[j][k]-'a'] != tt){
               yes = false;
               break;
            }
            if (yes) ans++;
        }
        printf("Case #%d: %d\n", i, ans);
    }

	

	return 0;
};

