#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

#define pb push_back
int main() {
    int n,t,na,nb,ansA, ansB;
    ofstream fout("out.txt");
    ifstream fin("in.txt");
    fin>>n;
    for( int c=1;c<=n;c++) {
         vector <int> a_b,b_a,a,b;
         ansA=0;ansB=0;
         na=nb=t=0;
         char s[10];
         int h,m;
         fin>>t>>na>>nb;
         cout<<t<<"   "<<na<<"    "<<nb<<"\n";         
         for( int i=0;i<na;i++)  {
              fin>>s;
              sscanf(s,"%d:%d",&h,&m);
              a.pb(h*60+m);
              fin>>s;
              sscanf(s,"%d:%d",&h,&m);
              a_b.pb(h*60+m);
         }
         for( int i=0;i<nb;i++)  {
              fin>>s;
              sscanf(s,"%d:%d",&h,&m);
              b.pb(h*60+m);
              fin>>s;
              sscanf(s,"%d:%d",&h,&m);
              b_a.pb(h*60+m);
         }
         sort(a.begin(),a.end());
         sort(b.begin(),b.end());
         sort(a_b.begin(),a_b.end());
         sort(b_a.begin(),b_a.end());
         for( int i=0;i<a.size();i++) {
              bool found=false;
              for( int j=0;j<b_a.size();j++) { 
                   if( a[i]-b_a[j] >=t) {
                       found=true;
                       b_a.erase(b_a.begin()+j);
                       break;
                   }
              }
              if( !found)
                  ansA++;
         }
            
         for( int i=0;i<b.size();i++) {
              bool found=false;
              for( int j=0;j<a_b.size();j++) 
                   if( b[i]-a_b[j] >=t) {
                       found=true;
                       a_b.erase(a_b.begin()+j);
                       break;
                   }
              if( !found)
                  ansB++;
         }          
         fout<<"Case #"<<c<<": "<<ansA<<" "<<ansB<<"\n";   
    }                
    fout.close();
    return 0;
}
