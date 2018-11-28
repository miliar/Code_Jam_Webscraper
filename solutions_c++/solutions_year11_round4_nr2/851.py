#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

int sumR[500][501],sumC[500][501];

int solve(int R, int C){
    //cout << "R = " << R << ", C = " << C << endl;
    for(int L = min(R,C);L >= 3;--L){
        //cout << "L = " << L << endl;
        for(int r = 0;r + L <= R;++r) for(int c = 0;c + L <= C;++c){
            long long numR = 0,denR = 0;
            
            for(int i = r;i < r + L;++i){
                if(i == r || i == r+L-1){
                    numR += (2 * (i - r) + 1) * (sumR[i][c + L - 1] - sumR[i][c + 1]);
                    denR += sumR[i][c + L - 1] - sumR[i][c + 1];
                }else{
                    numR += (2 * (i - r) + 1) * (sumR[i][c + L] - sumR[i][c]);
                    denR += sumR[i][c + L] - sumR[i][c];
                }
            }
            
            long long numC = 0,denC = 0;
            
            for(int i = c;i < c + L;++i){
                if(i == c || i == c+L-1){
                    numC += (2 * (i - c) + 1) * (sumC[i][r + L - 1] - sumC[i][r + 1]);
                    denC += sumC[i][r + L - 1] - sumC[i][r + 1];
                }else{
                    numC += (2 * (i - c) + 1) * (sumC[i][r + L] - sumC[i][r]);
                    denC += sumC[i][r + L] - sumC[i][r];
                }
            }
            
            //cout << L << " " << r << " " << c << " " << numR << " " << denR << " " << numC << " " << denC << endl;
            
            if(denR != 0 && numR % denR == 0 && numR / denR == L)
                if(denC != 0 && numC % denC == 0 && numC / denC == L)
                    return L;
        }
    }
    
    return -1;
}

int main(){
    int TC,R,C,D;
    char M[500][501];
    
    scanf("%d",&TC);
    
    for(int tc = 1;tc <= TC;++tc){
        scanf("%d %d %d",&R,&C,&D);
        //cout << R << " " << C << " " << D << endl;
        
        for(int i = 0;i < R;++i)
            scanf("%s",M[i]);
        
        /*for(int i = 0;i < R;++i)
            cout << M[i] << endl;
        cout << endl;*/
        //D = 0;
        
        for(int i = 0;i < R;++i){
            sumR[i][0] = 0;
            
            for(int j = 0;j < C;++j)
                sumR[i][j + 1] = sumR[i][j] + D + M[i][j] - '0';
        }
        
        for(int i = 0;i < C;++i){
            sumC[i][0] = 0;
            
            for(int j = 0;j < R;++j)
                sumC[i][j + 1] = sumC[i][j] + D + M[j][i] - '0';
        }
        
        /*for(int i = 0;i < R;++i){
            for(int j = 0;j <= C;++j) cout << sumR[i][j] << " ";
            cout << endl;
        }
        cout << endl;
        
        for(int i = 0;i < C;++i){
            for(int j = 0;j <= R;++j) cout << sumC[i][j] << " ";
            cout << endl;
        }
        cout << endl;*/
        
        int side = solve(R,C);
        
        printf("Case #%d: ",tc);
        
        if(side == -1) puts("IMPOSSIBLE");
        else printf("%d\n",side);
    }
    
    return 0;
}
