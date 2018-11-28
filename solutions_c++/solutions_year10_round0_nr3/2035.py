#include <fstream>
#include <iostream>
using namespace std;

#define MAXN 1005

long long T, R, k, N, size[MAXN];
long long val[MAXN], next[MAXN];

long long first[MAXN];
long long prePer, per;
unsigned long long prePerVal, perVal[MAXN];
long long cnt;

long long solve()
{
    memset(val, 0, sizeof(val));
    memset(next, 0, sizeof(next));
    memset(first, 0, sizeof(first));
    memset(perVal, 0, sizeof(perVal));

    long long ind, in;
    for(int i = 0; i < N; i++){
        in = 0;
        ind = i;
        while(in + size[ind] <= k && ((ind == i && !in) || (ind != i && in > 0))){
            in += size[ind];
            ind = (ind + 1) % N;
        }
        val[i] = in;
        next[i] = ind;
        //cout << val[i] << " " << next[i] << endl;
    }

    ind = 0;
    first[0] = 1;
    while(!first[next[ind]]){
        first[next[ind]] = first[ind] + 1;
        ind = next[ind];
    }

    /*for(int i = 0; i < N; i++){
        cout << first[i] << " ";
    }
    cout << endl;*/

    prePer = first[next[ind]] - 1;
    per = first[ind] - prePer;

    //cout << prePer << " ! " << per << endl;

    prePerVal = 0;
    ind = 0;
    while(R && first[ind] <= prePer){
        prePerVal += val[ind];
        ind = next[ind];
        R--;
    }
    //cout << R << " " << prePerVal << endl;

    if(!R){
        return prePerVal;
    }

    cnt = 1;
    perVal[0] = val[ind];
    ind = next[ind];
    while(first[ind] > prePer + 1){
        //cout << ind << " " << first[ind] << endl;
        perVal[cnt] = perVal[cnt - 1] + val[ind];
        ind = next[ind];
        cnt++;
    }

    //cout << cnt << endl;

    long long fullPerCnt = R / per;
    long long extra = (R % per ? perVal[R % per - 1] : 0);

    return prePerVal + perVal[cnt - 1] * fullPerCnt + extra;
}

int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    fin >> T;
    for(int i = 1; i <= T; i++){
        fin >> R >> k >> N;
        for(int j = 0; j < N; j++){
            fin >> size[j];
        }
        fout << "Case #" << i << ": " << solve() << endl;
    }
}
