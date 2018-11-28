/* 
 * File:   main.cpp
 * Author: Mi
 *
 * Created on 2011年5月7日, 上午10:13
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
char str[105];
int sato[105],satb[105];
int main(int argc, char** argv)
{
        freopen("A-large.in","r",stdin);
        freopen("A-large.out","w",stdout);
        int t,n,ans,to,tb,cnto,cntb,cnt=1;
        scanf("%d",&t);
        while(t--)
        {
                to=tb=1;
                ans=0;
                cnto=cntb=0;
                memset(sato,0,sizeof(sato));
                memset(satb,0,sizeof(satb));
                scanf("%d",&n);
                for(int i=0;i<n;i++)
                {
                        int temp;
                        scanf(" %c %d",&str[i],&temp);
                        if(str[i]=='O')
                                sato[cnto++]=temp;
                        else
                                satb[cntb++]=temp;
                }
                for(int i=0,j=0,k=0,col=0;;col++)
                {
                        int flag=0;
                        if(j==cnto&&k==cntb)
                        {
                                ans=col;
                                break;
                        }
                        if(sato[j]>to&&sato[j])
                                to++;
                        else if(sato[j]<to&&sato[j])
                                to--;
                        else if(sato[j]==to)
                                if(str[i]=='O'&&!flag)
                                {
                                        j++;
                                        i++;
                                        flag=1;
                                }
                        if(satb[k]>tb&&satb[k])
                                tb++;
                        else if(satb[k]<tb&&satb[k])
                                tb--;
                        else if(satb[k]==tb)
                                if(str[i]=='B'&&!flag)
                                {
                                        k++;
                                        i++;
                                        flag=1;
                                }
                }
                printf("Case #%d: %d\n",cnt++,ans);
        }
        return 0;
}

