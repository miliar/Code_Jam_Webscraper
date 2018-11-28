/*
ID: kishwarshafin
PROG:
LANG: C++
*/
/*
Timus JI: 119454XP
*/
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 2147483647
#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)

struct triplate{
    int x;
    int y;
    int z;
};
vector<triplate>T[40][2];
bool color[31][11][11][11];
int nums[100];
int N,S,P;
int DP[101][101];



void dp(int ori,int num,int a,int b,int c)
{
    if(a==-1)
    {
        for(int i=0;i<=10;i++)
            if(num-i>=0)dp(ori,num-i,i,-1,-1);
    }
    else if(b==-1)
    {
        for(int i=0;i<=10;i++)
        {
            if(num-i>=0 && abs(a-i)<=2)
                dp(ori,num-i,a,i,c);
        }
    }
    else if(c==-1)
    {
        if(num>10)return;
        if(abs(a-num)>2)return;
        if(abs(b-num)>2)return;
        triplate A;
        A.x=a;
        A.y=b;
        A.z=num;
        if(color[ori][A.x][A.y][A.z]==false)
        {
            color[ori][A.x][A.y][A.z]=true;
            if(abs(A.x-A.y)==2 || abs(A.x-A.z)==2 || abs(A.y-A.z)==2)
                T[ori][0].push_back(A);
            else
                T[ori][1].push_back(A);
        }
    }
}

void gen()
{
    memset(color,0,sizeof(color));
    for(int i=0;i<=30;i++)
        dp(i,i,-1,-1,-1);
}

int solve(int n,int s)
{
    if(DP[n][s]!=-1)return DP[n][s];
    if(n==N)
    {
        return 0;
    }
    else
    {
        int num=nums[n];
        int a=0,b=0;
        if(T[num][0].size()!=0 && s>0)
        {
            bool boro=false;
            for(int i=0;i<T[num][0].size();i++)
            {
                int mx=max(T[num][0][i].x,max(T[num][0][i].y,T[num][0][i].z));
                if(mx>=P)
                {
                    boro=true;
                    break;
                }
            }
            if(boro==true)a=1+solve(n+1,s-1);
            else a=solve(n+1,s-1);
        }
        if(T[num][1].size()!=0)
        {
            bool boro=false;
            for(int i=0;i<T[num][1].size();i++)
            {
                int mx=max(T[num][1][i].x,max(T[num][1][i].y,T[num][1][i].z));
                if(mx>=P)
                {
                    boro=true;
                    break;
                }
            }
            if(boro==true)b=1+solve(n+1,s);
            else b=solve(n+1,s);
        }
        DP[n][s]=max(a,b);
        return DP[n][s];
    }
}



int main()
{
//    #ifndef ONLINE_JUDGE
//	in("in.txt");
//	out("out.txt");
//    #endif


    gen();

    int t,caseno=1;
    cin>>t;
    while(t--)
    {
        printf("Case #%d: ",caseno++);


        scanf("%d %d %d",&N,&S,&P);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&nums[i]);
        }
        memset(DP,-1,sizeof(DP));
        printf("%d\n",solve(0,S));
    }
	return 0;
}
