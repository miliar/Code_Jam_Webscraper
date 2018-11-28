#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

int M[100][100];
int Mdis[100][100];
char ans[100][100];
int di[4] = {-1, 0, 0, 1};
int dj[4] = {0, -1, 1, 0};

void get_sink(int i,int j,int H,int W, int & sink_i, int & sink_j)
{
    int k, tmpi, tmpj;
    sink_i = -1;
    sink_j = -1;
    for(k=0; k<4; ++k) {
        tmpi = i + di[k];
        tmpj = j + dj[k];
        if( tmpi >=0 && tmpi < H && tmpj >=0 && tmpj <W && M[i][j] > M[tmpi][tmpj]) {
            if (sink_i == -1) {
                sink_i = tmpi;
                sink_j = tmpj;
            }
            else {
                if (M[tmpi][tmpj] < M[sink_i][sink_j]) {
                    sink_i = tmpi;
                    sink_j = tmpj;
                }
            }
        }
    }
    return;
}

void process(int H, int W)
{
    char cc = 'a';
    int i,j,k, kk,sinki, sinkj, tmpi, tmpj, dis;
    for (i=0; i<H; ++i) {
        for (j=0; j<W; ++j) {
            // for each grid
            if (ans[i][j] != '0') continue; // skip it
            // 1) find sink

            sinki = i;
            sinkj = j;
            get_sink(sinki, sinkj, H, W, tmpi, tmpj );
            while( tmpi != -1 ) {
                sinki = tmpi;
                sinkj = tmpj;
                // printf(" == found slower i,j = %d,%d\n", sinki, sinkj);
                get_sink(sinki, sinkj, H, W, tmpi, tmpj );
            }

            if (ans[sinki][sinkj] != '0') {
                printf("Error: find sink error\n");
                return;
            }
            // printf(" == found sink i,j = %d,%d\n", sinki, sinkj);

            // 2) from sink to up
            queue<pair<int, int> > Q;
            Q.push( pair<int,int>( sinki, sinkj ) );
            ans[sinki][sinkj] = cc;
            while( !Q.empty() ) {
                pair<int,int> t = Q.front();
                // printf(" == pop i,j = %d,%d\n", t.first, t.second);
                Q.pop();
                for (k=0; k<4; ++k) {
                    tmpi = t.first + di[k];
                    tmpj = t.second + dj[k];
                    if( tmpi >=0 && tmpi < H && tmpj >=0 && tmpj <W && M[t.first][t.second] < M[tmpi][tmpj]) {
                        dis = M[tmpi][tmpj] - M[ t.first ][ t.second ]; 
                        if (Mdis[tmpi][tmpj] == -1 || dis > Mdis[tmpi][tmpj]) {
                            ans[tmpi][tmpj] = cc;
                            Mdis[tmpi][tmpj] = dis;
                            Q.push( pair<int,int>(tmpi, tmpj) );
                        }
                        else if ( dis == Mdis[tmpi][tmpj] ) {
                            // special process
                            // find its sink
                            int ti ,tj;
                            get_sink(tmpi, tmpj, H, W, ti, tj );
                            if (ti == t.first && tj == t.second && ans[tmpi][tmpj] != cc) {
                                ans[tmpi][tmpj] = cc;
                                Mdis[tmpi][tmpj] = dis;
                                Q.push( pair<int,int>(tmpi, tmpj) );
                            }

                        }
                    }
                }
            }
            cc += 1;
/*
printf("===\n");
    for (tmpi=0; tmpi<H; ++tmpi) {
        for (tmpj=0; tmpj<W; ++tmpj) {
            printf("%d", Mdis[tmpi][tmpj]);
            if (tmpj!=W-1) printf(" ");
        }
        printf("\n");
    }
printf("===\n");
*/ 
        }
    }

/* 
printf("===\n");
    for (tmpi=0; tmpi<H; ++tmpi) {
        for (tmpj=0; tmpj<W; ++tmpj) {
            printf("%d", Mdis[tmpi][tmpj]);
            if (tmpj!=W-1) printf(" ");
        }
        printf("\n");
    }
printf("===\n");
*/
    
    for (i=0; i<H; ++i) {
        for (j=0; j<W; ++j) {
            printf("%c", ans[i][j]);
            if (j!=W-1) printf(" ");
        }
        printf("\n");
    }
    return;
}

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);

    int T,H,W,Ti,i,j;

    scanf("%d", &T);
    for (Ti=0; Ti<T; ++Ti) {
        scanf("%d%d", &H, &W);
        for (i=0; i<H; ++i) {
            for (j=0; j<W; ++j) {
                scanf("%d", &(M[i][j]) );
                ans[i][j] = '0';
                Mdis[i][j] = -1;
            }
        }
        printf("Case #%d:\n", Ti+1);
        process(H, W);
    }

    return 0;
}

