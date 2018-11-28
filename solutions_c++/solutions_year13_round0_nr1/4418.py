#include<stdio.h>
#include<stdlib.h>

int a[5][5];
char s[5];
int main()
{
    freopen("C:\\Users\\lovelotus\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\lovelotus\\Desktop\\output.txt","w",stdout);
    int i,j,p,c,c1,t,k,win,xc,xc1;
    scanf("%d",&t);
    k=1;
    while(t--)
    {
        for(i=0;i<4;i++)
        {
            scanf("%s",s);
            for(j=0;j<4;j++)
            {
                switch(s[j])
                {
                    case 'X': a[i][j]=2; break;
                    case 'O': a[i][j]=3; break;
                    case 'T': a[i][j]=4; break;
                    case '.': a[i][j]=1; break;
                }
            }
        }
        p=0;win=0;
        for(i=0;i<4;i++)
        {
            c=c1=xc=xc1=0;
            for(j=0;j<4;j++)
            {
                if(a[i][j]==2) c++;
                else if(a[i][j]==3) c1++;
                else if(a[i][j]==4) {c++;c1++;}
                if(a[j][i]==2) xc++;
                else if(a[j][i]==3) xc1++;
                else if(a[j][i]==4) {xc++;xc1++;}
                if(a[i][j]!=1) p++;
            }
            if(c==4 || xc ==4) {win=1;break;}
            else if(c1==4 || xc1==4) {win=2;break;}
        }
            if(!win && p==16) win=3;
                c=c1=xc=xc1=0;
                for(i=0;i<4;i++)
                {
                    if(a[i][i]==2) c++;
                    else if(a[i][i]==3) c1++;
                    else if(a[i][i]==4) {c++;c1++;}
                    if(a[i][3-i]==2) xc++;
                    else if(a[i][3-i]==3) xc1++;
                    else if(a[i][3-i]==4) {xc++;xc1++;}
                }
                if(c==4 ||xc==4) win=1;
                else if(c1==4 || xc1==4) win=2;
        if(win==0) printf("Case #%d: Game has not completed\n",k++);
        else if(win==1) printf("Case #%d: X won\n",k++);
        else if(win==2) printf("Case #%d: O won\n",k++);
        else printf("Case #%d: Draw\n",k++);
    }
    return 0;
}
