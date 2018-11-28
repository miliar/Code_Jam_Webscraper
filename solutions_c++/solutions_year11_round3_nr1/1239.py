#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

char m[51][51];
char aux[51][51];
int r , c;
void iguala(){
    for(int i = 0 ; i < r ; ++i){
        for(int j = 0; j < c ; j++){
            aux[i][j] = m[i][j];
        }
    }
}

void doit(int test){
    printf("Case #%d:\n",test);
    char p;
    cin >> r >> c;
    for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < c ; j++){
            cin >> p;
            m[i][j] = p;
        }
    }
    iguala();
    for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < c ; j++){
            if( aux[i][j] == '#' ){
                if( i + 1 < r && j + 1 < c ){
                    if( aux[i+1][j] == '#' && aux[i][j+1] == '#' && aux[i+1][j+1] == '#' ){
                        aux[i][j] = '/';
                        aux[i][j+1] = '\\';
                        aux[i+1][j] = '\\';
                        aux[i+1][j+1] = '/';
                    }
                }
            }
        }
    }
    for(int i = 0 ; i < r ; i++) for(int j = 0 ; j < c ; j++) if( aux[i][j] == '#' ){  puts("Impossible"); return; }
    for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < c ; j++){
            cout<<aux[i][j];
        }
        cout<<endl;
    }
}

int main(){
    int g;
    cin >> g;
    for(int i = 1 ; i <= g ; i++) doit(i);
}
