#include <iostream>
#include <fstream>

#pragma optimize("O2",on)
using namespace std;

bool prime[1100];
int p[1100],rank[1100];

int fs(int x) {
    if (p[x]!=x)
        p[x]=fs(p[x]);
    return p[x];
}
void un(int a, int b) {
    if (rank[a]>rank[b])
        p[b]=a;
    else {
        if (rank[a]==rank[b])
            rank[b]++;
        p[a]=b;
    }
}

int main() {
#ifndef ONLINE_JUDGE
	ifstream cin("B-small.in");
    ofstream cout("B-small.out");
#endif
    memset(prime,true,sizeof prime);
    prime[0]=prime[1]=false;
    for (int i=2; i<=1000; i++)
        if (prime[i])
            for (int j=i*i; j<=1000; j+=i)
                prime[j]=false;
    int T; cin>>T;
    for (int o=1; o<=T; o++) {
        int A,B,P,res;
        cin>>A>>B>>P;
        for (int i=A; i<=B; i++) {
            rank[i]=0; p[i]=i;
        } res=B-A+1;
        for (int l=P; l<=B; l++)
            if (prime[l]) {
                for (int i=A; i<=B; i++)
                    for (int j=A; j<i; j++)
                        if (i%l==0 && j%l==0 && fs(i)!=fs(j)) {
                            res--;
                            un(fs(i),fs(j));
                        }
            }
        cout<<"Case #"<<o<<": "<<res<<endl;
    }
	return 0;
}