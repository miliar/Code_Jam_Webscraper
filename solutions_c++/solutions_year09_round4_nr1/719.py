#include <iostream>
#include <algorithm>

using namespace std;

const int maxn = 40;

int n;
int a[maxn];


int swap2(int from, int to) {
  //std::cerr << '(' << from << ',' << to << ")\n";
  for(int i=from;i<to;i++) swap(a[i], a[i+1]);
  //for(int i=0;i<n;i++) std::cerr << a[i] << ' ';std::cerr <<'\n';
  return to-from;
}

int main() {
  int T;
  cin >> T;
  for(int tcase=1;tcase<=T;tcase++) {
    cin >> n;
    for(int i=0;i<n;i++){
      a[i] = 0;
      for(int j=0;j<n;j++){
	char tmp;
	cin >> tmp;
	if(tmp=='1') a[i] = j; 
      }
    }
    //for(int i=0;i<n;i++) std::cerr << a[i] << ' ';std::cerr <<'\n';
    int sol = 0;
    for(int i=0;i<n;i++) {
      int count = 0;
      for(int l=0;l<n;l++)
	if(a[l]>=i) count++;
      
      for(int l=n-1;l>=0;l--)
	if(a[l]>=i) {
	  if(l<i+count-1)
	    sol+= swap2(l, i+count-1);
	  count--;
	}
    }

    cout << "Case #" << tcase << ": " << sol << '\n';
  }
}
