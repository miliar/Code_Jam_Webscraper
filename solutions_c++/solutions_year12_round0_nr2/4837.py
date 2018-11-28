#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
#include<string.h>
#include<map>
#include<vector>
#define MAX 1010

using namespace std;

int n,p,s;
int a[MAX];
int sol;

void solve()
{
    sol=0;
    for(int i=0;i<n;i++)
    {
        int d;

        if(a[i]<0 || a[i]>30) continue;
        if(a[i]==0)
        {
            if(p<=0) sol++;
            continue;
        }
        if(a[i]==29 || a[i]==30)
        {
            if(p<=10) sol++;
            continue;
        }

        if(a[i]%3==0)
        {
            d = a[i]/3;
            if(d>=p) sol++;
            else if(d+1>=p && s>0)
            {
                sol++;
                s--;
            }
        }
        else if(a[i]%3==1)
        {
            d = a[i]/3;
            if(d+1>=p) sol++;
        }
        else if(a[i]%3==2)
        {
            d = a[i]/3;
            if(d+1>=p)sol++;
            else if(d+2>=p && s>0)
            {
                sol++;
                s--;
            }
        }
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w+", stdout);
    int cases;
	scanf("%d\n",&cases);

	for(int i=1;i<=cases;i++)
	{
	    scanf("%d%d%d",&n,&s,&p);
	    for(int i=0;i<n;i++)
	    {
	        scanf("%d",&a[i]);
	    }
        solve();
        printf("Case #%d: %d\n",i,sol);
	}

    return 0;
}


