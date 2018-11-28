#include <iostream>
#include <cstring>

#define MAX 1005

using namespace std;

int rides, cap, n;
long long sum;

long long v[MAX];
int jumpto[MAX];
long long acc[MAX];

void buildT() {
  memset(jumpto, 0, sizeof(jumpto));
  memset(acc, 0, sizeof(acc));

  for (int i=0; i<n;i++) {
    int j=i;
    while (true) {
      if (acc[i]+v[j] <= cap) {
	acc[i] += v[j];
	j = (j+1)%n;
      }
      else
	break;
    }
    jumpto[i] = j;
  }
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i<=t; i++) {
    cin >> rides >> cap >> n;

    long long sum = 0;
    for (int j=0;j<n;j++) {
      cin >> v[j];
      sum+=v[j];
    }
    
    if (sum <= cap)
      cout << "Case #" << i << ": " << sum*rides << endl;
    else {
      buildT();
      
      long long cnt = 0;
      
      int next = 0;
      for (int j = 0; j<rides; j++) {
	cnt += acc[next];
	next = jumpto[next];
      }
      cout << "Case #" << i << ": " << cnt << endl;
    }
  }
  return 0;
}
