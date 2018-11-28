#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
#define For(i,a,b)  for(int i=a; i<=b; i++)
#define Ford(i,a,b) for(int i=a; i>=b; i--)
#define fillchar(a) memset(a, 0, sizeof(a))
#define maxn 105
#define maxq 1005

string ten[maxn], hoi[maxq];
int n, q, f[maxq], e[maxn], next[maxq][maxn];

void ktao(){
    fillchar(e);
    fillchar(f);
    fillchar(next);
    
    cin>>n;
    cin.ignore();
    For(i,1,n) getline(cin, ten[i]);
    cin>>q;
    cin.ignore();
    For(i,1,q) getline(cin, hoi[i]);
}

int xuly(){
    For(j,1,n) {e[j]=q+1;next[q+1][j]=q+1;}
    //initiative
    Ford(i,q,1){
        For(j,1,n){
            if (hoi[i]==ten[j]) {next[i][j]=i;e[j]=i;}
                else next[i][j]=next[i+1][j];
        }
    }
    //dynamic programming
    Ford(i,q,1){
        f[i]=maxq;        
        For(j,1,n){
            if (hoi[i]!=ten[j]) f[i]=min(f[i], f[next[i][j]]+1);
        }    
    }
    int kq=maxq;
    For(i,1,n) kq=min(kq, f[e[i]]);
    return kq;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out","w", stdout);
    int ntest;
    cin>>ntest;
    For(test,1,ntest){
        ktao();
        cout<<"Case #"<<test<<": "<<xuly()<<endl;
    }    
    return 0;
}
