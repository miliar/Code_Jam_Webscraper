#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

int v[20];

#define MOD 10000

int main() {
  int k;
  scanf("%d",&k);
  getchar();
  string s;
  for (int kk = 0; kk < k; kk++) {
    printf("Case #%d: ",kk+1);
    getline(cin,s);
    int len = s.length();
    memset(v,0,sizeof(v));
    for (int i = 0; i < len; i++) {
      switch(s[i]) {
      case 'w':
	v[0] = (v[0]+1)%MOD;
	break;
      case 'e':
	v[1] = (v[1] + v[0])%MOD;
	v[6] = (v[6] + v[5])%MOD;
	v[14] = (v[14] + v[13])%MOD;
	break;
      case 'l':
	v[2] = (v[2] + v[1])%MOD;
	break;
      case 'c':
	v[3] = (v[3] + v[2])%MOD;
	v[11] = (v[11] + v[10])%MOD;
	break;
      case 'o':
	v[4] = (v[4] + v[3])%MOD;
	v[12] = (v[12] + v[11])%MOD;
	v[9] = (v[9] + v[8])%MOD;
	break;
      case 'm':
	v[5] = (v[5] + v[4])%MOD;
	v[18] = (v[18] + v[17])%MOD;
	break;
      case ' ':
	v[7] = (v[7] + v[6])%MOD;
	v[10] = (v[10] + v[9])%MOD;
	v[15] = (v[15] + v[14])%MOD;
	break;
      case 't':
	v[8] = (v[8] + v[7])%MOD;
	break;
      case 'd':
	v[13] = (v[13] + v[12])%MOD;
	break;
      case 'j':
	v[16] = (v[16] + v[15])%MOD;
	break;
      case 'a':
	v[17] = (v[17] + v[16])%MOD;
	break;
      default:
	break;
      }
    }
    printf("%04d\n",v[18]);
  }
  return 0;
}
