//Bot Trust
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

int ntest, n ;
int pos['O'+1],w['O'+1] , v[101];
char u[101] ;
void init(){
    w['O'] =  w['B'] = 0;
    pos['O'] = pos['B'] = 1;

}
char calc(char x){
    return (x == 'O' ? 'B' : 'O');
}
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> ntest ;
    for(int i = 0; i<ntest; i++){
        cin >> n;init();
        for(int j = 0;j<n;j++) cin >> u[j] >> v[j];
        int j = 0;
        while (j<n){
            int now = w[calc(u[j])] - w[u[j]];
            int cur = abs(v[j] - pos[u[j]]) - now;
            if (cur < 0) w[u[j]] = w[calc(u[j])] + 1 ;
            else w[u[j]] = cur + w[calc(u[j])] + 1;
            //if (j == n-1) break;
            pos[u[j]]= v[j];
            while (u[j] == u[j+1] )  {
                j++;
                if (j==n) break;
                pos[u[j]] = v[j];
                w[u[j]] += abs(v[j]- v[j-1]) + 1;
            }
            //  cout << j << " " <<w['O'] << " " << w['B'] << endl;
            j++;
        }
        cout << "Case #"<< i+1 << ": "<< max(w['O'] , w['B']) << endl;
    }
    return 0;
}
