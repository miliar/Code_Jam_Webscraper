#include<iostream>
#include<fstream>
#include<vector>
#include<sstream>

using namespace std;

int main() {
     int n,s,q,ret=0;
     ofstream fout("out");
     ifstream fin("in.in");
     char s0[102];
     fin.getline(s0,101,'\n');
     stringstream ss1(s0);     
     ss1>>n;
     for( int i=1;i<=n;i++) {
          ret=0;     
          vector<string> eng(0);
          string s1;
          fin.getline(s0,101,'\n');
          stringstream ss2(s0);
          ss2>>s;          
          for( int j=0;j<s;j++) {
               fin.getline(s0,101,'\n');
               s1=s0;
               eng.push_back(s1);               
          }
          fin.getline(s0,101,'\n');
          stringstream ss3(s0);
          ss3>>q;
          vector<string>temp =eng;
          for( int j=0;j<q;j++) {
               fin.getline(s0,101,'\n');
               s1=s0;
               vector<string>:: iterator it;
               it=find(temp.begin(),temp.end(),s1);
               if( it!=temp.end())
                   temp.erase(it);                 
               if( !temp.size()) {
                   ret++;
                   temp=eng;
                   it=find(temp.begin(),temp.end(),s1);
                   if( it!=temp.end())
                   temp.erase(it);                 
               }
          }
          fout<<"Case #"<<i<<": "<<ret<<"\n";
     }
     fout.close();
     return 0;
}
