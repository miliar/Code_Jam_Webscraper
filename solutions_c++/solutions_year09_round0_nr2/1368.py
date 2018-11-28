#include<iostream>
#include<fstream>
#include<map>
using namespace std;

int mp[101][101];
char pict[101][101];
int main() {
  int N,H,W;
  ifstream IN("in.txt");
  ofstream OUT("out.txt");
  IN >> N;
  map< pair<int,int> ,pair<int,int> > M;
  int min,mk,mj;
  char st,sk;
  pair<int,int> P,p;
  for (int i = 1; i <= N; i++) {
    IN >> H >> W;
    st = 'a';
    for (int j = 0; j < H; j++) 
      for (int k = 0; k < W; k++)
        IN >> mp[j][k];
    M = map< pair<int,int> ,pair<int,int> >();
    for (int j = 0; j < H; j++) {
      for (int k = 0; k < W; k++) {
        if (!pict[j][k]){
        P.first = j;
        P.second = k;
        hell:;
        min = mp[j][k];
        if (j - 1 >= 0) {
          if (mp[j-1][k] < min){ 
            min = mp[j-1][k];
            mj = j-1;
            mk = k;
          }
        }
        if (k - 1 >= 0) {
          if (mp[j][k-1] < min){ 
            min = mp[j][k-1];
            mj = j;
            mk = k - 1;
          }
        }
        if (k + 1 < W) {
          if (mp[j][k + 1] < min)  {
            min = mp[j][k + 1];
            mj = j;
            mk = k + 1;
          }
        }
        if (j + 1 < H) {
          if (mp[j+1][k] < min) {
            min = mp[j+1][k];
            mj = j + 1;
            mk = k;
          }
        }   
        if (min == mp[j][k])  {
          p.first = j;
          p.second = k;
          if (pict[j][k]) 
            sk = pict[j][k];
          else {
            sk = st;
            st++;
          }
          while(1) {
            pict[p.first][p.second] = sk;
            if (p == P) break;
            p = M[p];
          }
          j = P.first;
          k = P.second;
       }
       else {
          M[make_pair(mj,mk)] = make_pair(j,k);
          k = mk;
          j = mj;
          if (pict[j][k]){
            sk = pict[j][k];
            p.first = j;
            p.second = k;
            while(1) {
              pict[p.first][p.second] = sk;
              if (p == P) break;
              p = M[p];
            }
            j = P.first;
            k = P.second;
          }
          else goto hell;
        }
      }
     }
    }      
    OUT<<"Case #"<<i<<":"<<endl;
    for (int j = 0; j < H; j++) {
      for (int k = 0; k < W; k++) {
        if(k < W - 1) OUT<<pict[j][k]<<" ";
        else OUT<<pict[j][k];
      }
      OUT<<endl;
    }
     for (int j = 0; j < H; j++) 
      for (int k = 0; k < W; k++) 
        pict[j][k] = 0;     

  }
}
    
    
  
  