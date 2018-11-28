#include <iostream>
#include <vector>

using namespace std;

int calc(int a1,int a2,int b1,int b2)
{

  int tot = 0;

  for (int i=a1;i<=a2;i++) {
    for (int j=b1;j<=b2;j++) {
      vector<int> arr;
      int max;
      int min;
      if (i > j) {
	max = i;
	min = j;
      } else {
	max = j;
	min = i;
      };

      while (max % min) {
	arr.push_back(max/min);
	int res = max % min;
	max = min;
	min = res;
      };

      arr.push_back(max/min);

      int play=0;
      for (int k=0;k<arr.size();k++) {
	if (arr[k] != 1) {
	  break;
	};
	play++;
      };

      if (!(play%2)) {
	tot++;
      };

    };
  };

  return tot;

};

int main() {

  int n;
  cin >> n;

  for (int i=0;i<n;i++) {

    int a1, a2, b1, b2;
    cin >> a1 >> a2 >> b1 >> b2;
    int res = calc(a1,a2,b1,b2);
    cout << "Case #" << i+1 << ": " << res << endl;
    
  };

  return 0;

};
