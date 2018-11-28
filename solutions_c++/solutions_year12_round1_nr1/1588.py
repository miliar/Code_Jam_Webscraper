#include <cstdio>
#include <cmath>
#include <utility>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;
#define MAX 10001
#define ST first
#define ND second
#define MP make_pair
#define PII pair<int, int>
#define VI vector<int>

int t[MAX];

int main()
{
    int n;
    scanf("%d", &n);
    for(int ch = 1; ch <= n; ++ ch){
        int a, b;
        scanf("%d %d", &a, &b);
        double ent = b+2;
        double keep=1;
        double gl = 10000001;
        for(int i = 1, h = b; i <= a; ++ i, --h){
            double c;
            scanf("%lf", &c);
            keep *= c;
            double l;
            l = keep*(h+a-i)+(1-keep)*(h+b+2);
            if(l < gl) gl = l;
        }
        printf("Case #%d: %0.6lf\n", ch, min(ent, gl));
    }
}
