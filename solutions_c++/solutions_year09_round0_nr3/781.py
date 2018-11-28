#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
#define SL size()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define X first
#define Y second
#define LE length()
#define PB push_back

string wel = "welcome to code jam";

int calc[21][502];

int main(){
    int kases; cin>>kases;
    string s; getline(cin,s);
    for(int k=1;k<=kases;k++){
       getline(cin,s); calc[0][0] = 0;
       for(int j=0;j<(int)s.LE;j++){
          if(j) calc[0][j] = calc[0][j-1];
          if(wel[0] == s[j]) calc[0][j]++;
          //cout<<calc[0][j]<<" "; 
       }//cout<<endl;
       for(int i=1;i<(int)wel.LE;i++ ){
          calc[i][0] = 0;
          for(int j=0;j<(int)s.LE;j++){
             if(j)calc[i][j] = calc[i][j-1];
             if(wel[i] == s[j]){ calc[i][j]+=calc[i-1][j-1]; calc[i][j]%=10000;}
            // cout<<calc[i][j]<<" ";
          }//cout<<endl;
       }
       
       cout<<"Case #"<<k<<": ";
       if(calc[(int)wel.LE - 1][(int)s.LE -1] < 10 ) cout<<"000"<<calc[(int)wel.LE - 1][(int)s.LE -1]<<endl;
       else if(calc[(int)wel.LE - 1][(int)s.LE -1] < 100) cout<<"00"<<calc[(int)wel.LE - 1][(int)s.LE -1]<<endl;
       else if(calc[(int)wel.LE - 1][(int)s.LE -1] < 1000) cout<<"0"<<calc[(int)wel.LE - 1][(int)s.LE -1]<<endl;
       else cout<<calc[(int)wel.LE - 1][(int)s.LE -1]<<endl;
    }
}
