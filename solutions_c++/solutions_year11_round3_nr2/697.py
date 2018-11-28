#include <iostream>
#include <cstdio>

using namespace std;

typedef unsigned long long int u64;

u64 C, N, td, L;

const u64 maxN = 100001;
int dist[maxN];

u64 solve(int a, int b){
    u64 actime = 0;
    u64 pos = 0;
    u64 nextdist;
//    a = 2;
//    b = 0;
//    cout << a << " " << b <<endl;
    while(pos < N){
        nextdist  = dist[pos%C];
//        cout << "C " << C << endl;
//        cout << "pos " << pos << endl;
//        cout << "posindex " << (pos%C) << endl;
//        cout << "dist " << nextdist << endl;
//        cout << "actime " << actime << endl;
        u64 nexttime = actime + nextdist * 2;
        if((a == pos or b == pos) and nexttime >= td){ // does finish in time
            if(td <= actime){
                actime += nextdist;
            }else{
//                cout << "HALF" << endl;
                // find out how much to double
                // acttime, td, nexttime
                int finishdiff = td - actime;
                int rest = nextdist - finishdiff/2;
//                cout << rest << " rest" << endl;
//                cout << finishdiff << " fd" << endl;
//                cout << (nextdist*2) << " = " << (finishdiff*1) << " + " << (nextdist*2-finishdiff) << endl;
                actime += finishdiff + rest;
            }
//            cout << finishdiff << " fd" << endl;
        }else{ // does not finish in time
//            cout << "not fin" << endl;
            actime = nexttime;
        }
        pos++;
    }
    
    // does finish in time
//    cout << a << " " << b << " " << actime << endl;
    return actime;
}


int main(){
    u64 T;
    cin >> T;
    for(u64 t = 1; t <= T; t++){
        cin >> L >> td >> N >> C;
        for(u64 i = 0; i < C; i++){
            u64 tmp;
            cin >> tmp;
            dist[i] = tmp;
//            cout << dist[i] << endl;
        }
        u64 sol = 1000000000000000000;
        // Choose one or two boosters and find out the value
        if(L == 0){
//            cout << "L " << L << endl;
            sol = solve(-1, -1);
        } else if(L == 1){
            for(u64 i = 0; i < N; i++){
                u64 res = solve(i, -1);
                if(res < sol){
                    sol = res;
                }
            }
        }else if(L == 2){
            for(u64 i = 0; i < N - 1; i++){
                for(u64 j = i + 1; j < N; j++){
                    u64 res = solve(i, j);
                    if(res < sol){
                        sol = res;
                    }
//                    break;
                }
//                break;
            }
        }
        cout << "Case #" << t << ": " << sol << endl;
//        break;
    }
}
