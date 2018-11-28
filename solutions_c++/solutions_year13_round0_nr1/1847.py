#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<iostream>
#include<time.h>
#include<sstream>
#include<string>
#include<algorithm>

#define nl printf("\n")

using namespace std;

void vyhral_nekdo(int os, int xs, bool & rozhodnuto, int i) {
    if (xs == 4) {
        printf("Case #%d: X won\n",i);
        rozhodnuto = true;
    }
    if (os == 4) {
        printf("Case #%d: O won\n",i);
        rozhodnuto = true;
    }
}


int main()
{

    int T;
    scanf("%d",&T);
    string line;
    getline(cin,line);

    for (int i = 1; i <= T; i++) {
        vector<string> pole;
        for (int j = 0; j < 4; j++) {
            getline(cin,line);
            pole.push_back(line);
        }
        getline(cin,line);

        bool rozhodnuto = false;
        int pocet_tecek;

        for (int smer = 0; smer < 2; smer++) {
            for (int yy = 0; yy < 4; yy++) {
                int os = 0;
                int xs = 0;
                for (int xx = 0; xx < 4; xx++) {
                    int x = smer ? xx : yy;
                    int y = smer ? yy : xx;

                    if (pole[y][x] == 'X' || pole[y][x] == 'T') {
                        xs++;
                    }
                    if (pole[y][x] == 'O' || pole[y][x] == 'T') {
                        os++;
                    }
                }
                vyhral_nekdo(os,xs,rozhodnuto,i);
                if (rozhodnuto) break;
            }

            if (rozhodnuto) break;
            int os = 0;
            int xs = 0;
            for (int y = 0; y < 4; y++) {
                int x = smer ? y : 3-y;
                if (pole[y][x] == 'X' || pole[y][x] == 'T') {
                    xs++;
                }
                if (pole[y][x] == 'O' || pole[y][x] == 'T') {
                    os++;
                }
            }
            vyhral_nekdo(os,xs,rozhodnuto,i);
            if (rozhodnuto) break;
        }


        if (!rozhodnuto) {
            int pocet_tecek = 0;
            for (auto s : pole) {
                pocet_tecek += count(s.begin(),s.end(),'.');
            }
            if (pocet_tecek == 0) {
                printf("Case #%d: Draw\n",i);
            } else {
                printf("Case #%d: Game has not completed\n",i);
            }
        }
    }
}
