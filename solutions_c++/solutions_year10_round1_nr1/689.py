#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<string>
#include<sstream>
#include<set>
#include<cmath>
#define REP(i,n) for(int i=0;i<n;++i)
#define REPD(i,n) for(int i=n;i>-1;--i)
#define FOR(i,j,k) for(int i=j;i<k;++i)
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define PRINT(v) {REP(i,v.size()) cout<<v[i]<<" ";cout<<endl;}
using namespace std;

vector<string> gravity(vector<string> board)
{
     vector<string> ret;
     
     REP(i,board.size())
     {
   /*    int j=0;
       while(j<board.size()&&board[i][j]=='.') ++j;
       if(j==board.size()) {ret.PB(board[i]);continue;}
       while(j<board.size()&&board[i][j]!='.')++j;
       if(j==board.size()) {ret.PB(board[i]);continue;}*/
       
       string tmp=""; REP(j,board.size()) if(board[i][j]!='.') tmp+=board[i][j];
       
       
       string tmp2=""; REP(u,board.size()-tmp.size()) tmp2+='.';
       tmp2+=tmp;
      // cout<<tmp2<<"|"<<endl;
       ret.PB(tmp2);
     }
     return ret;
 }
 
 bool check(vector<string> board,char A,int K)
 {
      REP(i,board.size())REP(j,board.size()) if(board[i][j]!=A) board[i][j]='.';
      
      REP(i,board.size()) REP(j,board.size())
      if(board[i][j]!='.')
      {
        int cnt=0;int wsk=j; while(wsk<board.size()&&board[i][wsk]!='.') {++cnt;++wsk;}
        if(cnt>=K) return true;
        cnt=0;wsk=i; while(wsk<board.size()&&board[wsk][j]!='.') {++cnt;++wsk;}
        if(cnt>=K) return true;
        cnt=0;int wskX=i;int wskY=j; while(wskX<board.size()&&wskY<board.size()&&board[wskX][wskY]!='.') {++cnt;++wskX;++wskY;}
        if(cnt>=K) return true;
        cnt=0; wskX=i;wskY=j; while(wskX<board.size()&&wskY<board.size()&&board[wskX][wskY]!='.') {++cnt;--wskX;++wskY;}
        if(cnt>=K) return true;
      }
      return false; 
 }
 
int main()
{

   ios_base::sync_with_stdio(0);
   int T;cin>>T;
   REP(ww,T)
   {
   
          int N,K;cin>>N>>K;
          vector<string> board;
          REP(i,N) {string a;cin>>a;board.PB(a);}
                                       
          
      //    REP(i,N) {REP(j,N) cout<<board[i][j];cout<<endl;}         
       //   board=rotate(board);
       //   REP(i,N) {REP(j,N) cout<<board[i][j];cout<<endl;}
       //  cout<<endl;
          board=gravity(board);
       //   REP(i,N) {REP(j,N) cout<<board[i][j];cout<<endl;}
          
          bool blue = check(board,'B',K);
          bool red = check(board,'R',K);
          string ret="Neither";
          if(blue&&red) ret="Both";
          else if(blue) ret="Blue";
          else if(red) ret="Red";                
          cout<<"Case #"<<(ww+1)<<": "<<ret<<endl;
   }
}
