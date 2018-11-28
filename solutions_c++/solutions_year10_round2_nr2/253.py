/*
Program:
Author: ldl
Method:
DataStructure:
Date: 2010- -
Status:
Remark:
*/
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int n,k,b,t;
int x[100],v[100];

int main(){
//    freopen("test.txt","r",stdin);
    int T;
    scanf("%d", &T);
    for (int p = 1; p <= T ; p++){
        printf("Case #%d: ", p);
        scanf("%d%d%d%d", &n  , &k , &b, &t);
        for (int i = 1; i <= n ; i++)
          scanf("%d", &x[i]);
        for (int i = 1; i <= n ; i++)
          scanf("%d", &v[i]);
        int ans = 0 , cur = 0;
        for (int i = n; i >= 1 ; i--)
        {
           if (x[i] + v[i] * t >= b) k-- , ans += cur;
             else cur++;
           if (!k) break;
        }
        if (!k) printf("%d\n", ans);
          else printf("IMPOSSIBLE\n");
    }
    return 0;
}
  
