#include <fstream>
#include <iostream>
using namespace std;


static const int MOD = 100003;

long long INV[MOD+1];

void initINV() {
    for (long long i=1; i<MOD; i++) {
        if (i%10000==0) cerr<<i<<endl;
        for (long long j=i; j<MOD; j++)
            if (i*j % MOD == 1)
                INV[i]=j, INV[j]=i;
    }
}

void saveINV() {
    ofstream file("inv.txt");
    for (int i=1; i<MOD; i++) file<<INV[i]<<" ";
}

void loadINV() {
    ifstream file("inv.txt");
    for (int i=1; i<MOD; i++) file>>INV[i];
}


int NCK[512][512];
int nChooseK(int n, int k) {
    if (NCK[n][k]!=0) return NCK[n][k];
    long long result = 1;
    for (long long i=n; i>n-k; i--)
        result = result*i % MOD;
    for (long long i=k; i>1; i--)
        result = result*INV[i] % MOD;
//     cerr<<"nck: "<<result<<endl;
    return NCK[n][k] = (int)result;
}


int T[1000][1000];

int main() {
//     initINV();
//     saveINV();
    loadINV();
    cerr<<"--"<<endl;
    
//     T[2][1]=1;
    for (int a=2; a<=502; a++) {
        T[a][1]=1;
        cerr<<a<<endl;
        for (int b=a+1; b<=502; b++) {
            for (int x=0; x<=a; x++) {
                if (T[a][x+1]==0) continue;
                int y = a-x-2;
                T[b][a] = (T[b][a] + ((long long)T[a][x+1])*nChooseK(b-a-1, y)) % MOD;
//                 if (T[b][a]!=0) cerr<<"T["<<b<<"]["<<a<<"]="<<T[b][a]<<endl;
            }
        }
    }
    
    int C; cin>>C;
    for (int c=1; c<=C; c++) {
        int N; cin>>N;
        int result = 0;
        for (int x=0; x<=N; x++)
            result = (result+T[N][x]) % MOD;
        cout<<"Case #"<<c<<": "<<result<<endl;
    }
    
    return 0;
}
