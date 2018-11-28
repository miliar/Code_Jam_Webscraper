#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <cmath>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define mp make_pair
#define pb push_back

typedef long long ll;

using namespace std;

struct Plant
{
    double x,y,r;
};

double len(Plant &p1, Plant &p2)
{
    double dx = p1.x-p2.x;
    double dy = p1.y-p2.y;
    double rr = sqrt(dx*dx+dy*dy);
    return (rr+p1.r+p2.r)/2;
}

void solve(int kase)
{
    int n;

    Plant plant[50];
    
    scanf("%d",&n);
    REP(i,n) {
        scanf("%lf %lf %lf",&plant[i].x, &plant[i].y, &plant[i].r);
    }
    double s1=plant[0].r;
    double s2=1238123,s3=1298312;
    double sol = 0.;
    if(n > 1) {
        s1 = max(len(plant[0],plant[1]), plant[2].r);
    }
    if(n > 2) {
        s2 = max(len(plant[0],plant[2]), plant[1].r);
        s3 = max(len(plant[1],plant[2]), plant[0].r);
    }
    if(n == 2) { sol = max(plant[0].r, plant[1].r); }
    else { sol = min(s1,min(s2,s3)); }

    printf("Case #%d: %lf\n",kase,sol);
}

int main()
{
    int t;
    scanf("%d",&t);
    REP(i,t) solve(i+1);

	return 0;
}
