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

#define maxn 110
#define datat int
#define ansdatat int

int st, tot[10], cat[10];

void set_tot(int num){
     int a;
     while (num>0){
           a  = num%10;
           if (a>0) tot[a]++;
           num/=10;
     }
}

bool check(int num){
     memset(cat, 0, sizeof(cat));
     int a;
     while (num>0){
           a  = num%10;
           if (a>0) cat[a]++;
           if (cat[a]>tot[a]) return false;
           num/=10;
     }
     for (int i = 1;i<=9;i++)
     if (cat[i] < tot[i]) return false;
     return true;
}

int main(){
	
//	freopen(".in", "r", stdin);
    int tttt;
    scanf("%d", &tttt);
    for (int ttt = 1;ttt<=tttt;ttt++){
        scanf("%d", &st);
        memset(tot, 0, sizeof(tot));
        set_tot(st);
        int ans = st+1;
        while (!check(ans)){
              ans++;
        }
        printf("Case #%d: %d\n", ttt,ans);
    }

	

	return 0;
};

