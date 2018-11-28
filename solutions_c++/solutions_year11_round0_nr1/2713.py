#define forr(x,y,z)for(int (x)=(y);(x)<(z);(x)++)
#include <string>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {
  int tcase,n,tujuan[105],ox,to[105],ob,tb[105],no,nb,nto,ntb;
  char kode[105];
  cin >> tcase;

  forr(i,1,tcase+1) {
    cin >> n;
    nto = ntb = 0;
    forr(j,0,n) {
      cin >> kode[j] >> tujuan[j];
      if(kode[j] == 'O') {
        to[nto] = tujuan[j];
        nto++;
      } else {
        tb[ntb] = tujuan[j];
        ntb++;
      }
    }

    ox = ob = 0;
    no = nb = 1;
    int time = 0, getnow = 0;
    do {
      if(kode[getnow] == 'O') {
        time += 1 + abs(no - to[ox]);
        if(nb > tb[ob]) {
          nb -= min(abs(no - to[ox])+1, nb-tb[ob]);
        } else if(nb < tb[ob]) {
          nb += min(abs(no - to[ox])+1, tb[ob]-nb);
        }
        no = to[ox];
        ox++;
      } else {
        time += 1 + abs(nb - tb[ob]);
        if(no > to[ox]) {
          no -= min(abs(nb - tb[ob])+1, no-to[ox]);
        } else if(no < to[ox]) {
          no += min(abs(nb - tb[ob])+1, to[ox]-no);
        }
        nb = tb[ob];
        ob++;
      }
      getnow++;
    } while(getnow < n);

    cout << "Case #" << i << ": " << time << "\n";
  }

  return 0;
}

