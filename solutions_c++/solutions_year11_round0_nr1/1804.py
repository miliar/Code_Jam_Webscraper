#include <iostream>

using namespace std;

int dist(int a, int b){
    return (a > b)? (a-b) : (b-a);
}

int nearest(int pos, int target, int mdist){
    if( dist(pos, target) <= mdist ){
        return target;
    }
    else{
        return (pos < target) ? pos + mdist : pos - mdist;
    }
}

int main(){
    int T;
    cin >> T;
    for( int i = 0; i < T; i++ ){
        int N;
        cin >> N;
        int curPos[2] = {1, 1};
        int target[100];
        int targetType[100];
        int cursor[2] = {N, N};
        int totaldist = 0;
        for ( int j = 0; j < N; j++) {
            int robotType;
            char robot;
            int pos;
            cin >> robot;
            cin >> pos;
            if (robot == 'O'){
                robotType = 0;
            }
            else
                robotType = 1;
            if(cursor[robotType] == N)
                cursor[robotType] = j;
            target[j] = pos;
            targetType[j] = robotType;
        }


        for ( int j = 0; j < N; j++) {
            int current = targetType[j];
            int other = targetType[j] ^ 1;
            int dista = 0;
            dista = dist(target[j], curPos[ current ]) + 1;
            for ( int k = j+1; k < N; k++){
                if( targetType[k] == current ){
                    cursor[current] = k;
                    break;
                }
            }
            curPos[current] = target[j];
            if( cursor[other] < N)
                curPos[other] = nearest(curPos[other], target[cursor[other]], dista);
            totaldist += dista;
            //cout << totaldist << " " << curPos[other] << " " << cursor[current] << endl;

        }
            

        cout << "Case #" << i+1 << ": " << totaldist << endl;
    }
    return 0;
}
