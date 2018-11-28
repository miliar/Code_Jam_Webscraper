#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> sieve(int n){
    vector<bool> isprime(max(3,n+1),1);
    isprime[0]=0;
    isprime[1]=0;
    for (int i=2;i*i<isprime.size();++i) if (isprime[i]){
        for (int j=2*i;j<isprime.size();j+=i) isprime[j]=0;
    }
    vector<int> primes;
    for (int i=0;i<isprime.size();++i) if (isprime[i]) primes.push_back(i);
    return primes;
}

int repr(vector<int> &padr, int x){
    if (padr[x]==x) return x;
    return padr[x]=repr(padr,padr[x]);
}

bool share(vector<int> &primes, vector<vector<bool> > &fact, int i, int j, int p){
    for (int k=0;k<primes.size();++k) if (primes[k]>=p){
        if (fact[i][k]==1 && fact[j][k]==1) return 1;
    }
    return 0;
}

int main(){
    int c;
    cin>>c;
    vector<int> primes=sieve(1050);
    for (int cc=0;cc<c;++cc){
        long long a,b,p;
        cin>>a>>b>>p;
        vector<vector<bool> > fact(b+1,vector<bool>(primes.size(),0));
        for (int i=0;i<fact.size();++i){
            for (int j=0;j<primes.size() && primes[j]<=i;++j){
                if (i%primes[j]==0) fact[i][j]=1;
            }
        }
        vector<int> padr(b+1);
        for (int i=0;i<padr.size();++i) padr[i]=i;
        for (int i=a;i<padr.size();++i){
            for (int j=i+1;j<padr.size();++j){
                if (repr(padr,i)!=repr(padr,j) && share(primes,fact,i,j,p)){
                    padr[repr(padr,j)]=repr(padr,i);
                }
            }
        }
        set<int> comp;
        for (int i=a;i<=b;++i) comp.insert(repr(padr,i));
        int ans=comp.size();
        cout<<"Case #"<<cc+1<<": "<<ans<<endl;
    }
}
