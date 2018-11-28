#include <cstdio>
#include <cstring>

using namespace std;

char temp[110][110];
int played_games[110],n;
double mem[3][100];
int c[3][100];

double wp( int a ){
    int p = 0;
    if( c[0][a] != -1 ) return mem[0][a];
        
    for(int i = 0;i < n; ++i){
        if( temp[a][i] == '.' ) continue;
        if( temp[a][i] == '1' ) ++p;
    }
    c[0][a] = 1;
    return mem[0][a] = (double)p / played_games[a];
}

double owp( int a ){
    double sm = 0;
    if( c[1][a] != -1 ) return mem[1][a];
    
    for(int i = 0; i < n; ++i){
        if( temp[a][i] == '.' ) continue;
        if( temp[a][i] == '1' ){
            sm += wp(i) * played_games[i] / (played_games[i] - 1);
        }else{
            sm += (wp(i) * played_games[i] - 1) / (played_games[i] - 1);
        }
    }
    c[1][a] = 1;
        return mem[1][a] = sm / played_games[a];
}

double oowp( int a ){
    double sm = 0;
    if( c[2][a] != -1 ) return mem[2][a];
    for(int i = 0; i < n; ++i){
        if( temp[a][i] == '.' ) continue;
        sm += owp( i );
    }
    c[2][a] = 1;
    return mem[2][a] = sm / played_games[a];
}


int main(){
    int test;
    scanf("%d",&test);
    for(int i = 0; i < test ; ++i){
        memset( mem, -1, sizeof(mem));
        memset( c, -1, sizeof(c));
        scanf("%d",&n);
        printf("Case #%d:\n", i+1);
        for(int j = 0; j < n; ++j)
            scanf("%s",temp[j]);
        for(int j = 0; j < n; ++j){
            played_games[j] = 0;
            for(int z = 0; z < n; ++z){
                if( temp[j][z] == '.' ) continue;
                ++played_games[j];
            }
        }
        for(int j = 0; j < n; ++j){
            double a = wp(j);
            double b = owp(j);
            double c = oowp(j);
            
            printf("%.10lf\n",0.25 * a + 0.5 * b + 0.25 * c );
        }
    }
    return 0;
}
