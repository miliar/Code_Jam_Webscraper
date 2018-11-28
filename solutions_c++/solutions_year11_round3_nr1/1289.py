#include <iostream>
#include <fstream>
using namespace std;

#define INPUT "A-large.in"
#define OUTPUT "a.out"
#define MAX 55

int test,r,c;
char t[MAX][MAX];

bool inside(int i, int j){
    if (i<0 || i >= r) return false;
    if (j<0 || j >= c) return false;
    return true;
}

bool replace(){
    for (int i=0;i<r;i++)
    for (int j=0;j<c;j++)
    if (t[i][j] == '#'){
        t[i][j] = '/';
        if (inside(i,j+1) && t[i][j+1]=='#'){
            t[i][j+1] = '\\';
        } else {
            return false;
        }
        if (inside(i+1,j) && t[i+1][j] =='#'){
            t[i+1][j] = '\\';
        } else {
            return false;
        }
        if (inside(i+1,j+1) && t[i+1][j+1] == '#'){
            t[i+1][j+1] = '/';
        } else {
            return false;
        }
    }
    return true;
}

int main(){
    freopen(INPUT,"r",stdin);
    freopen(OUTPUT,"w",stdout);

    cin >> test;

    for (int task=1;task<=test;task++){
        cout << "Case #" <<task << ":" <<endl;
        cin >> r >> c;
        for (int i=0;i<r;i++)
        for (int j=0;j<c;j++)
        {
            cin >> t[i][j];
        }

        if (replace()){
            for (int i=0;i<r;i++){
                for (int j=0;j<c;j++){
                    cout << t[i][j];
                }
                cout << endl;
            }
        } else {
            cout << "Impossible"<<endl;
        }
    }

}
