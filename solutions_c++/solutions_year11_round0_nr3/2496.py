#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iomanip>
#include <cstdio>

using namespace std;

#define PRINT(x) cout << "DEBUG " << #x << " = " << x <<  endl;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i = 0; i < (n); i++)
#define frr(i, n) for(int i = 0; i < (n); i++)
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long ll;

int N;
int arr[1010];

void read()
{
 cin >> N;
 frr (i,N)
  cin >> arr[i];
}

int proc()
{
 int bits[22];
 _cl(bits);
 frr (i, N) {
  frr (j,21)
   bits[j] += ((1<<j) & arr[i]) ? 1 : 0;
 }
 frr (i, 21)
  if (bits[i]%2==1) 
   return -1;
 int sum=0, min_val=arr[0];
 frr (i, N) {
  sum += arr[i];
  min_val = min(min_val, arr[i]);
 }
 return sum - min_val;
}

int main()
{
	int T;

	cin >> T;

	frr(i, T)
	{
		read();
		int res = proc();
  cout << "Case #" << i+1 << ": ";
  if (res == -1)
   cout << "NO" << endl;
  else
   cout << res << endl;
	}

	return 0;
}

