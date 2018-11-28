#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#define x first
#define y second
using namespace std;

int main(){
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    long long c,r,k,n;
    fin>>c;
    for (long long cases=1;cases<=c;cases++){
        cout<<cases<<endl;
        fin>>r>>k>>n;
        vector <long long> v(n);
        for (long long i=0;i<n;i++) fin>>v[i];
        vector <pair <long long,long long> > res(n); //Total i comptador
        for (long long i=0;i<n;i++){
            long long aux=v[i],aux2=1;
            for (long long j=i+1;j!=i;j++){
                if (j==n){
                    j=-1;
                    continue;
                }
                if (aux+v[j]<=k){
                    aux+=v[j];
                    aux2++;
                }
                else break;
            }
            res[i].x=aux;
            res[i].y=aux2;
        }
        long long pos=0,result=0;
        for (long long i=0;i<r;i++){
            result+=res[pos].x;
            pos+=res[pos].y;
            if (pos>n-1) pos-=n;
        }
        fout<<"Case #"<<cases<<": "<<result<<endl;
    }
}
