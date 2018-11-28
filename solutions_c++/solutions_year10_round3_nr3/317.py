#include <cstdlib>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;
fstream fin,fout;

char map[512][512];
int  dmap[512][512];

class CAns{
    public:
      int c,size;
    };

vector<CAns> ans;
int n,m;
int ssize = 0;

void dbg(){
    for(int i=0;i<m;++i){
      for(int r=0;r<n;++r)
        if(1){
          if(map[i][r]!='*')
            fout << (int)map[i][r];else
            fout << ' ';
          }else
          fout << dmap[i][r] << " ";
      fout << endl;
      }
    fout << endl;
    }

void erase(int x,int y,int w){
    for(int i=x+1;i<=x+w;++i)
      for(int r=y+1;r<=y+w;++r){
         map[i][r]  = '*';
         dmap[i][r] = 0;
         }
    ssize+=w*w;
    }

void bans(){
    //ans.clear();
    
    int mx = 1;
    for(int i=0;i<m;++i)
      for(int r=0;r<n;++r)
        if(mx < dmap[i][r])
          mx = dmap[i][r];
    
    for(int i=0;i<m;++i)
      for(int r=0;r<n;++r)
        if(dmap[i][r]==mx){
          erase(i-mx,r-mx,mx);
          if(!(ans.size() && ans[ans.size()-1].size==mx)){
            ans.push_back(CAns());
            ans[ans.size()-1].size = mx;
            }
          ans[ans.size()-1].c++;
          return;
          }
    }

void ndmap(){
    for(int i=0;i<m;++i)
      if(map[i][0]=='*')
        dmap[i][0] = 0;else
        dmap[i][0] = 1;
        
    for(int i=0;i<n;++i)
      if(map[0][i]=='*')
        dmap[0][i] = 0;else
        dmap[0][i] = 1;
    
    for(int i=1;i<m;++i)
      for(int r=1;r<n;++r){
        if(map[i][r] != map[i-1][r] &&
           map[i][r] != map[i][r-1] &&
           map[i][r] == map[i-1][r-1]){
          dmap[i][r] = dmap[i-1][r-1]+1;
          dmap[i][r] = min(dmap[i][r],dmap[i][r-1]+1);
          dmap[i][r] = min(dmap[i][r],dmap[i-1][r]+1);
          }else
          dmap[i][r] = 1;
        if(map[i][r]=='*')
          dmap[i][r] = 0;
        }
    
    //dbg();
    }

void wrk(int testn){
    fin >> m >> n;
    
    for(int i=0;i<m;++i){
      for(int r=0;r<n/4;++r){
        char c;
        fin >> c;
        if(c >= 'A')
          c = c-'A'+10;else
          c-='0';
        for(int q=0;q<4;++q){
          map[i][r*4+3-q] = c%2;
          c/=2;
          //fout << int(map[i][r*4+3-q]);
          }
        }
      //fout << endl;
      }
    ans.clear();
    ssize = 0;
    
    while(ssize < n*m){
      ndmap();
      bans();
      }
    
    fout << "Case #" << testn << ": " << ans.size() << endl;
    for(int i=0;i<ans.size();++i)
      fout << ans[i].size << " "<< ans[i].c << endl; 
    }

int main(){
    fin. open("./input.txt", fstream::in);
    fout.open("./output.txt",fstream::out);

    int testC;
    fin >> testC;
    
    for(int i=0;i<testC;++i)
      wrk(i+1);
    
    fin.close();
    fout.close();
    return 0;
    }





