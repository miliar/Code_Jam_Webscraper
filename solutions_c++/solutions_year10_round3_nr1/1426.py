#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
struct Npoint{double x,y;}P[1005][2];
int N;
double multi(Npoint p0,Npoint p1,Npoint p2){return (p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y);}
bool segcross(Npoint s1,Npoint e1,Npoint s2,Npoint e2)
{
    if(max(s1.x,e1.x)>=min(s2.x,e2.x)&&max(s1.y,e1.y)>=min(s2.y,e2.y)&&
    max(s2.x,e2.x)>=min(s1.x,e1.x)&&max(s2.y,e2.y)>=min(s1.y,e1.y)&&
    multi(s1,e1,s2)*multi(s1,e1,e2)<=0&&multi(s2,e2,s1)*multi(s2,e2,e1)<=0)
        return true;
    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large1.out","w",stdout);
    int T,i,j;double h1,h2;int cnt,Case=0;
    scanf("%d",&T);
    while(T--)
    {
        cnt=0;
        scanf("%d",&N);
        for(i=0;i<N;i++)
        {
            scanf("%lf%lf",&h1,&h2);
            P[i][0].x=0;P[i][0].y=h1;
            P[i][1].x=10;P[i][1].y=h2;
        }
        for(i=0;i<N;i++)
            for(j=i+1;j<N;j++)
                if(segcross(P[i][0],P[i][1],P[j][0],P[j][1]))
                    cnt++;
        printf("Case #%d: %d\n",++Case,cnt);
    }
    return 0;
}
