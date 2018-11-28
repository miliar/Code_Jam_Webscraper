#include<stdio.h>
int main()
{
    int t,i,j,k,tr,tc,a[5][5],w,d;
    char c;
    scanf("%d",&t);
    for(k=1;k<=t;++k)
    {
        c=getchar();
        for(i=0;i<4;i++)
            a[4][i]=0;
        tr=w=-1;
        tc=-2;d=0;
        for(i=0;i<4;++i)
        {
            for(j=a[i][4]=0;j<4;j++)
            {
                scanf("%c",&c);
                if(c=='O')
                     a[i][j]=1;
                else if(c=='X')
                     a[i][j]=-1;
                else if(c=='.')
                {
                     a[i][j]=0;
                     d=1;
                }
                else
                {
                     a[i][j]=0;
                     tr=i;
                     tc=j;
                }
                a[i][4]+=a[i][j];
                a[4][j]+=a[i][j];
            }
            c=getchar();
        }
        for(i=0;i<4;i++)
        {
            if(a[i][4]==4 || a[i][4]==3 && tr==i || a[4][i]==4 || a[4][i]==3 && tc==j )
            {
                w=0;
                break;
            }
            else if(a[i][4]==-4 || a[i][4]==-3 && tr==i || a[4][i]==-4 || a[4][i]==-3 && tc==j)
            {
                 w=1;
                 break;
            }
        }
        if(w==-1){
        if( a[0][0]+a[1][1]+a[2][2]+a[3][3] == 4 || a[0][0]+a[1][1]+a[2][2]+a[3][3] == 3 && tr==tc )
            w=0;
        else if(a[0][0]+a[1][1]+a[2][2]+a[3][3] == -4 || a[0][0]+a[1][1]+a[2][2]+a[3][3] == -3 && tr==tc )
            w=1;
        else if( a[0][3]+a[1][2]+a[2][1]+a[3][0] == 4 || a[0][3]+a[1][2]+a[2][1]+a[3][0] == 3 && tr+tc==3 )
             w=0;
        else if( a[0][3]+a[1][2]+a[2][1]+a[3][0] == -4 || a[0][3]+a[1][2]+a[2][1]+a[3][0] == -3 && tr+tc==3 )
             w=1;}
        
        if(w==0)
            printf("Case #%d: O won\n",k);
        else if(w==1)
            printf("Case #%d: X won\n",k);
        else if(d==1)
            printf("Case #%d: Game has not completed\n",k);
        else
            printf("Case #%d: Draw\n",k);
    }
    return 0;
}
