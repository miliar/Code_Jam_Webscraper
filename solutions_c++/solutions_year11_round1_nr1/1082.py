#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  int cx;
  cin >> cx;
  for (int kk = 1; kk <= cx; ++kk){
    cout <<"Case #"<<kk<<": ";
    int n,pd,pg;
    cin >> n >> pd >> pg;
    int wd,ld,wg,lg;
    wg = pg*10;
    lg = 1000 -wg;
    bool possible=false;
    for (int k = 1;k<=min(n,100);++k){
      if ((pd*k)%100==0){
        wd = pd*k/100;
	ld = k-wd;
	if (wd<=wg && ld<=lg){
	  possible = true;
	}
      }
    }
    cout << (possible?"Possible":"Broken") <<endl;
  }
}
