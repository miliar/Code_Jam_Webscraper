#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
char s[6][6];
int main()
{
	int i,j,k,l,n,m,t,T,ii,c1,c2,sign;
	freopen("c://A-large.in","r",stdin);
	freopen("c://output.txt","w",stdout);
    scanf("%d",&T);
    for(ii=1;ii<=T;++ii)
    {
        for(i=0;i<4;++i)
        {
            scanf("%s",s[i]);
        }
        t=sign=0;
        for(i=0;i<4;++i)
        {
            c1=c2=0;
            for(j=0;j<4;++j)
            {
                if(s[i][j]=='O')
                {
                    c1++;
                }
                else if(s[i][j]=='X')
                {
                    c2++;
                }
                else if(s[i][j]=='T')
                {
                    c1++;c2++;
                }
                else
                {
                    t++;
                }
            }
            if(c1==4||c2==4)break;
            c1=c2=0;
            for(j=0;j<4;++j)
            {
                if(s[j][i]=='O')
                {
                    c1++;
                }
                else if(s[j][i]=='X')
                {
                    c2++;
                }
                else if(s[j][i]=='T')
                {
                    c1++;c2++;
                }
                else
                {
                    t++;
                }
            }
            if(c1==4||c2==4)break;
        }
        if(c1==4)sign=1;
        else if(c2==4)sign=2;
        else
        {
            c1=c2=0;
            for(i=0;i<4;++i)
            {
                if(s[i][i]=='O')
                {
                    c1++;
                }
                else if(s[i][i]=='X')
                {
                    c2++;
                }
                else if(s[i][i]=='T')
                {
                    c1++;c2++;
                }
                if(c1==4)sign=1;
                else if(c2==4)sign=2;

            }
            c1=c2=0;
            for(i=0;i<4;++i)
            {
                if(s[i][3-i]=='O')
                {
                    c1++;
                }
                else if(s[i][3-i]=='X')
                {
                    c2++;
                }
                else if(s[i][3-i]=='T')
                {
                    c1++;c2++;
                }
                if(c1==4)sign=1;
                else if(c2==4)sign=2;

            }
        }
        if(sign==0&&t==0)printf("Case #%d: Draw",ii);
        else if(sign==0&&t!=0)printf("Case #%d: Game has not completed",ii);
        else if(sign==1)printf("Case #%d: O won",ii);
        else if(sign==2)printf("Case #%d: X won",ii);
        if(ii!=T)printf("\n");

    }


    return 0;
}
