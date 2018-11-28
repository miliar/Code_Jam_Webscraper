#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int a[4][4];
char s[10];
int i,j,k,n,m;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.txt","w",stdout); 
    int cs,t=0;
    char ch;
    scanf("%d",&cs);
    while (t++ < cs)
    {
        for (i = 0 ; i< 4; i++)
        {
            scanf("%s",s);
            for (j = 0 ; j < 4; j++)
            {
                ch=s[j];
                if (ch=='O') a[i][j]=1;
                else if (ch=='X') a[i][j]=2;
                else if (ch=='T') a[i][j]=3;
                else a[i][j]=0;
            }
        }
        int now,cur;
        int ok = 3;
        for (int i = 0 ; i < 4; i++)
        {
            now=3;cur=0;
            for (int j = 0; j < 4; j++)
            {
                now &= a[i][j];
                cur+=(a[i][j]==3);
            }
         //   cout<<now<<' '<<cur<<endl;
            if (now!=0 && cur < 2)
            ok = now;
        }
        for (int i = 0 ; i < 4; i++)
        {
            now=3;cur=0;
            for (int j = 0; j < 4; j++)
            {
                now &= a[j][i];
                cur+=(a[j][i]==3);
            }
            if (now!=0 && cur < 2)
            ok = now;
        }
        now=3;cur=0;
            for (int j = 0; j < 4; j++)
            {
                now &= a[j][j];
                cur+=(a[j][j]==3);
            }
            if (now!=0 && cur < 2)
            ok = now;
 now=3;cur=0;
            for (int j = 0; j < 4; j++)
            {
                now &= a[j][3-j];
                cur+=(a[j][3-j]==3);
            }
            if (now!=0 && cur < 2)
            ok = now;
        if (ok != 1 && ok != 2)
           for (int i = 0 ; i < 4; i++) for (int j = 0; j<4;j++) if (a[i][j]==0) ok=a[i][j];
        if (ok==0) printf("Case #%d: Game has not completed\n", t);
        if (ok==1) printf("Case #%d: O won\n", t);
        if (ok==2) printf("Case #%d: X won\n", t);
        if (ok==3) printf("Case #%d: Draw\n", t);
        
    }
}
