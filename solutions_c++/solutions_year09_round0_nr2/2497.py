#include <iostream>
using namespace std;

int field[101][101];
int result[101][101];
int vect[101][101];
int px[5] = {0,0,-1,1,0};
int py[5] = {0,-1,0,0,1};

int calc2(int h, int w){
  if(result[h][w]>=0) return result[h][w];
  result[h][w] = calc2(h+py[vect[h][w]], w+px[vect[h][w]]);
  return result[h][w];
}

void calc(int H, int W){
  for(int h=0; h<H; h++) for(int w=0; w<W; w++) result[h][w] = -1;
  
  bool no, we, ea, so;
  int sink = 0, minval, minvec;
  for(int h=0; h<H; h++)
    for(int w=0; w<W; w++){
      minval = 99999;
      minvec = -1;
      no = true;
      if(h-1>=0){if(field[h-1][w]>=field[h][w]) no = false;}
      else no = false;
      if(no) if(minval>field[h-1][w]){ minval = field[h-1][w]; minvec = 1; }
      we = true;
      if(w-1>=0){if(field[h][w-1]>=field[h][w]) we = false;}
      else we = false;
      if(we) if(minval>field[h][w-1]){ minval = field[h][w-1]; minvec = 2; }
      ea = true;
      if(w+1<W){if(field[h][w+1]>=field[h][w]) ea = false;}
      else ea = false;
      if(ea) if(minval>field[h][w+1]){ minval = field[h][w+1]; minvec = 3; }
      so = true;
      if(h+1<H){if(field[h+1][w]>=field[h][w]) so = false;}
      else so = false;
      if(so) if(minval>field[h+1][w]){ minval = field[h+1][w]; minvec = 4; }
      if(no==false && we==false && ea==false && so==false){
	result[h][w] = sink++;
	minvec = 0;
      }
      vect[h][w] = minvec;
      
    }
  /*
  for(int h=0; h<H; h++){
    for(int w=0; w<W; w++){
      cout << result[h][w] << " ";
    }cout << endl;
  }
  */

  for(int h=0; h<H; h++)
    for(int w=0; w<W; w++)
      if(result[h][w]<0) calc2(h, w);

  int label = 0;
  int labels[26];
  for(int i=0; i<26; i++) labels[i] = -1;
  for(int h=0; h<H; h++){
    for(int w=0; w<W; w++){
      if(labels[result[h][w]]==-1){
	labels[result[h][w]] = label++;
      }
      //cout << result[h][w] << " ";
      cout << (char)(labels[result[h][w]]+'a');
      if(w!=W-1) cout << " ";
    }
    cout << endl;
  }


}

int main(){
  int T, H, W, d;
  cin >> T;
  for(int i=0; i<T; i++){
    cin >> H >> W;
    for(int h=0; h<H; h++)
      for(int w=0; w<W; w++)
	cin >> field[h][w];
    cout << "Case #" << i+1 << ":" << endl;
    calc(H, W);
  }
  return 0;
}
