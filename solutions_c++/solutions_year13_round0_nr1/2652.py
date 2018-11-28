#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int t,i,j,o,o1,x,x1,t1,test,dot,dot1,tc,f,c;
     freopen("C:\\Users\\SAGAR\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\SAGAR\\Desktop\\output.txt","w",stdout);
    scanf("%d",&test);
    for(tc=1;tc<=test;tc++)
    {
                           o=o1=x=x1=t=t1=0;
                        char a[4][4];c=f=0;
                        for(i=0;i<4;i++)
                        scanf("%s",a[i]);
                        for(i=0;i<4;i++)
                        {
                                        if(a[i][i]=='X')
                                        x++;
                                        else if(a[i][i]=='O')
                                        o++;
                                        else if(a[i][i]=='T')
                                        t++;
                                        if(a[3-i][i]=='X')
                                        x1++;
                                        else if(a[3-i][i]=='O')
                                        o1++;
                                        else if(a[3-i][i]=='T')
                                        t1++;
                        }
                        if(x+t==4||x1+t1==4)
                        {
                        printf("Case #%d: X won\n",tc);
                        continue;
                        }
                        if(o+t==4||o1+t1==4)
                        {
                        printf("Case #%d: O won\n",tc);
                        continue;
                        }
                        for(i=0;i<4;i++)
                        {
                                        o=o1=x=x1=t=t1=dot=dot1=0;
                                        for(j=0;j<4;j++)
                                        {
                                                        if(a[i][j]=='X')
                                                        x++;
                                                        else if(a[i][j]=='O')
                                                        o++;
                                                        else if(a[i][j]=='T')
                                                        t++;
                                                        else
                                                        dot++;
                                        }
                                        for(j=0;j<4;j++)
                                        {
                                                        if(a[j][i]=='X')
                                                        x1++;
                                                        else if(a[j][i]=='O')
                                                        o1++;
                                                        else if(a[j][i]=='T')
                                                        t1++;
                                                        else dot1++;
                                        }
                                        if(x+t==4||x1+t1==4)
                                        {
                                        c=1;
                                        printf("Case #%d: X won\n",tc);
                                        break;
                                        }
                                        if(o+t==4||o1+t1==4)
                                        {
                                        c=1;
                                        printf("Case #%d: O won\n",tc);
                                        break;
                                        }
                                        if(dot!=0||dot1!=0)
                                        f=1;
                                        
                        }
                        if(c)
                        continue;
                        if(f)
                        printf("Case #%d: Game has not completed\n",tc);
                        else
                        printf("Case #%d: Draw\n",tc);
    }
    return 0;
}
