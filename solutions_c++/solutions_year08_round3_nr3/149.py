#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

ifstream in("slimit1.in");
ofstream out("slimit1.out");

long long N, n, m, X, Y, Z;
long long A[500001];
long long slimits[500001];

void getval();

int main(){
    in >> N;
    for(int i=0; i<N; i++){
        out << "Case #" << i+1 << ": ";
        getval();
    }
}


void getval()
{
    in >> n >> m >> X >> Y >> Z;
    for(int i=0; i<m; i++)in >> A[i];
    for(int i=0; i<n; i++){
        slimits[i] = A[i%m];
        A[i%m] = (X * A[i%m] + Y * (i + 1))%Z;
    }        
    //use A for sequence numbering
    A[0]=1;
    long long total=0;
    if(n>=1)total=1;
    for(int i=1; i<n; i++){
        A[i]=1;
        for(int j=0; j<i; j++){
            if(slimits[j]<slimits[i]) {
                A[i] = (A[i]+A[j])%1000000007;                   
            }
        }
        total=(total+A[i])%1000000007;
    }
    out << total << endl;
}

