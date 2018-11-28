#include <stdio.h>
#include <stack>
#include <vector>
#include <map>
#include <queue>

int tab[105][105];
char wynik[105][105];
int T,H,W;

using namespace std;

typedef pair < int,int > Para;


bool czyPozOK(int h, int w) {
    return (0 <= h) && (h < H) && (0 <= w) && (w < W);

}

int zmi[4] = {-1,0,0,1};
int zmj[4] = {0,-1,1,0};

int main() {


    scanf("%d",&T);

    for (int testy = 1; testy <= T; ++testy) {

        scanf("%d %d",&H,&W);

//        map <  pair < int,int > , vector < pair < int, int > > > graf;
        map <  Para , vector < Para > > graf;

        
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j)
                scanf("%d",&tab[i][j]);

//        printf("H = %d, W = %d\n",H,W);

        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j) {
                bool byl = false;
                int naji , najj;
                int najmniej = tab[i][j];

                for (int k = 0; k < 4; ++k) {
                    int x = i + zmi[k];
                    int y = j + zmj[k];
                    if (czyPozOK(x,y)) {
                        if (tab[x][y] < najmniej) {
                            byl = true;
                            najmniej = tab[x][y];
                            naji = x; najj = y;
                        }
                    }

                }

                Para poz1, poz2;
                poz1.first = i;
                poz1.second = j;

                poz2.first = poz2.second = 0;

                if (byl) {
                    poz2.first = naji;
                    poz2.second = najj;

                    graf[poz1].push_back(poz2);
                    graf[poz2].push_back(poz1);

                } else {
                    graf[poz1].push_back(poz2);
                    graf[poz1].pop_back();

                }


            }

/*
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j) {
                Para p;
                p.first = i;
                p.second = j;
                printf("<%d,%d>:",p.first,p.second);
                for (vector<Para>::iterator iter = graf[p].begin(); iter != graf[p].end(); ++iter) {
                    printf("<%d,%d>",iter->first,iter->second);
                }
                printf("\n");


            }
*/
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j)
                wynik[i][j] = ' ';

        char znak = 'a';


        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j) {
                Para p;
                p.first = i;
                p.second = j;
                
                if (wynik[i][j] == ' ') {
                    
                    queue<Para> kolejka;
                    kolejka.push(p);

                    while (!kolejka.empty()) {
                        Para x = kolejka.front();
                        kolejka.pop();
                        wynik[x.first][x.second] = znak;
                        for (vector<Para>::iterator iter = graf[x].begin(); iter != graf[x].end(); ++iter) {
                            if (wynik[iter->first][iter->second] == ' ') {
                                wynik[iter->first][iter->second] = znak;
                                kolejka.push(*iter);

                            }
                         }
                    }

                    ++znak;
                }
       }

        printf("Case #%d:\n",testy);
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j)
                printf("%c ",wynik[i][j]);
            printf("\n");
        }

    }

    return 0;
}

