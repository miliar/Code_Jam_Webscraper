#include <iostream>
#include <fstream>
#include <string>

#pragma optimize("O2",on)
using namespace std;

string s[12];
int res=0,n,m,mmax;
int f[12][1500];

void toms(int ms, int *a) {
    memset(a,0,sizeof(int)*10);
    int p=0;
    while (ms!=0) {
        a[p++]=ms%2;
        ms/=2;
    }
}

bool can(int ind, int ms) {
    int a[12];  toms(ms,a);
    for (int i=0; i<n; i++)
        if (a[i]==1 && ((i-1>=0 && a[i-1]==1) || s[ind][i]=='x'))
            return false;
    return true;
}

bool good(int m1, int m2) {
    int a[12],b[12];
    toms(m1,a); toms(m2,b);
    for (int i=0; i<n; i++)
        if (a[i]==1 && ((i+1<n && b[i+1]==1)||(i-1>=0 && b[i-1]==1)))
            return false;
    return true;
}
int od(int x ){
    int res=0;
    while (x!=0) {
        if (x%2==1)
            res++;
        x/=2;
    }
    return res;
}

int main() {
#ifndef ONLINE_JUDGE
	ifstream cin("C-small.in");
    ofstream cout("C-small.out");
#endif
    int T; cin>>T;
    for (int o=1; o<=T; o++) {
        cin>>m>>n; getline(cin,s[0]);
        for (int i=0; i<m; i++)
            getline(cin,s[i]);
        memset(f,0,sizeof f);
        mmax=1<<n;
        for (int i=0; i<mmax; i++)
            if (can(0,i)) f[1][i]=od(i);
        for (int j=2; j<=m; j++)
            for (int a=0; a<mmax; a++) if (can(j-2,a))
                for (int b=0; b<mmax; b++) if (can(j-1,b))
                    if (good(a,b)) 
                        f[j][b]=max(f[j][b],f[j-1][a]+od(b));
        int res=0;
        for (int i=0; i<mmax; i++)
            if (f[m][i]>res) res=f[m][i];
        cout<<"Case #"<<o<<": "<<res<<endl;
    }
	return 0;
}