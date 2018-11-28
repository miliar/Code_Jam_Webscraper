#include<stdio.h>
#include<stdlib.h>

char inp[5][5];

int abs(int a){return (a<0)?-a:a;}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int z,t,i,j,diag,diag2,calx[5],caly[5],ist,iswon,posx,posy,ispnt;
    scanf ("%d",&z);
    for (t=1;t<=z;++t)
    {
        ist = 0;
        ispnt = 0;
        iswon = 0;
        diag = diag2 = 0;
        posx = posy=0;
        for (i=0;i<4;i++)
        {
            calx[i] = 0;
            caly[i] = 0;
        }
        for (i=0;i<4;i++)
        {
            scanf ("%s",inp[i]);
        }
        printf ("Case #%d: ",t);
        for (i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
            {
                if (inp[i][j] == 'O')
                {
                    calx[i]+=1;caly[j]+=1;
                }
                else if (inp[i][j] == 'X')
                {
                    calx[i]-=1;caly[j]-=1;
                }
                else if (inp[i][j] == 'T')
                {
                    ist = 1;
                    posx = i;
                    posy = j;
                }
                else ispnt = 1;
            }
        }
        for (i=0;i<4;i++)
        {
            if (abs(calx[i])==4||(ist && posx == i && abs(calx[i])==3))
            {
                if (calx[i] < 0)printf ("X won\n");
                else printf ("O won\n");
                iswon = 1;
                break;
            }
            if (abs(caly[i])==4||(ist && posy == i && abs(caly[i])==3))
            {
                if (caly[i] < 0)printf ("X won\n");
                else printf ("O won\n");
                iswon = 1;
                break;
            }
            if (inp[i][i] == 'X')diag-=1;
            else if (inp[i][i] == 'O')diag+= 1;
            if (inp[i][3-i] == 'X')diag2-=1;
            else if (inp[i][3-i] == 'O')diag2+=1;
        }
        if (!iswon && (abs(diag)==4 || (ist && posy == posx && abs(diag)==3)))
        {
            //printf ("%d\n",diag);
            if (diag < 0)printf ("X won\n");
            else printf ("O won\n");
            iswon =1;
        }
        if (!iswon && (abs(diag2)==4 || (ist && posy == 3-posx && abs(diag2) == 3)))
        {
            //printf ("%d\n",diag2);
            if (diag2 < 0)printf ("X won\n");
            else printf ("O won\n");
            iswon =1;
        }
        if (iswon)continue;
        else if (ispnt)printf ("Game has not completed\n");
        else printf ("Draw\n");
    }
    return 0;
}
