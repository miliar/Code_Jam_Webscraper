#include <iostream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#define fori(N) for(int i=0; i<N; i++)
#define forj(N) for(int j=0; j<N; j++)

using namespace std;

int n,r,c;
char letter = 'a'-1;
int alt[100][100];
char bas[100][100];

char basin(int a, int b){
    char l = '*';
    int lowAlt = alt[a][b];
    int lowDir = 0;
    if(a-1 >-1 && alt[a-1][b] < lowAlt) {
        lowAlt = alt[a-1][b];
         lowDir = 1;
    }
    if(b-1 > -1 && alt[a][b-1] < lowAlt){
         lowAlt = alt[a][b-1]; 
         lowDir = 2;
    }
    if(b+1 < c && alt[a][b+1] < lowAlt){
         lowAlt = alt[a][b+1];
          lowDir = 3;
    }
    if(a+1 < r && alt[a+1][b] < lowAlt){
         lowAlt = alt[a+1][b];
          lowDir = 4;
    }
    
    if(lowDir == 0){
         if(bas[a][b] != '0') return bas[a][b];
         bas[a][b] = ++letter;
         l = letter;
    }
    else if(lowDir == 1){
        if(bas[a-1][b] != '0') return bas[a-1][b];
        bas[a][b] = basin(a-1, b);
        l = bas[a][b];
    }
    else if(lowDir == 2){
        if(bas[a][b-1] != '0') return bas[a][b-1];
        bas[a][b] = basin(a, b-1);
        l = bas[a][b];
    }
    else if(lowDir == 3){
        if(bas[a][b+1] != '0') return bas[a][b+1];
        bas[a][b] = basin(a, b+1);
        l = bas[a][b];
    }
    else if(lowDir == 4){
        if(bas[a+1][b] != '0') return bas[a+1][b];
        bas[a][b] = basin(a+1, b);
        l = bas[a][b];
    }
    return l;
}

int main(){
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    
    fin >> n;
    for(int Z=0; Z<n; Z++){
        letter = 'a' - 1;
        //input
        fin >> r >> c;
        fori(r){
            forj(c){
                fin >> alt[i][j];
                bas[i][j] = '0';
            }
        }
        //process
        
        fori(r){
            forj(c){
                if(bas[i][j] == '0') bas[i][j] = basin(i,j);
            }
        }
        
        fout << "Case #" << Z+1 << ": " << endl;
        fori(r){
            forj(c){
                fout << bas[i][j] << ' ';
            }
            fout << endl;
        }
    }   
    
    cin.get();
    return 0;   
}
