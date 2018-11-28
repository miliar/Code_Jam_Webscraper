#define forr(x,y,z)for(int (x)=(y);(x)<(z);(x)++)
#include <string>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;
char pasangan[10],hasil[10],lawan[10];

int getcode(char c) {
  switch(c) {
    case 'Q' : return 0;
    case 'W' : return 1;
    case 'E' : return 2;
    case 'R' : return 3;
    case 'A' : return 4;
    case 'S' : return 5;
    case 'D' : return 6;
    case 'F' : return 7;
    default : return -1;
  }
}

int main() {
  int tcase, c, d, n;
  cin >> tcase;
  forr(i,1,tcase+1) {
    forr(j,0,8) {
      pasangan[j] = lawan[j] = hasil[j] = ' ';
    }
    cin >> c;
    string s;
    forr(j,0,c) {
      cin >> s;
      pasangan[getcode(s[0])] = s[1];
      pasangan[getcode(s[1])] = s[0];
      hasil[getcode(s[0])] = hasil[getcode(s[1])] = s[2];
    }

    cin >> d;
    forr(j,0,d) {
      cin >> s;
      lawan[getcode(s[0])] = s[1];
      lawan[getcode(s[1])] = s[0];
    }

    cin >> n >> s;
    string solve = "";
    int lenh = 0;
    forr(j,0,n) {
      if(lenh > 0 && solve[lenh-1] == pasangan[getcode(s[j])]) {
        solve[lenh-1] = hasil[getcode(s[j])];
      } else {
        bool rusak = false;
        int start = -1;
        forr(k,0,lenh) {
          if(solve[k] == lawan[getcode(s[j])]) {
            start = k;
            rusak = true;
            break;
          }
        }

        if(rusak) {
          solve = "";
          lenh = 0;
        } else {
          solve.push_back(s[j]);
          lenh++;
        }
      }
    }

    cout << "Case #" << i << ": [";
    if(lenh) {
      cout << solve[0];
      forr(j,1,lenh) cout << ", " << solve[j];
    }
    cout << "]\n";
  }

  return 0;
}

