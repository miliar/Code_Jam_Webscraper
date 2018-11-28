#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

typedef long long ll;
typedef long double ld;
#define sz ((int)size())

int oo = (int)1e9;

//#define SMALL
#define LARGE

int bubbleSort(vector <int> & A){
	int cnt = 0;
	int cur = 0;
	//for(int i = 0 ; i < A.size() ; i++ ){
	while(A.size()){
		for(int  j = 0; j < A.size() ; j++){
			if( A[j]-1 <= cur ){
				cnt += j;
				A.erase(A.begin()+j);
				break;
			}
		}
		cur++;
	}
	return cnt;
}

int main()
{
	freopen("a.txt","rt",stdin);
	#ifdef SMALL
	freopen("A-small-attempt1.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	#endif
	#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	#endif

	int t;
	scanf("%d ",&t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ",i+1);
		int n;
		scanf("%d",&n);
		vector <int> arr(n,0);
		char c;
		for(int i = 0 ; i < n ; i++ ){
			for(int j = 0 ; j < n ; j++ ){
				scanf(" %c",&c);
				if( c == '1')
					arr[i] = j+1;
			}
		}

		cout << bubbleSort(arr) << endl;
	}

	return 0;
}
