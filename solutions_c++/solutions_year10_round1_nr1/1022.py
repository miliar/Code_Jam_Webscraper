#include <iostream>
#include <string>
#define VAZIO '.'
#define RED 'R'
#define BLUE 'B'

using namespace std;

void problemA(){
    int ncasos, caso = 0;
    cin >> ncasos;
    while (caso++ < ncasos){
        int n, k;
        bool Bwins = false, Rwins = false;
        cin >> n >> k;

        char tab[n][n];
        for (int col=n-1; col>=0; col--){
            for (int lin=0; lin<n; lin++){
                cin >> tab[lin][col];
            }
        }

        for (int col=0; col<n; col++){
            for (int lin=n-1; lin>0; lin--){
                if (tab[lin][col] == VAZIO){
                    int posvazio = lin, pospeca = lin-1;
                    while ((pospeca > 0) && (tab[pospeca][col] == VAZIO)){
                        pospeca--;
                    }

                    if (tab[pospeca][col] != VAZIO){
                        tab[posvazio][col] = tab[pospeca][col];
                        tab[pospeca][col] = VAZIO;
                    }else
                        break;
                }
            }
        }

        for (int lin=0; lin<n; lin++){
            int Rn = 0, Bn = 0;
            char ant = VAZIO;
            for (int col=0; col<n; col++){
                if (tab[lin][col] == VAZIO || tab[lin][col] != ant){
                    Rn = Bn = 0;
                }
                if (tab[lin][col] == BLUE) Bn++;
                if (tab[lin][col] == RED) Rn++;
                ant = tab[lin][col];
                Bwins = Bwins || Bn >= k;
                Rwins = Rwins || Rn >= k;
            }
        }

        for (int col=0; col<n; col++){
            int Rn = 0, Bn = 0;
            char ant = VAZIO;
            for (int lin=0; lin<n; lin++){
                if (tab[lin][col] == VAZIO || tab[lin][col] != ant){
                    Rn = Bn = 0;
                }
                if (tab[lin][col] == BLUE) Bn++;
                if (tab[lin][col] == RED) Rn++;
                ant = tab[lin][col];
                Bwins = Bwins || Bn >= k;
                Rwins = Rwins || Rn >= k;
            }
        }










        for (int i=0; i<n; i++){
            int Rn = 0, Bn = 0;
            char ant = VAZIO;
            int x=i, y=0;
            do{
                /*if (caso == 2){
                    cout << "[" << x << "," << y << "] = " << tab[x][y] << endl;
                    cout << "Rn = " << Rn << endl;
                }*/
                if (tab[x][y] == VAZIO || tab[x][y] != ant){
                    Rn = Bn = 0;
                }
                if (tab[x][y] == BLUE) Bn++;
                if (tab[x][y] == RED) Rn++;
                ant = tab[x][y];
                Bwins = Bwins || Bn >= k;
                Rwins = Rwins || Rn >= k;
            }while((++x < n) && (++y < n));
        }

        for (int i=0; i<n; i++){
            int Rn = 0, Bn = 0;
            char ant = VAZIO;
            int x=0, y=i;
            do{
                if (tab[x][y] == VAZIO || tab[x][y] != ant){
                    Rn = Bn = 0;
                }
                if (tab[x][y] == BLUE) Bn++;
                if (tab[x][y] == RED) Rn++;
                ant = tab[x][y];
                Bwins = Bwins || Bn >= k;
                Rwins = Rwins || Rn >= k;
            }while((++x < n) && (++y < n));
        }

        for (int i=n-1; i>=0; i--){
            int Rn = 0, Bn = 0;
            char ant = VAZIO;
            int x=i, y=0;
            do{
                if (tab[x][y] == VAZIO || tab[x][y] != ant){
                    Rn = Bn = 0;
                }
                if (tab[x][y] == BLUE) Bn++;
                if (tab[x][y] == RED) Rn++;
                ant = tab[x][y];
                Bwins = Bwins || Bn >= k;
                Rwins = Rwins || Rn >= k;
            }while((--x >= 0) && (++y < n));
        }

        for (int i=n-1; i>=0; i--){
            int Rn = 0, Bn = 0;
            char ant = VAZIO;
            int x=n-1, y=i;
            do{
                if (tab[x][y] == VAZIO || tab[x][y] != ant){
                    Rn = Bn = 0;
                }
                if (tab[x][y] == BLUE) Bn++;
                if (tab[x][y] == RED) Rn++;
                ant = tab[x][y];
                Bwins = Bwins || Bn >= k;
                Rwins = Rwins || Rn >= k;
            }while((--x >= 0) && (++y < n));
        }





        string winner = "Neither";
        if (Rwins && Bwins) winner = "Both";
        else if (Rwins) winner = "Red";
        else if (Bwins) winner = "Blue";


        cout << "Case #" << caso << ": " << winner << endl;
    }
}

int main(){
    problemA();
    return 0;
}
