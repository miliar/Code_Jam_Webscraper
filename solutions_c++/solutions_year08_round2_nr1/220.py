#include <cstdio>
#include <algorithm>

using namespace std;

long long Count[5][5], nrT;
bool mark[9][9][9], bun[19][19];

long long solve1(unsigned r1, unsigned r2){
     if (Count[r1][r2] > 2){
        long long N = Count[r1][r2];
        return N*(N-1)*(N-2)/6;
     }
     return 0;
}

long long solve2(int a, int b, int c, int d){
     pair<int, int> p1 = make_pair(a, b);
     pair<int, int> p2 = make_pair(c, d);
     if (p1 >= p2) return 0;
     long long N = Count[a][b];
     long long M = Count[c][d];
     long long rez = 0;
     if (N>1 && M>0 && bun[2*a+c][2*b+d])
        rez += (N*(N-1)/2) * M;
     if (M>1 && N>0 && bun[a+2*c][b+2*d]) 
        rez += (M*(M-1)/2) * N;
     return rez;
}

long long solve3(int a, int b, int c, int d, int e, int f){
     if (!bun[a+c+e][b+d+f]) return 0;
     int A = a*3+b;
     int B = c*3+d;
     int C = e*3+f;
     if (A>=B || A>=C || B>=C) return 0;
     long long N = Count[a][b];
     long long M = Count[c][d];
     return N * M * Count[e][f];
}


void solve(){
     long long n, A, B, C, D, M, x, y;
     scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d", &n, &A, &B, &C, &D, &x, &y, &M);
     memset(Count, 0, sizeof(Count));
     for (int i=0; i<n; i++){
         Count[x%3][y%3]++;
         x = (A*x + B)%M;
         y = (C*y + D)%M;
     }
     for (int i=0; i<19; i++)
         for (int j=0; j<19; j++)
             bun[i][j] = (i%3 == 0) && (j%3 == 0);
     long long rez = 0;
     for (int a=0; a<3; a++)
         for (int b=0; b<3; b++)
             rez += solve1(a, b);
//     printf("%I64d\n", rez);
     for (int a=0; a<3; a++)
         for (int b=0; b<3; b++)
             for (int c=0; c<3; c++)
                 for (int d=0; d<3; d++)
                     rez += solve2(a, b, c, d);
//     printf("%I64d\n", rez);                     
     for (int a=0; a<3; a++)
         for (int b=0; b<3; b++)
             for (int c=0; c<3; c++)
                 for (int d=0; d<3; d++)
                     for (int e=0; e<3; e++)
                         for (int f=0; f<3; f++)                     
                             rez += solve3(a, b, c, d, e, f);
     nrT++;
     printf("Case #%d: ", nrT);
     printf("%I64d\n", rez);
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w",stdout);
    int tst;
    scanf("%d", &tst);
    while (tst--)
          solve();
    return 0;
}
