#include <iostream>
using namespace std;
int a[2][105][105];
int main(){
    int r,c,o;
    cin >> c;
    o = c;
    while (c--){
        cin >> r;
        cout << "Case #"<<o-c <<": ";
        int ans = 0;
        memset(a,0,sizeof a);
        for (int i = 0; i < r; ++i){
            int x1,x2,y1,y2;
            cin >> x1 >> y1 >> x2 >> y2;
            if (x1>x2){
                int k = x2;
                x2 = x1;
                x1 = k;
            }
            if (y1>y2){
                int k = y2;
                y2 = y1;
                y1 = k;
            }
            for (int j = x1; j<=x2; ++j)
                for (int k = y1; k<=y2; ++k){
                    a[0][j][k] = 1;
                }
        }
        bool somebac = false;
        do{
            somebac = false;
            for (int i = 1; i <= 100; ++i)
                for (int j = 1; j <= 100; ++j)
                    a[(ans+1)%2][i][j] = 0;
            for (int i = 2; i <= 100; ++i)
                for (int j = 2; j <= 100; ++j)
                    if (a[(ans%2)][i-1][j] && a[(ans%2)][i][j-1] && a[(ans)%2][i][j]==0){
                        a[(ans+1)%2][i][j] = 1;
                    //    cout << ans <<" "<< i <<" " << j <<endl;
                        somebac = true;
                    }else if (a[(ans)%2][i-1][j]==0 && a[ans%2][i][j-1]==0 && a[(ans)%2][i][j]==1){
                        a[(ans+1)%2][i][j] = 0;
                        
                    }else{ a[(ans+1)%2][i][j] = a[(ans)%2][i][j];
                         if (a[(ans+1)%2][i][j]==1){
                             somebac = true;
                      //       cout << ans <<" " << i <<" "<< j <<endl;
                         }
                    }
            if (somebac)
                ++ans;            
        } while (somebac);
        cout << ans+1 <<endl;
    }    
}
