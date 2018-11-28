#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <queue>
#include <cstring>
#include <stack>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int n;
        scanf("%d",&n);
        double res=0;
        int c;
        for(int k=0;k<n;k++)
        {
            scanf("%d",&c);
            if(c!=k+1)
                res++;
        }
        
        printf("Case #%d: %lf\n",i+1,res);
    }
}
