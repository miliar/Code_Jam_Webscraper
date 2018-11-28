#include <iostream>
#include <queue>
#include <fstream>

using namespace std;

ifstream fin("small.in");
ofstream fout("small.out");

int calc(int R, int k, int N){
    int sum=0;
    queue<int> Q;
    queue<int> QT;
    int g;
    while(N--){
        fin >> g;
        Q.push(g);
    }
    int cur;
    while(R--){
        cur = 0;
        while(!Q.empty() && Q.front()+cur <= k){
            QT.push(Q.front());
            cur += Q.front();
            Q.pop();
        }
        sum += cur;
        while(!QT.empty()){
            Q.push(QT.front());
            QT.pop();
        }
    }

    return sum;
}

int main(){
    int T, R, k, N;
    fin >> T;
    for(int i=1; i <= T; i++){
        fin >> R >> k >> N;
        fout << "Case #" << i << ": " <<calc(R, k, N) << endl;
    }
}