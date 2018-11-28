#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main() {
    ofstream fout("SMS.txt");
    int casos;
    cin>>casos;
    for(int cas=1;cas<=casos;cas++) {
            int p,k,n;
            cin>>p;
            cin>>k;
            cin>>n;
            vector<int> v(n);
            for(int i=0;i<n;i++) cin>>v[i];
            sort(v.begin(),v.end());
            reverse(v.begin(),v.end());
            int cont=0;
            for(int i=0;i<n;i++) {
                    cont+=(v[i]*(int((i/k)+1)));
            }
            if(cas<casos) fout<<"Case #"<<cas<<": "<<cont<<endl;
            else fout<<"Case #"<<cas<<": "<<cont;
    }
}
