#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

int cnt[65536]={0};
char str[10];
int main()
{
    int n,temp,max=0,maxnum=0,start;
    scanf("%d",&n);
    getchar();
    for(int i=1;i<=n;i++)
        {
            gets(str);
            temp=start=0;
            while(str[start])
               temp=(temp<<3)+(temp<<1)+str[start++]-'0';
            cnt[temp]++;
            if((cnt[temp]>max)||((cnt[temp]==max)&&(temp<maxnum)))
                {
                max=cnt[temp];
                maxnum=temp;
                }
        }
    printf("%d\n%d\n",maxnum,max);
}
