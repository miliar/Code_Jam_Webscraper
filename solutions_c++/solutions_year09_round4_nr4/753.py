#include<iostream>
#include<iomanip>
#include<cmath>
#include<vector>

struct plant
{
    int x,y,r;
};
int n;
plant plants[100];
int partition[100];

std::vector<int> parts[2];
double circle_r(int p)
{
    if(parts[p].size()==1)return plants[parts[p][0]].r;
    double m = 0;
    for(int i=0;i<parts[p].size();i++)
    {
        plant a = plants[parts[p][i]];
        for(int j=i+1;j<parts[p].size();j++)
        {
            plant b = plants[parts[p][j]];
            double d = sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2))+a.r+b.r;
            if(d>m)m = d;
        }
    }
    return m/2;
}

/*
void make_partition(int a,int b,int side)
{
    plant ap = plants[a];
    plant bp = plants[b];
    double kulma = (bp.y-ap.y)/double(
}*/

bool intersect(int a,int b,int c,int d)
{
    double ya = plants[a].y;
    double xa = plants[a].x;
    double yb = plants[b].y;
    double xb = plants[b].x;
    yb-=ya;
    xb-=xa;
    double yc = plants[c].y;
    double xc = plants[c].x;
    double yd = plants[d].y;
    double xd = plants[d].x;
    yd-=yc;
    xd-=xc;
    
    double bxd = xb*yd-xd*yb; 
    if(bxd==0)return false;
    yd/=bxd;
    xd/=bxd;
    yc-=ya;
    xc-=xa;
    double t = (xc*yd-xd*yc);
    if(0<=t and t<=1)return true;
    return false;
}

bool can_add(int p,int i)
{
   for(int t=0;t<parts[p].size();t++)
   {
       for(int a=0;a<parts[!p].size();a++)
       {
           for(int b=a+1;b<parts[!p].size();a++)
           {
               if(intersect(i,parts[p][t],parts[!p][b],parts[!p][a]))
               {
                   return false;
               }
           }
       }
   }
   return true;
}
double solve(int i)
{
    if(i==n)
    {
        return circle_r(0)+circle_r(1);
    }
    double m = 100000;
    //add to 0
    if(can_add(0,i))
    {
        parts[0].push_back(i);
        m = std::min(m,solve(i+1));
        parts[0].pop_back();
    }
    if(can_add(1,i))
    {
        parts[1].push_back(i);
        m = std::min(m,solve(i+1));
        parts[1].pop_back();
    }
    return m;
}

int main()
{
    int c;
    std::cin>>c;
    for(int cn=1;cn<=c;cn++)
    {
        std::cin>>n;
        for(int i=0;i<n;i++)
        {
            plant p;
            std::cin>>p.x>>p.y>>p.r;
            plants[i]=p;
        }
//        std::cout<<intersect(0,1,2,3)<<"\n";
//        std::cout<<solve(0)<<"\n";
        double m = 1000000;
        for(int i=0;i<1<<n;i++)
        {
            parts[0].clear();
            parts[1].clear();
            for(int j=0;j<n;j++)
            {
                if(i&(1<<j))
                {
                    parts[0].push_back(j);
                }else
                {
                    parts[1].push_back(j);
                }
            }
            m = std::min(m,std::max(circle_r(0),circle_r(1)));
        }
        std::cout<<"Case #"<<cn<<": "<<std::fixed<<m<<"\n";
    }
}
