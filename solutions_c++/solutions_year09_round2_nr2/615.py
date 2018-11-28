int N;

#include <stdio.h>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;


void restart(string& num, int count) {
  if (count <= 1) return;
  sort(num.begin(), num.begin() +  count);
  reverse(num.begin(), num.begin() +  count);
}

// Increase length by one (add a zero and restart numering)
const string& insert_zero(string& num) {
  num += '0';
  // find smallest digit larger than zero
  int min = '0' + 10;
  int min_p = -1;
  for (int p=0; p<num.size()-1; p++) {
    if (num[p]=='0') continue;
    if (num[p] < min) {
      min_p = p;
      min = num[p];
    }
  }
  assert(min_p != -1);
  swap(num[min_p], num[num.size()-1]);
  
  // Sort remaining digits
  restart(num, num.size() - 1);
  return num;
}

const string& next(string& num, int mustinc) {
  if (mustinc >= num.size()) return insert_zero(num);
  
  // Search for next larger
  int k = num[mustinc];
  while (++k <= '9') {
    for (int p = mustinc -1 ; p>=0; p--) {
      if (num[p] == k) {
        swap(num[p], num[mustinc]);
        restart(num, mustinc);
        return num;
      }
    }
  }

  // none found, must try with one larger
  return next(num, mustinc+1);
}

int main()
{
  // Input
  scanf("%d\n",&N);
  fprintf(stderr,"N = %d: \n",N);

  // Output
  for (int x=1; x<=N; x++) {
    
    fprintf(stderr,"Case #%d: \n",x);
    string num;
    cin >> num;
    reverse(num.begin(), num.end());
    next(num,0);
    reverse(num.begin(), num.end());
    printf("Case #%d: %s\n",x, num.c_str());
  }
  return 0;
}
