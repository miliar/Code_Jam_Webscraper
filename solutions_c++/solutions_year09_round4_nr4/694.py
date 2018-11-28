#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<stack>
#include<cstring>
#include<cstdlib>
#include<list>
#include<set>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define vi vector<int>
#define vd vector<double>
#define pii pair<int,int>
#define pdd pair<double,double>
using namespace std;
int tests,tcounter;
int N;
pii A[64];
int r[64];
double R;
double dist(pii a,pii b)
{
    return sqrt((double)(a.x-b.x)*(a.x-b.x)+(double)(a.y-b.y)*(a.y-b.y));
}
int main()
{
    int i,j,k;
    scanf("%d",&tests);
    for(tcounter=1;tcounter<=tests;++tcounter)
    {
        printf("Case #%d: ",tcounter);
        scanf("%d",&N);
        for(i=0;i<N;++i)scanf("%d %d %d",&A[i].x,&A[i].y,&r[i]);
        if(N==1)
        {
            printf("%.8lf\n",(double)r[0]);
            continue;
        }
        if(N==2)
        {
            R=max(r[0],r[1]);
            printf("%.8lf\n",R);
            continue;
        }
        double a=dist(A[0],A[1]),b=dist(A[1],A[2]),c=dist(A[2],A[0]);
        R=(a+r[0]+r[1])/2.0;
        R=min(R,(b+r[1]+r[2])/2.0);
        R=min(R,(c+r[0]+r[2])/2.0);
        printf("%.8lf\n",R);
    }
    return 0;
}
