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

char beg(int f,int c);

char M[101][101];
int V[101][101];
int F,C,last=0;


void flowy(int f,int c){
     int dir=0,min=1000000;
     if(f>0 && V[f][c] > V[f-1][c]){ min = V[f-1][c]; dir=1;}
     if(c>0 && V[f][c] > V[f][c-1] && V[f][c-1] < min){min = V[f][c-1]; dir = 2;}
     if(c + 1 < C && V[f][c] > V[f][c+1] && V[f][c+1] < min ){min = V[f][c+1]; dir =3;}
     if(f+1 < F && V[f][c] > V[f+1][c] && V[f+1][c] < min){min = V[f+1][c]; dir=4;}
     if(dir == 1 && M[f][c] < M[f-1][c]){ M[f-1][c] = M[f][c]; beg(f-1,c);}
     if(dir == 2 && M[f][c] < M[f][c-1]){ M[f][c-1] = M[f][c]; beg(f,c-1);}
     if(dir == 3 && M[f][c] < M[f][c+1]){ M[f][c+1] = M[f][c]; beg(f,c+1);}
     if(dir == 4 && M[f][c] < M[f+1][c]){ M[f+1][c] = M[f][c]; beg(f+1,c);}
}

char beg(int f,int c){
     if(M[f][c] <= 'z'){flowy(f,c); return M[f][c];}
     int dir=0,min=1000000;
     if(f>0 && V[f][c] > V[f-1][c] ){ min = V[f-1][c]; dir=1;}
     if(c>0 && V[f][c] > V[f][c-1] && V[f][c-1] < min){min = V[f][c-1]; dir = 2;}
     if(c + 1 < C && V[f][c] > V[f][c+1] && V[f][c+1] < min ){min = V[f][c+1]; dir =3;}
     if(f+1 < F && V[f][c] > V[f+1][c] && V[f+1][c] < min){min = V[f+1][c]; dir=4;}
     if(dir == 1){return M[f][c] = beg(f-1,c);}
     if(dir == 2){return M[f][c] = beg(f,c-1);}
     if(dir == 3){return M[f][c] = beg(f,c+1);}
     if(dir == 4){return M[f][c] = beg(f+1,c);}
     last++; M[f][c] = 'a' + last; return M[f][c];
}


int main(){
    int kases; cin>>kases;
    for(int k=1;k<=kases;k++){
       cin>>F>>C; last = 0;
       for(int f=0;f<F;f++){
          for(int c=0;c<C;c++){
              cin>>V[f][c]; M[f][c] = 'z' +1;
          }
       }
       M[0][0] = 'a';
       for(int f=0;f<F;f++){
          for(int c=0;c<C;c++){
             beg(f,c);
          }
       }
       cout<<"Case #"<<k<<":"<<endl;
       for(int f=0;f<F;f++){
          cout<<M[f][0];
          for(int c=1;c<C;c++){
             cout<<" "<<M[f][c];
          }cout<<endl;
       }
    }
}
