#include <iostream>
#include <vector>
#include <iomanip>


using namespace std;

typedef pair<long double,long double> PII;
typedef pair<long double,PII> PIII;

#define s first
#define b second.first
#define e second.second

int main(){
    int Tc;
    cin >> Tc;
    for(int tc=1;tc<=Tc;tc++){
            int R, C, D;
            cin >> R >> C >> D;
            vector<vector<int> > T(R, vector<int>(C));
            
            for(int i=0;i<R;i++) for(int j=0;j<C;j++){
                    char c;
                    cin >> c;
                    T[i][j] = c - '0' + D;
            }
            
            vector<vector<int> > sumi(R, vector<int> (C));
            for(int i=0;i<R;i++) for(int j=0;j<C;j++){
                    if(i == 0 && j == 0) sumi[i][j] = i * T[i][j];
                    else if(i == 0) sumi[i][j] = i*T[i][j] + sumi[i][j-1];
                    else if(j == 0) sumi[i][j] = i*T[i][j] + sumi[i-1][j];
                    else sumi[i][j] = i*T[i][j] + sumi[i-1][j] + sumi[i][j-1] - sumi[i-1][j-1];
            }
            
            vector<vector<int> > sumj(R, vector<int> (C));
            for(int i=0;i<R;i++) for(int j=0;j<C;j++){
                    if(i == 0 && j == 0) sumj[i][j] = j * T[i][j];
                    else if(i == 0) sumj[i][j] = j*T[i][j] + sumj[i][j-1];
                    else if(j == 0) sumj[i][j] = j*T[i][j] + sumj[i-1][j];
                    else sumj[i][j] = j*T[i][j] + sumj[i-1][j] + sumj[i][j-1] - sumj[i-1][j-1];
            }
            
            vector<vector<int> > sum(R, vector<int> (C));
            for(int i=0;i<R;i++){ for(int j=0;j<C;j++){
                    if(i == 0 && j == 0) sum[i][j] = T[i][j];
                    else if(i == 0) sum[i][j] = T[i][j] + sum[i][j-1];
                    else if(j == 0) sum[i][j] = T[i][j] + sum[i-1][j];
                    else sum[i][j] = T[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1];
//                    cerr << sum[i][j] << " ";
            } }
            
            
            
            int sol = 0;
            for(int i=0;i<R;i++) for(int j=0;j<C;j++) for(int k=3;k<=max(R, C); k++)
                    if(i+k <= R && j+k <= C){
                          double den = sum[i+k-1][j+k-1] + ((i==0||j==0)?0:sum[i-1][j-1]) - ((i==0)?0:sum[i-1][j+k-1]) - ((j==0)?0:sum[i+k-1][j-1]) - T[i][j] - T[i+k-1][j] - T[i][j+k-1] - T[i+k-1][j+k-1];
                          double numi = sumi[i+k-1][j+k-1] + ((i==0||j==0)?0:sumi[i-1][j-1]) - ((i==0)?0:sumi[i-1][j+k-1]) - ((j==0)?0:sumi[i+k-1][j-1]) - i*T[i][j] - (i+k-1)*T[i+k-1][j] - i*T[i][j+k-1] - (i+k-1)*T[i+k-1][j+k-1];
                          double numj = sumj[i+k-1][j+k-1] + ((i==0||j==0)?0:sumj[i-1][j-1]) - ((i==0)?0:sumj[i-1][j+k-1]) - ((j==0)?0:sumj[i+k-1][j-1]) - j*T[i][j] - j*T[i+k-1][j] - (j+k-1)*T[i][j+k-1] - (j+k-1)*T[i+k-1][j+k-1];
//                          if(i == 1 && j == 1) 
  //                             cerr << i << " " << j << " " << k << " - " << den << " " << numi << " " << numj << " " << numi / den << " " << numj / den << endl;
                          if(numi / den == (double(i) + double(k-1)/2.) && numj / den== ((double)j + double(k-1)/2)) sol = max(sol, k);
                    }
            if(sol != 0) cout << "Case #" << tc << ": " << sol << endl;
            else cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
                    
    }
}



/*
1
4 4 0
2111
2111
2111
3111
*/
