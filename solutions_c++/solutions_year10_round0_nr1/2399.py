#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
#define vsort(v) sort((v).begin(), (v).end());
#define vrsort(v) sort((v).begin(), (v).end(), greater<int>());
#define loop(n) for (int i=0;i<n;i++)
#define vforeach(i,v) for (i=0;i<(int)(v).size();i++)
#define forspan(i,s,e) for (i=s;i<e;i++)

void
solve(int num)
{
  int N, K;
  int ans;
  vi v;

  cin >> N >> K;
  v.resize(N);
  for (int i = 0; i < N; i++) {
    v[i] = 0;
  }

  for (int i = 0; i < K; i++) {
    for (int j = 0; j < N; j++) {
      if (v[j]) {
        v[j] = 0;
      } else {
        v[j] = 1;
        break;
      }
    }
  }

  ans = 1;
  for (int i = 0; i < N; i++) {
    if (v[i] == 0) {
      ans = 0;
      break;
    }
  }

  cout << "Case #" << num << ": ";
  if (ans) {
    cout << "ON";
  } else {
    cout << "OFF";
  }
  cout << endl;

//  for (int i = 0; i < N; i++) {
//    cout << v[i] << " ";
//  }
//  cout << endl;
}

int
main()
{
  int N, i;

  cin >> N;
  for (i = 0; i < N; i++) {
    solve(i + 1);
  }
}

