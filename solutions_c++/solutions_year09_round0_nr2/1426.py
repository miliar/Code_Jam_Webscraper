#include<iostream>
#include<string>
#include<vector>

using namespace std;

int H, W;
char curr_char = 'a' - 1;


int getN(int pos) {
  return pos - W; 
}

int getS(int pos) {
  if(pos + W < H*W)
    return pos + W;
  return -1; 
}
int getW(int pos) {
  if (pos%W == 0)
    return -1;
  return pos - 1; 
}
int getE(int pos) {
  if ((pos+1)%W == 0)
    return -1;
  return pos + 1; 
}

char getRegion(const vector<int>& alts,
	       vector<char>& regs,
	       int pos) {
  if (regs[pos] != '0') {
    return regs[pos];
  }
  int curr_alt = alts[pos];
  int min_alt = curr_alt;
  int min_pos = pos;
  int npos = getN(pos);
  int epos = getE(pos);
  int wpos = getW(pos);
  int spos = getS(pos);
  if (npos >= 0 && alts[npos] < min_alt) {
    min_alt = alts[npos];
    min_pos = npos;
  }
  if (wpos >= 0 && alts[wpos] < min_alt) {
    min_alt = alts[wpos];
    min_pos = wpos;
  }
  if (epos >= 0 && alts[epos] < min_alt) {
    min_alt = alts[epos];
    min_pos = epos;
  }
  if (spos >= 0 && alts[spos] < min_alt) {
    min_alt = alts[spos];
    min_pos = spos;
  }
  //Sink
  if (min_pos == pos) {
    //    cout << "SINK: " << pos << endl;
    regs[pos] = ++curr_char;
    return curr_char;
  }
  char setc = getRegion(alts, regs, min_pos);
  regs[pos] = setc;
  return setc;
}

int main(int argc, char * argv[])
{
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    curr_char = 'a' - 1;
    cin >> H >> W;
    //    cout << H << W << endl;
    long long int N = H*W;
    vector<int> alts ;
    vector<char> regs;
    for (int i = 0; i < N; i++) {
      int alt;
      cin >> alt;
      alts.push_back(alt);
      regs.push_back('0');
    }
    for (int j = 0; j < N; j++) {
      if (regs[j] == '0') {
	getRegion(alts, regs, j);
      }
    }
    cout << "Case #" << t+1 << ":" << endl;
    for (int l = 0; l < N; l++) {
      if ((l+1)%W == 0) {
	cout << regs[l] << endl;
      } else {
	cout << regs[l] << " ";
      }
    }
  }
}
