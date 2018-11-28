#include <cstdio>

int table[200][200];
int n;
int orig[200][200];
int sum;

int make(int nsize)
{
    int i;
    int j;
    for (i=0; i<nsize; i++)
    {
        for (j=0; j<nsize; j++)
        {
            int high = table[i][j];
            if (high > 0 && table[j][i] != -1 && table[j][i] != high)
            {
                return -1;
            }
            else if (table[j][i] != -1)
                high = table[i][j];
            if (high > 0 && table[nsize-1-i][nsize-1-j] != -1 && table[nsize-1-i][nsize-1-j] != high)
            {
                return -1;
            }
            else if (table[nsize-1-i][nsize-1-j] != -1)
                high = table[nsize-1-i][nsize-1-j];
            if (high > 0 && table[nsize-1-j][nsize-1-i] != -1 && table[nsize-1-j][nsize-1-i] != high)
            {
                return -1;
            }
            else if (table[nsize-1-j][nsize-1-i] != -1)
                high = table[nsize-1-j][nsize-1-i];                
        }
    }
    return nsize * nsize;
}

int main()
{
    int i, j;
    int a, b;
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        int best = 1000000000;
        int aux;
        scanf("%d", &n);
        sum = 0;
        for (i=0; i<n; i++)
        {
            for (j=0; j<=i; j++)
            {
                scanf("%d", &orig[i-j][j]);
            }
        }
        for (i=1; i<n; i++)
        {
            for (j=i; j<n; j++)
            {
                scanf("%d", &orig[i-j+n-1][j]);
            }
        }
        sum = n * n;
        // side of square
        int side;
        int px, py;
        bool ok = true;
        for (side=n; side < 3 * n && ok; side++)
        {
            px = 0;
            for (py = 0; py + n <= side && ok; py++)
            {
                for (a=0; a<side; a++)
                {
                    for (b=0; b<side; b++)
                    {
                        table[a][b] = -1;
                    }
                }
                for (a=0; a<n; a++)
                {
                    for (b=0; b<n; b++)
                    {
                        table[px + a][py + b] = orig[a][b];
                    }
                }
                aux = make(side);
                if (aux != -1)
                {
                    ok = false;
                    break;
                }
            }
            px = side - n;
            for (py = 0; py + n <= side && ok; py++)
            {
                for (a=0; a<side; a++)
                {
                    for (b=0; b<side; b++)
                    {
                        table[a][b] = -1;
                    }
                }
                for (a=0; a<n; a++)
                {
                    for (b=0; b<n; b++)
                    {
                        table[px + a][py + b] = orig[a][b];
                    }
                }
                aux = make(side);
                if (aux != -1)
                {
                    ok = false;
                    break;
                }
            }
            py = 0;
            for (px = 0; px + n <= side && ok; px++)
            {
                for (a=0; a<side; a++)
                {
                    for (b=0; b<side; b++)
                    {
                        table[a][b] = -1;
                    }
                }
                for (a=0; a<n; a++)
                {
                    for (b=0; b<n; b++)
                    {
                        table[px + a][py + b] = orig[a][b];
                    }
                }
                aux = make(side);
                if (aux != -1)
                {
                    ok = false;
                    break;
                }
            }
            py = side - n;
            for (px = 0; px + n <= side && ok; px++)
            {
                for (a=0; a<side; a++)
                {
                    for (b=0; b<side; b++)
                    {
                        table[a][b] = -1;
                    }
                }
                for (a=0; a<n; a++)
                {
                    for (b=0; b<n; b++)
                    {
                        table[px + a][py + b] = orig[a][b];
                    }
                }
                aux = make(side);
                if (aux != -1)
                {
                    ok = false;
                    break;
                }
            }
        }
        // center in square
/*        for (i=0; i<n; i++)
        {
            for (j=0; j<n; j++)
            {
                int nsize = i;
                if (nsize < j) nsize = j;
                if (nsize < n - 1 - i) nsize = n - 1 - i;
                if (nsize < n - 1 - j) nsize = n - 1 - j;
                
                int c1 = nsize - i;
                int c2 = nsize - j;
                nsize = 2 * nsize + 1;
                for (a=0; a<nsize; a++)
                {
                    for (b=0; b<nsize; b++)
                    {
                        table[a][b] = -1;
                    }
                }
                for (a=0; a<n; a++)
                {
                    for (b=0; b<n; b++)
                    {
                        table[c1 + a][c2 + b] = orig[a][b];
                    }
                }
                aux = make(nsize);
                if (aux != -1)
                {
                    if (aux < best) best = aux;
                }
            }
        }
        // center not in square
        for (i=0; i<=n; i++)
        {
            for (j=0; j<=n; j++)
            {
                int nsize = i;
                if (nsize < j) nsize = j;
                if (nsize < n - i) nsize = n - i;
                if (nsize < n - j) nsize = n - j;
                
                int c1 = nsize - i;
                int c2 = nsize - j;
                nsize = 2 * nsize;
                for (a=0; a<nsize; a++)
                {
                    for (b=0; b<nsize; b++)
                    {
                        table[a][b] = -1;
                    }
                }
                for (a=0; a<n; a++)
                {
                    for (b=0; b<n; b++)
                    {
                        table[c1 + a][c2 + b] = orig[a][b];
                    }
                }
                aux = make(nsize);
                if (aux != -1)
                {
                    if (aux < best) best = aux;
                }
            }
        }*/
        side--;
        printf("Case #%d: %d\n", t+1, side * side - n * n);
    }
    return 0;
}
