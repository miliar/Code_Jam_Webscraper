#include <cstdlib>
#include <iostream>

using namespace std;

int step[4][2] = {{0, 1}, {1, 1}, {1, 0}, {1, -1}};

int main(int argc, char *argv[])
{
    FILE* fin = fopen("A-large.in", "r");
    FILE* fout = fopen("A-large.out", "w");
    
    int t;
    int n, k;
    char arr[60][60];
    fscanf(fin, "%d", &t);
    for (int tt = 0; tt < t; tt++)
    {
        fscanf(fin, "%d%d", &n, &k);
        for (int i = 0; i < n; i++)
        {
            fscanf(fin, "%s", arr[i]);
        }
        /*
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                printf("%c", arr[i][j]);
            }
            printf("\n");
        }
        printf("\n");
        */
        for (int i = 0; i < n; i++) // line
        {
            int emp = n-1;
            for (int j = n-1; j >= 0; j--) //row
            {
                if (arr[i][j] != '.')
                {
                   arr[i][emp] = arr[i][j];
                   if (j != emp)
                      arr[i][j] = '.';
                   emp--;
                }
            }
        }
        /*
        printf("out herr\n");
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                printf("%c", arr[i][j]);
            }
            printf("\n");
        }
        printf("\n");
        */
        //
        bool blue = false;
        bool red = false;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                //printf("%d %d\n", i, j);
                if (arr[i][j] == '.')
                {
                   continue;
                }
                else
                {
                    for (int m = 0; m < 4; m++)
                    {
                        int cnt = 1;
                        int x = i+step[m][0];
                        int y = j+step[m][1];
                        //printf("m:%d %d\n", step[m][0], step[m][1]);
                        while (x < n && y < n && x >= 0 && y >= 0 && arr[x][y] == arr[i][j])
                        {
                              cnt++;
                              x += step[m][0];
                              y += step[m][1];
                              //printf("new %d %d\n", x, y);
                        }
                        if (cnt >= k)
                        {
                           if (arr[i][j] == 'B')
                           {
                              blue = true;
                           }
                           else
                           {
                               red = true;
                           }
                           break;
                        }
                    }
                }
            }
        }
        fprintf(fout, "Case #%d: ", tt+1);
        if (blue ==  true && red == true)
        {
                 fprintf(fout, "Both\n");
        }
        else if (blue == true && red != true)
        {
             fprintf(fout, "Blue\n");
        }
        else if (blue != true && red == true)
        {
             fprintf(fout, "Red\n");
        }
        else
        {
            fprintf(fout, "Neither\n");
        }
    } 
    return EXIT_SUCCESS;
}
