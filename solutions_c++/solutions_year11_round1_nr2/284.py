#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int n,m;
int part[10000];
int t[10000][1024];

int main()
{
    FILE * input = fopen("input.txt", "r");
    FILE * output = fopen("output", "w");
    int T;
    fscanf(input, "%d", &T);
    printf("%d\n", T);
    for(int cas = 1; cas <= T; cas++)
    {
        fscanf(input,"%d%d", &n, &m);
        printf("%d %d\n", n, m);
        char dico[n][10];
        int length[n];
        for(int i = 0; i < n; i++)
        {
            char c = 0;
            while(c < 'a' || c > 'z')
                fscanf(input, "%c", &c);
            int j = 0;
            while(c >= 'a' && c <= 'z')
            {
                dico[i][j] = c;
                fscanf(input, "%c", &c);
                j++;
            }
            length[i] = j;
        }
        int ordre[m][26];
        fprintf(output,"Case #%d: ", cas);
        for(int i = 0; i < m; i++)
        {
            char c = 0;
            while(c < 'a' || c > 'z')
                fscanf(input, "%c", &c);
            for(int j = 0; j < 26; j++)
            {
                ordre[i][j] = c;
                fscanf(input, "%c", &c);
            }
        }
        //ok pour la lecture
        for(int o = 0; o < m; o++) //pour chaque ordre
        {
            int points[n+1];
            for(int i = 0; i <= n; i++) points[i] = 0;
            int nbpart = 0;
            int ext[10];
            for(int i = 0; i < 10; i++) ext[i] = -1;
            for(int i = 0; i < n; i++)
            {
                if(ext[length[i]-1] >= 0) part[i] = ext[length[i]-1];
                else
                {
                    ext[length[i]-1] = nbpart;
                    part[i] = nbpart;
                    nbpart++;
                }
            }
            //printf("nb %d\n", nbpart);
            int lu = 0;
            while(nbpart < n)
            {
                /*printf("(%c) part : ", ordre[o][lu]);
                for(int i = 0; i < n; i++)
                    printf("%d ", part[i]);
                printf("\npoints : ");
                for(int i = 0; i < nbpart; i++)
                    printf("%d ", points[i]);
                printf("\n");*/
                bool split[n];
                for(int i = 0; i < n; i++) split[i] = false;
                for(int i = 0; i < n; i++)
                    for(int j = 0; j < 1024; j++)
                        t[i][j] = -1;
                char c = ordre[o][lu];
                for(int i = 0; i < n; i++)
                {
                    int hash = 0;
                    for(int j = 0; j < length[i]; j++)
                        if(dico[i][j] == c) hash += (1<<j);
                    t[part[i]][hash]++;
                }
                int nbpart2 = nbpart;
                for(int h = 1023; h >= 0; h--)
                {
                    for(int p = 0; p < nbpart; p++)
                    {
                        if(t[p][h] >= 0)
                        {
                            if(!split[p])
                            {
                                split[p] = true;
                                t[p][h] = p;
                            }
                            else
                            {
                                t[p][h] = nbpart2;
                                points[nbpart2] = points[p];
                                if(h == 0) points[nbpart2]++;
                                nbpart2++;
                            }
                        }
                    }
                }
                for(int i = 0; i < n; i++)
                {
                    int hash = 0;
                    for(int j = 0; j < length[i]; j++)
                        if(dico[i][j] == c) hash += (1<<j);
                    part[i] = t[part[i]][hash];
                }
                nbpart = nbpart2;
                lu++;
            }
                /*printf("part : ");
                for(int i = 0; i < n; i++)
                    printf("%d ", part[i]);
                printf("\npoints : ");
                for(int i = 0; i < nbpart; i++)
                    printf("%d ", points[i]);
                printf("\n");*/
            int maxp = -1;
            for(int i = 0; i < nbpart; i++)
                if(points[i] > maxp) maxp = points[i];
            int i = 0;
            while(points[part[i]] < maxp) i++;
            for(int j = 0; j < length[i]; j++)
                fprintf(output,"%c", dico[i][j]);
            if(o != m-1) fprintf(output," ");
        }
        fprintf(output,"\n");
    }
	return 0;
}






/*        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < 26; j++)
                printf("%c", ordre[i][j]);
            printf("\n");
        }
*/
