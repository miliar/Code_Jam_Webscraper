/* 
 * File:   main.cpp
 * Author: Mi
 *
 * Created on 2011年5月7日, 上午9:19
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
char com[37][5],cle[30][3],str[105];
int main(int argc, char** argv)
{
        freopen("B-small-attempt2.in","r",stdin);
        freopen("B-small-attempt2.out","w",stdout);
        int t,c,d,n,cnt=1;
        scanf("%d",&t);
        while(t--)
        {
                memset(str,0,sizeof(str));
                scanf("%d",&c);
                for(int i=0;i<c;i++)
                        scanf("%s",&com[i]);
                scanf("%d",&d);
                for(int i=0;i<d;i++)
                        scanf("%s",&cle[i]);
                scanf("%d ",&n);
                int f=0,ff=0;
                int j=-1;
                for(int i=0;i<n;i++)
                {
                        char temp;
                        scanf("%c",&temp);
                        str[++j]=temp;
                        if(i)
                        {
                                for(int k=0;k<c;k++)
                                {
                                        if(str[j-1]==com[k][0]&&str[j]==com[k][1]||str[j-1]==com[k][1]&&str[j]==com[k][0])
                                        {
                                                if(j==f)
                                                        f=0;
                                                if(j==ff)
                                                        ff=0;
                                                str[j-1]=com[k][2];
                                                j--;
                                        }
                                }
                        }
                        for(int k=0;k<d;k++)
                        {
                                if(str[j]==cle[k][0]&&!f)
                                        f=j+1;
                                if(str[j]==cle[k][1]&&!ff)
                                        ff=j+1;
                                if(ff&&f)
                                {
                                        f=ff=0;
                                        j=-1;
                                }
                        }
                }
                str[j+1]='\0';
                if(j==-1)
                        printf("Case #%d: []\n",cnt++);
                else
                {
                        printf("Case #%d: [%c",cnt++,str[0]);
                        for(int i=1;i<=j;i++)
                                printf(", %c",str[i]);
                        printf("]\n");
                }
                //puts(str);
        }
        return 0;
}

