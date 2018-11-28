#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

int main() {
     int t,n;
     long long int ret=0;
     ifstream fin("in.txt");
     ofstream fout("out.txt");
     fin>>t;
     for(int i=1;i<=t;i++) {
             vector<int> v1,v2;
             fin>>n;
             for(int j=0;j<n;j++) {
                     int x;
                     fin>>x;
                     v1.push_back(x);
             }
             for(int j=0;j<n;j++) {
                     int x;
                     fin>>x;
                     v2.push_back(x);
             }
             sort(v1.begin(),v1.end());
             sort(v2.rbegin(),v2.rend());
             ret=0;
             for(int j=0;j<n;j++) 
                     ret+=v1[j]*v2[j];
             fout<<"Case #"<<i<<": "<<ret<<"\n";
     }
     return 0;
}
     
