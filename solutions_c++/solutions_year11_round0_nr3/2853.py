/* 
 * File:   main.cpp
 * Author: Mi
 *
 * Created on 2011年5月7日, 上午10:33
 */

#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <map>
#include <vector>
#include <stdlib.h>

using namespace std;

/*
 * 
 */
int a[1005];
long long sum;
int main(int argc, char** argv) 
{
        freopen("C-large.in","r",stdin);
        freopen("C-large.out","w",stdout);
        int t,n,cnt=1;

        scanf("%d",&t);
        while(t--)
        {
                int temp;
                sum=0;
                scanf("%d%d",&n,&a[0]);
                temp=a[0];
                for(int i=1;i<n;i++)
                {
                        scanf("%d",&a[i]);
                        temp^=a[i];
                }
                printf("Case #%d: ",cnt++);
                if(temp)
                        puts("NO");
                else
                {
                        sort(a,a+n);
                        for(int i=1;i<n;i++)
                                sum+=(long long)a[i];
                        printf("%lld\n",sum);
                }
                
        }
        return 0;
}

