// 3550.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


#include <iostream>
#include <algorithm>
using namespace std;
const int inf = 1 << 30;
int p,q;
int sz[13],num[110];
int cal()
{
    int res = 0;
    bool asd[110] = {0};
    for(int i = 1; i <= q; i++)
    {
        int now = num[sz[i]];    
        for(int j = now-1; j >= 1;j--)
        {
            if(asd[j]) break;
            res++;    
        }
        for(int j = now+1; j <= p; j++)
        {
            if(asd[j]) break;
            res++; 
        }
        asd[now] = 1;
    }
    return res;    
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out1.txt", "w", stdout);
    int t,i,j,k,cnt,res,mid,t1;
    scanf("%d",&t);
	t1=1;
    while(t--)
    {
        scanf("%d %d",&p,&q);     
        cnt=1;
        for(i=1;i<=q;i++)
        {
            cnt*=i;
            sz[i]=i;
            scanf("%d",&num[i]);
        } 
        res = inf;
        while(cnt--)
        {
            mid = cal();       
            res = min(res, mid);        
            next_permutation(sz+1, sz+1+q);
        }
        printf("Case #%d: %d\n", t1, res);
		t1++;
    }    
}
