#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
using namespace std;
#define For(i,a,b)  for(int i=a; i<=b; i++)
#define Ford(i,a,b) for(int i=a; i>=b; i--)
#define fillchar(a) memset(a, 0, sizeof(a))

int kq, k, used[10], a[10];
string st, st2;
void ktra(){
    st2="";
    int dem=1;
    For(i,0,st.size()/k-1)
        For(j,1,k) st2+=st[i*k+a[j]-1];
    For(i,1,st2.size()-1)
        if (st2[i]!=st2[i-1]) dem++;
    kq=min(kq,dem);
}

void duyet(int i){
    if (i>k){
        ktra();
        return;
    }
    For(j,1,k) if (!used[j]){
        a[i]=j;
        used[j]=1;
        duyet(i+1);
        used[j]=0;
    }
}

int main(){
    freopen("c.in", "r", stdin);
    freopen("c.out","w", stdout);
    int ntest;
    cin>>ntest;
    For(test,1,ntest){
        cin>>k;
        cin>>st;
        fillchar(used);
        kq=10000;
        duyet(1);
        cout<<"Case #"<<test<<": "<<kq<<endl;
    }
    return 0;
}
