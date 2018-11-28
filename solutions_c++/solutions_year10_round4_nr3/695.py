#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
using namespace std;

#define	REP(i,n)	for(int (i) = 0; (i) < (n); (i)++)

bool matrix[2][250][250];
int R;
int X1,X2,Y1,Y2;


int main(){
    int T,cas;
    int i,j,k;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    cin>>T;
    for(cas = 1;cas <=T;++cas){
        memset(matrix,0,sizeof(matrix));
        cin>>R;
        for(i=0;i<R;++i){
            cin>>X1>>Y1>>X2>>Y2;
            for(j=X1;j<=X2;++j) for(k=Y1;k<=Y2;++k) matrix[0][j][k] = 1;
        }
        int current = 0;
        int next = 1;
        int steps =0;
        while(true){
            steps++;
            bool flag = false;
            for(i=1;i<250;++i) for(j=1;j<250;++j){
                if(matrix[current][i][j]){
                    if(matrix[current][i-1][j]||matrix[current][i][j-1]){
                        matrix[next][i][j] = true;
                        flag = true;
                    }
                    else{
                        matrix[next][i][j] = false;
                    }
                }
                else{
                    if(matrix[current][i-1][j]&&matrix[current][i][j-1]){
                        matrix[next][i][j] = true;
                        flag = true;
                    }
                    else{
                        matrix[next][i][j] = false;
                    }
                    
                }
            }
            if(!flag) break;
            current = 1-current;
            next = 1-next;
        }
        cout<<"Case #"<<cas<<": ";
        cout<<steps<<endl;
    }
    return 0;
}
