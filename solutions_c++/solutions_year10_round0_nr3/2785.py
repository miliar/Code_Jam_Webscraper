#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

#define DEBUG 0

#if DEBUG

#define CIN cin
#define COUT cout

#else

ifstream fin;
ofstream fout;
#define CIN fin
#define COUT fout

#endif

int C;
int k;
int R;
int N;
int arr_g[1000];
long long arr_sum[1000];

#define M(i) ((i) % N)

int make_group(int pos, long long &value) {
  long long sum = 0;
  int i;
  for(i = 0; i < N; ++i) {
    sum += arr_g[M(pos + i)];
    if(sum > k) {
      sum -= arr_g[M(pos + i)];
      break;
    }
  }
  
  value = sum;
  return M(pos + i);
}

int main() {
#if !DEBUG
  fin.open("C-small-attempt1.in");
  fout.open("res.txt");
#endif

  CIN >> C;
  int c = 1;
  while(c <= C) {
    CIN >> R >> k >> N;
    int special_mark = -1;
    long long sum = 0;
    for(int i = 0; i < N; ++i) {
      CIN >> arr_g[i];
      if(arr_g[i] > k) {
        special_mark = i;
      }
    }
    if(special_mark != -1) {
      for(int i = 0; i < special_mark; ++i) {
        sum += arr_g[i];
      }
    }
    else {
      int pos_mark;
      pos_mark = make_group(0, sum);
      arr_sum[0] = sum;
      int r = 1;
      int next_pos = pos_mark;
      while(r < R) {
        next_pos = make_group(next_pos, sum);
        arr_sum[r] = sum;
        r++;
        if(next_pos == pos_mark) {
          break;
        }
      }
      if(r == R) {
        sum = 0;
        for(int i = 0; i < r; ++i) {
          sum += arr_sum[i];
        }
      } else {
        sum = 0;
        for(int i = 1; i < r; ++i) {
          sum += arr_sum[i];
        }
        int nr = (R - 1) / (r - 1);
        int remain = (R - 1) % (r - 1);
        sum *= nr;
        sum += arr_sum[0];
        for(int i = 0; i < remain; ++i)
          sum += arr_sum[i+1];
      }
    }
    COUT << "Case #" << c << ": " << sum << endl;
    c++;
  }
  return 0;
}