#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define erro 1e-12
#define igual(X,Y) ( fabs((X) - (Y)) < erro)

int main() {
    int n,res,a,b,j;
    scanf("%d" , &n);
    vi x;
    vi y;
    for(int i=1;i<=n;i++) {
        x.clear();
        y.clear();
        scanf("%d" , &a);
        for(j=0;j<a;j++) {
            scanf("%d" ,&b);
            x.push_back(b);
        }

        for(j=0;j<a;j++) {
            scanf("%d" ,&b);
            y.push_back(b);
        }

        sort(x.begin(),x.end());
        sort(y.begin(),y.end());
    
        res = 0;
      
        for(j=0;j<a;j++) {
            res += x[j]*y[a-1-j];
        }

        int aux = 0;
        for(j=0;j<a;j++) {
            aux += y[j]*x[a-1-j];
        }

        res = min(res,aux);

        printf("Case #%d: %d\n" , i, res);
    }
    return 0;
}

