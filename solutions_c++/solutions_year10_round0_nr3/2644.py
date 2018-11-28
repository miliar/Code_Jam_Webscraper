#include<iostream>
#include<fstream>

using namespace std;
ifstream fin("C.in");
ofstream fout("C.out");
long r,k,n,g[2000],t;
long long ans;
bool flag[2000];

int main() {
    fin >> t;
    for (int i=0;i<t;i++) {
        fin >> r >> k >> n;
        for (int j=0;j<n;j++) {
            fin >> g[j];
        }
        long counter=0;
        long capacity=k;
        ans=0;
        while (r>0) {
              memset(flag,false,sizeof(flag));
              while ((capacity>=g[counter]) && (!flag[counter])) {
                 capacity-=g[counter];
                 flag[counter]=true;
                 long long temp;
                 temp=g[counter];
                 ans=ans+temp;
                 counter=(counter+1)%n;
              }
              r--;
              capacity=k;
        }
        fout << "Case #" << i+1 << ": ";
        fout << ans << endl;
    }
    return 0;
}
