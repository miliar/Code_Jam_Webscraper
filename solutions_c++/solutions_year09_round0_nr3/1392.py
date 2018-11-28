#include <iostream>
#include <string>
#include <iostream>

using namespace std;

const int maxl = 500;

int l;
string line;
string welcome = "welcome to code jam";
const int wsize = welcome.size();
int d[maxl+1][20];
int ds[20];

int main() {
  int T;
  cin >> T;getline(cin, line);
  for(int tcase=1;tcase<=T;tcase++) {
    getline(cin,line);
    l = line.size();
    for(int j=0;j<wsize;j++) ds[j] = 0;
    for(int i=0;i<l;i++){
      if(line[i]==welcome[0])
	d[i][0] = 1;
      else
	d[i][0] = 0;
      for(int j=1;j<wsize;j++)
	if(line[i]==welcome[j]){
	  d[i][j] = ds[j-1];
	}else d[i][j] = 0;
      for(int j=0;j<wsize;j++)
	ds[j] = (ds[j] + d[i][j]) % 10000;
    }
    //for(int i=0;i<wsize;i++) cerr << welcome[i]; cerr << '\n';
    //for(int i=0;i<wsize;i++) cerr << ds[i] << ' '; cerr << '\n';
    cout << "Case #" << tcase << ": "
	 << ((ds[wsize-1] / 1000) % 10)
	 << ((ds[wsize-1] / 100) % 10)
	 << ((ds[wsize-1] / 10) % 10)
	 << ((ds[wsize-1] / 1) % 10) << '\n';
  }
}
