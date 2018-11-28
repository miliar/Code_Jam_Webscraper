#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;

char b[10][10];

int dx[] = {1, 0, 1, 1};
int dy[] = {0, 1, 1, -1};

bool valid (int x , int y)
{
    return (x >= 0 && x < 4 && y >= 0 && y < 4);
}

int main ()
{
    FILE *in = fopen ("A.in","r");
    FILE *out = fopen ("A.out","w");

    int t;
    int k = 1;

    fscanf (in,"%d",&t);

    while( t -- )
    {
        string ans = "";
        fprintf (out,"Case #%d: ",k ++);

        bool flag = false;
        bool done = false;

        for (int i=0; i<4; i++)
            fscanf (in,"%s",b[i]);

        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                if (b[i][j] == 'T')
                    continue;
                if (b[i][j] == '.')
                {
                    flag = true;
                    continue;
                }

                for (int k=0; k<4; k++)
                {
                    if (i != j && k == 2) continue;
                    if (i+j != 3 && k == 3) continue;

                    int m;

                    for (m=1; m<=4; m++)
                    {
                        int nx1 = m*dx[k] + i;
                        int ny1 = m*dy[k] + j;
                        int nx2 = - m*dx[k] + i;
                        int ny2 = - m*dy[k] + j;

                        if (valid(nx1 , ny1) == true)
                            if (b[nx1][ny1] != 'T' && b[nx1][ny1] != b[i][j])
                                break;

                        if (valid(nx2 , ny2) == true)
                            if (b[nx2][ny2] != 'T' && b[nx2][ny2] != b[i][j])
                                break;
                    }

                    if (m == 5)
                    {
                        done = true;
                        break;
                    }
                }

                if (done == true)
                {
                    if (b[i][j] == 'X')
                        ans = "X won";
                    else
                        ans = "O won";
                    break;
                }
            }

            if (done == true)
                break;
        }

        if (ans == "")
        {
            if (flag == true)
                ans = "Game has not completed";
            else
                ans = "Draw";
        }

        fprintf (out,"%s\n",ans.c_str());

        fscanf (in," ");
    }
}
