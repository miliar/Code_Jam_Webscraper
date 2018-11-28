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

int arr[210][2];
int CT[2] = {0,0};
int pos[2] = {-1,-1};
int button[2];

void read()
{
 string st;
 cin >> N;
 frr (i, N) {
  cin >> st >> arr[i][1];
  
  arr[i][0] = (st[0] == 'O' ? 0 : 1);
 }
}

void next(int r) {
 if (r!=0 && r!=1) {
  return;
 }

 pos[r]++;
 while (pos[r] < N) {
  if (arr[pos[r]][0] == r) {
   CT[r] += abs(button[r]-arr[pos[r]][1]);
   button[r] = arr[pos[r]][1];
   break;
  }
  pos[r]++;
 }
}

int proc()
{
 CT[0]=CT[1] = 0; //CT = {0,0};
 pos[0]=pos[1]=-1; //pos = {-1,-1};
 button[0]=button[1]=1; //button = {1,1};

 next(0); next(1);

 int other;
 frr (i, N) {
  other = (arr[i][0]+1)%2;
  CT[arr[i][0]]++;
  //cout << "*" << i << ": " << CT[arr[i][0]] << "b" << button[arr[i][0]] << "p" << pos[arr[i][0]] << endl;
  if (CT[other] < CT[arr[i][0]])
   CT[other] = CT[arr[i][0]];
  if (i==N-1) {
   return CT[arr[i][0]];
  }
  next(arr[i][0]);
 }
}

int main()
{
	int T;

	cin >> T;

	frr(i, T)
	{
		read();
	 cout << "Case #" << i+1 << ": " << proc() << endl;
	}

	return 0;
}

