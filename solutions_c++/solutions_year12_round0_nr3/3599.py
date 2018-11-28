#include <iostream>
#include <cmath>

using namespace std;

void add(char *num, int len) {
  if (len == 0) return;
  if (num[len-1] == 9) {
    num[len-1] = 0;
    add(num, len-1);
  } else {
    num[len-1]++;
  }
}

int check2(char *num, int len, int start) {
  for (int i = 0; i < len; i++) {
    if (num[start] != num[i]) return 1;
    if (++start >= len) start = 0;
  }
  return 0;
}

int check(char *num, char *low, char *high, int len, int start) {
  int s = start;
  if (num[start] > low[0] && num[start] < high[0]) return check2(num, len, s);
  if (num[start] < low[0] || num[start] > high[0]) return 0;
  if (num[start] == low[0]) { 
    for (int i = 0; i < len; i++) {
      if (num[start] > low[i]) return check2(num, len, s);
      if (num[start] < low[i]) return 0;
      if (++start >= len) start = 0;
    }
  } else if (num[start] == high[0]) { 
    for (int i = 0; i < len; i++) {
      if (num[start] > high[i]) return 0;
      if (num[start] < high[i]) return check2(num, len, s);
      if (++start >= len) start = 0;
    }
  }
  return check2(num, len, s);
}

int tochar(int num, char *ch) {
  char tmp[10];
  char len;

  for (len = 0; num > 0; len++) {
    tmp[len] = (num % 10);
    num /= 10;
  }

  for (int i = len-1; i >= 0; i--) {
    *ch = tmp[i];
    ch++;
  }

  return len;
}

int main() {
  int t;
  int a, b;
  int len;
  int ans;
  char ca[10], cb[10], num[10];

  cin >> t;
  
  for(int i = 0; i < t; i++){
    cin >> a >> b;
    len = tochar(a, ca);
    tochar(b, cb);
    //cout << (int)ca[0] << (int)ca[1] <<  (int)ca[2] <<  (int)ca[3] << endl;
    //cout << (int)cb[0] << (int)cb[1] <<  (int)cb[2] <<  (int)cb[3] << endl;
    ans = 0;
    for (int j = 1; j < len; j++) {
      tochar(a, num);
      for (int k = a; k <= b; k++) {
	if (check(num, ca, cb, len, j)) {
	  ans++;
	  //cout << k << endl;
	  //cout << (char)('0'+num[0]) << endl;
	  //cout << (int)num[0] << (int)num[1] <<  (int)num[2] <<  (int)num[3] << endl;
	}
	add(num, len);
      }
    }
    
    cout << "Case #" << (i+1) << ": " << (ans/2) << endl;
  }

  return 0;
}
