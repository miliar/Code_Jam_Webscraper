#include <iostream>
#include <fstream>
#include <string>
#include <map>

#pragma optimize("O2",on)
using namespace std;
map<string,int> A;
string Q[1100];
int f[1100];
bool ex[1100];

int main() {
	ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    int n; cin>>n;
    for (int o=1; o<=n; o++) {
        int s,q; string a;
        cin>>s; getline(cin,a);
        A.clear();
        for (int i=0; i<s; i++) {
            getline(cin,a);
            A[a]=i;
        }
        cin>>q; getline(cin,a);
        for (int i=1; i<=q; i++) 
            getline(cin,Q[i]);
        const int inf=1000000;
        for (int i=1; i<=q; i++)
            f[i]=inf;  f[0]=0;
        for (int i=1; i<=q; i++) {
            memset(ex,false,sizeof ex);
            int part=s,pos=i,l;
            map<string,int>::iterator it;
            while (pos>0) {
                it=A.find(Q[pos]);
                if (it!=A.end()) {
                    l=it->second;
                    if (!ex[l]) {
                        ex[l]=true;
                        part--;
                    }
                }
                if (part>0 && f[i]>f[pos-1]+1)
                    f[i]=f[pos-1]+1;
                pos--;
            }
        }
        cout<<"Case #"<<o<<": "<<max(f[q]-1,0)<<endl;
    }
	return 0;
}
