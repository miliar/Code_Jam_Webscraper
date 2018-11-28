#include <stdio.h>

int main ()
{
    freopen ("A-small-attempt0.in","r",stdin);
    freopen ("A-small-attempt0.out","w",stdout);
    int a,b,n,i,j,k,l,t;
    char c[4][5];
    scanf ("%d",&n);
    for (i=1;i<=n;i++)
        {
            k = 1;
            for (j=0;j<4;j++)
                scanf ("%s",c[j]);
            for (j=0;j<4;j++)
                for (l=0;l<4;l++)
                    {
                        if (c[j][l]=='T')
                            {
                                c[j][l] = 'X';
                                a = j;
                                b = l;
                            }
                        if (c[j][l]=='.')
                            k = 2;
                    }
            for (j=0;j<4;j++)
                if (c[j][0]=='X'&&c[j][0]==c[j][1]&&c[j][0]==c[j][2]&&c[j][0]==c[j][3])
                    k = 3;
            for (j=0;j<4;j++)
                if (c[0][j]=='X'&&c[0][j]==c[1][j]&&c[0][j]==c[2][j]&&c[0][j]==c[3][j])
                    k = 3;
            if (c[0][0]=='X'&&c[0][0]==c[1][1]&&c[0][0]==c[2][2]&&c[0][0]==c[3][3])
                k = 3;
            if (c[3][0]=='X'&&c[3][0]==c[2][1]&&c[3][0]==c[1][2]&&c[3][0]==c[0][3])
                k = 3;
            c[a][b] = 'O';
            for (j=0;j<4;j++)
                if (c[j][0]=='O'&&c[j][0]==c[j][1]&&c[j][0]==c[j][2]&&c[j][0]==c[j][3])
                    k = 4;
            for (j=0;j<4;j++)
                if (c[0][j]=='O'&&c[0][j]==c[1][j]&&c[0][j]==c[2][j]&&c[0][j]==c[3][j])
                    k = 4;
            if (c[0][0]=='O'&&c[0][0]==c[1][1]&&c[0][0]==c[2][2]&&c[0][0]==c[3][3])
                k = 4;
            if (c[3][0]=='O'&&c[3][0]==c[2][1]&&c[3][0]==c[1][2]&&c[3][0]==c[0][3])
                k = 4;
            if (k==1)
                printf ("Case #%d: Draw\n",i);
            else if (k==2)
                printf ("Case #%d: Game has not completed\n",i);
            else if (k==3)
                printf ("Case #%d: X won\n",i);
            else if (k==4)
                printf ("Case #%d: O won\n",i);
            //scanf (" ");
        }
    scanf (" ");
    return 0;
}
