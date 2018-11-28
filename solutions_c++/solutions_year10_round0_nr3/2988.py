#include<iostream>
using namespace std;

int main()
{
    freopen("inC.txt","r",stdin);
    freopen("outC.txt","w",stdout);
    int Case;
    cin >> Case;
    for ( int t = 1 ; t <= Case ; t++){
        long long R,k,N;
        cin >> R >> k >> N;
        long long cList[1001];
        for ( int i = 0 ; i < N ; i++){
            cin >> cList[i];
        }
        int pos = 0;

        long long income = 0;
        for ( int i = 0 ; i < R; i++){
            long long load = 0;
            //cout << "-->";
            int start = pos;
            while(cList[pos] + load <= k){
                load+=cList[pos];
               // cout << cList[pos] << ' ';
                pos = (pos+1)%N;
                if(pos == start)break;
            }
            //cout << endl;
            income+=load;
        }
        printf("Case #%d: ",t);
        cout << income << endl;
    }
    return 0;
}
