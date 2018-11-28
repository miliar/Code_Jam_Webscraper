#include <iostream>
#include <cstring>
using namespace std;

char F[64][64];
int n,m;

void show(){
    int i,j;
    for (i=0; i<n+2; i++) cout << F[i] << endl;
}
void simpleshow(){
    int i,j;
    for (i=1; i<=n; i++) { for (j=1; j<=m; j++) cout << F[i][j]; cout << endl; }
}
int trace(){
    int f=0;
    int i,j;
    for (i=1; i<n; i++) for (j=1; j<m; j++){
        if ((F[i][j] == '#') && (F[i][j+1] == '#') && (F[i+1][j] == '#') && (F[i+1][j+1] == '#')){
            F[i][j] = '/';
            F[i+1][j] = '\\';
            F[i][j+1] = '\\';
            F[i+1][j+1] = '/';
            f=1;
        }
    }
    return f;
}
int check(){
    int i,j;
    for (i=1; i<=n; i++) for (j=1; j<=m; j++){
        if(F[i][j]=='#') return 1;
    }
    return 0;
}
void solve(int test){
    cout << "Case #" << test << ":" << endl;
    memset(F,'.',sizeof(F));
    int i,j;
    cin >> n >> m;
    F[0][m+2] = 0;
    F[n+1][m+2] = 0;
    for (i=1;i<=n; i++) {
        cin >> F[i];
        for(j=m;j>=1;j--) F[i][j] = F[i][j-1];
        F[i][0] = '.';
        F[i][m+2] = 0;

    }
    while (trace()==1);

    if (check()==1){
        cout << "Impossible" << endl;
    }else{
        simpleshow();
    }

}
int main()
{
    int T;
    cin >> T;
    for(int iT=1; iT<=T; iT++) solve(iT);
    return 0;
}
