#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

char m[101][101];
double wp[101], owp[101] ,oowp[101];
int n ;
double busca(int p1 , int p2){
    int g = 0 , t = 0;
    for(int i = 0 ; i < n ; i++)if(i != p1){
        if( m[p2][i] != '.' ){
            t++;
            if(m[p2][i] == '1') g++;   
        }
    }
    return (1.00*g)/t;
}

void doit(int test){
    printf("Case #%d:\n",test);
    char r;
    scanf("%d",&n);
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < n ; j++){
            cin >> r;
            m[i][j] = r;
            //cout<<m[i][j];
        }
        //cout<<endl;
    }
    for(int i = 0 ; i < n ; i++){
        int g = 0 , t = 0;
        for(int j = 0 ; j < n ; j++){
            if( m[i][j] == '1' || m[i][j] == '0' ){
                t++;
                if( m[i][j] == '1' ) g++;
            }
        }
        //cout<<g<<" "<<t<<endl;
        wp[i] = (g*1.0)/t;
    }
    for(int i = 0 ; i < n ; i++){
        double res = 0.00;
        int tt = 0;
        for(int j = 0 ; j < n ; j++){
            if( m[i][j] != '.' ){
                tt++;
                res += busca( i , j );
            }
        }
        owp[i] = res/tt;
    }
    for(int i = 0 ; i < n ; i++){
        double res = 0.00;
        int tt = 0;
        for(int j = 0 ; j < n ; j++){
            if( m[i][j] != '.' ){
                res += owp[j];
                tt++;
            }
        }
        oowp[i] = res/tt;
    }
    for(int i = 0 ; i < n ; i++) cout<< 0.25*wp[i] + 0.5*owp[i] + 0.25 * oowp[i] <<endl;
} 

int main(){
    int t;
    scanf("%d",&t);
    for(int i = 0 ; i < t ; i++) doit(i+1);
}
