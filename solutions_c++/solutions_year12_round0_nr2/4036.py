#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>

#define fr2(i,n) for(i;i<(int)(n);i++)
#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef pair<string, string> ps;

ll T, S, P, t[100];



//Input  
//4
//3 1 5 15 13 11
//3 0 8 23 22 21
//2 1 1 8 0
//6 2 8 29 20 8 18 18 21
//
//Output 
//Case #1: 3
//Case #2: 2
//Case #3: 1
//Case #4: 3

void work()
{
	ll pos1 = 0;
	ll pos2 = 0;

	ll res = 0;
	ll i = 0, j = 0;
	fr(i, T) fr(j, T) if(t[i] > t[j])	 {
		ll temp = t[i];
		t[i] = t[j];
		t[j] = temp;	
	}

	fr(i, T)	{
		if(t[i] >= (P * 3) - 2)	{
			res++;
			pos1 = i + 1;
		}
	}

	if(T == res) goto PRINT;
	
	pos2 = pos1 + (T-res);	
	/*cout << "pos1 start : " <<  pos1 << endl;*/
	fr2(pos1, pos2)	{
		if(S > 0 && t[pos1] < 2)	{
			break;
		}
		if(S > 0 && t[pos1] >= (P * 3) - 4)	 {
			res++;
			S--;
		}
		if(S == 0) goto PRINT;
		if(T == res) goto PRINT;

	}
	
	
PRINT:
	cout << res << endl;
}

int main() {
	int total_cases, case_num = 0;
	
	
	cin >> total_cases;
	
	while (case_num < total_cases) {
		cin >> T >> S >> P;

		ll i = 0;
		fr(i,T)	cin >> t[i];
		
		case_num++;
		 cout << "Case #" << case_num << ": ";
		/*cout << "Case #%d: " << case_num;*/
		/*printf("Case #%d: ", case_num);*/

		work();		
		
	}
	return 0;
}
