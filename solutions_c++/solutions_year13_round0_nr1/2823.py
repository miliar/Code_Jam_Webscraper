#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<sstream>
#define REP(i,n) for(int i=0;i<n;++i)
#define FOR(i,j,k) for(int i=j;i<k;++i)
#define REPD(i,n) for(int i=n;i>-1;--i)
#define ALL(v) v.begin(),v.end()
#define ll long long
#define PB push_back
using namespace std;

bool Row(int wsk,vector<string> b,char c){
      string d = b[wsk];
      int cnt = 0;
      REP(i,d.size()) if(d[i]==c || d[i]=='T') ++cnt;
      return cnt == 4;
     }
     
     bool Column(int wsk,vector<string> b,char c){
      string d = "";
      REP(i,b.size()) d+=b[i][wsk];
      int cnt = 0;
      REP(i,d.size()) if(d[i]==c || d[i]=='T') ++cnt;
      return cnt == 4;
     }
     
          bool Diag1(vector<string> b,char c){
      string d = "";
      REP(i,b.size()) d+=b[i][i];
      int cnt = 0;
      REP(i,d.size()) if(d[i]==c || d[i]=='T') ++cnt;
      return cnt == 4;
     }
     
     bool Diag2(vector<string> b,char c){
      string d = "";
      REP(i,b.size()) d+=b[i][b.size()-1-i];
      int cnt = 0;
      REP(i,d.size()) if(d[i]==c || d[i]=='T') ++cnt;
      return cnt == 4;
     }

int main()
{
    int ts;cin>>ts;
    REP(tn,ts)
    {
        int n = 4;
        vector<string> b(n);
        REP(i,n) cin>>b[i];
        bool xWon = false, yWon = false;
        REP(i,n)
        {
           if(Row(i,b,'X')) xWon = true;
           else if(Row(i,b,'O')) yWon = true;
           else if(Column(i,b,'X')) xWon = true;
           else if(Column(i,b,'O')) yWon = true;
        }
        
        if(!xWon && !yWon){
                  if(Diag1(b,'X')) xWon = true; 
                  else if(Diag1(b,'O')) yWon=true;
                  else if(Diag2(b,'X')) xWon=true;
                  else if(Diag2(b,'O')) yWon=true;
                  }
        
        string ret = "Game has not completed";
        if(xWon) ret = "X won";
        else if(yWon) ret = "O won";
        else { 
                      bool isDraw = true;
                      REP(i,n) REP(j,n) if(b[i][j]=='.') {isDraw=false; break;}
                      if(isDraw) ret = "Draw";
             }

        cout<<"Case #"<<(tn+1)<<": "<<ret<<endl;
    }
}
