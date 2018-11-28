#include <cstdio>
#include <cstring>

using namespace std;

int T,n,k, C= 1;
char O[64][64], N[64][64];

inline void desce(int i, int j) {
    while (i+1 < n and N[i+1][j] == '.') {
        char ax = N[i+1][j];
        N[i+1][j] = N[i][j];
        N[i][j] = ax;
        i++;
    }
}

int main() {

    scanf("%d",&T);
        while (T--) {
        scanf("%d %d",&n, &k);
        for (int i=0;i<n;i++)
            scanf("%s",O[i]);

        // roda
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
                N[i][j] = O[n-1-j][i];


        // gravidade
        for (int j=0;j<n;j++) {
            for (int i=n-1;i>=0;i--)
                if (N[i][j] != '.')
                    desce(i,j);
        }
        // ve quem ganha
        bool r = false, b = false;
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++) {
                int contar = 0;
                //hor
                for (int x=0;x<k;x++)
                    if (0 <= x+j and x+j < n and N[i][x+j] == 'R')
                        contar++;
                    else
                        break;
                if (contar==k) {r = true; goto verb;}
                contar=0;
                // ver
                for (int x=0;x<k;x++)
                   if (0 <= x+i and x+i < n and N[x+i][j] == 'R')
                       contar++;
                   else
                       break;
                if (contar==k) {r = true; goto verb;}
                contar=0;
                // diago prin
                for (int x=0;x<k;x++)
                   if (0 <= x+i and x+i < n and 0 <= x+j and x+j < n and N[x+i][x+j] == 'R')
                       contar++;
                   else
                       break;
                if (contar==k) {r = true; goto verb;}

                // diago seg
                contar=0;
                for (int x=0;x<k;x++)
                   if (0 <= i+x and i+x < n and 0 <= j-x and j-x < n and N[i+x][j-x] == 'R')
                       contar++;
                   else
                       break;
                if (contar==k) {r = true; goto verb;}

verb:
                contar = 0;
                //hor
                for (int x=0;x<k;x++)
                    if (0 <= x+j and x+j < n and N[i][x+j] == 'B')
                        contar++;
                    else
                        break;
                if (contar==k) {b = true; goto verbf;}
                contar=0;
                // ver
                for (int x=0;x<k;x++)
                   if (0 <= x+i and x+i < n and N[x+i][j] == 'B')
                       contar++;
                   else
                       break;
                if (contar==k) {b = true; goto verbf;}
                contar=0;
                // diago prin
                for (int x=0;x<k;x++)
                   if (0 <= x+i and x+i < n and 0 <= x+j and x+j < n and N[x+i][x+j] == 'B')
                       contar++;
                   else
                       break;
                if (contar==k) {b = true; goto verbf;}
                contar=0;
                // diago seg
                for (int x=0;x<k;x++)
                   if (0 <= i+x and i+x < n and 0 <= j-x and j-x < n and N[i+x][j-x] == 'B')
                       contar++;
                   else
                       break;
                if (contar==k) {b = true; goto verbf;}

verbf:
                continue;

            }
        /*
        printf("k = %d\n",k);
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++)
                printf("%c",N[i][j]);
            printf("\n");
        }
        */

        // imrpime
        printf("Case #%d: ",C++);
        if (!b and !r)
            printf("Neither\n");
        else if (!b and r)
            printf("Red\n");
        else if (b and !r)
            printf("Blue\n");
        else
            printf("Both\n");
    }

    return 0;
}
