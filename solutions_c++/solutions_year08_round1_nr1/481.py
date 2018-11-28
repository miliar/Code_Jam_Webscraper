#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

int a[1000];
int b[1000];
int main()
{
    int t;
    scanf("%d",&t);
    int ct=1;
    while (t--)
    {
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        for (int i=0;i<n;i++)
        {
            scanf("%d",&b[i]);
        }
        sort(a,a+n);
        sort(b,b+n,greater<int>());
        int res=0;
        for (int i=0;i<n;i++)
            res+=a[i]*b[i];
        printf("Case #%d: %d\n",ct,res);
        ct++;
    }
    return 0;
}

        
