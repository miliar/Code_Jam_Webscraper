#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> VI;
typedef vector<string> VS;

#define Forall(i,v)   for(int i=0;i<(int)v.size();++i)
#define For(i,a,b)    for(int i=(a);i<(b);++i)
#define Rep(i,n)      for(int i=0;i<(n);++i)

#define All(a) (a).begin(),(a).end()
#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define Sort(c) sort((c).begin(),(c).end())

int solve(int N, VI A, VI B)
{
	int cnt = 0;
	For(i,0,N) For(j,i+1,N)
	{
		if(A[i+1]>A[i] && B[i+1]<B[i]) cnt++;
		if(A[i+1]<A[i] && B[i+1]>B[i]) cnt++;
	}
	return cnt;
}

int main(int argc, char* argv[])
{
	int num_of_test_cases;
	cin >> num_of_test_cases;
	
	Rep(test_case,num_of_test_cases)
	{
		int N;
		cin >> N;
		VI A(N);
		VI B(N);
		Rep(i,N) cin >> A[i] >> B[i];
		int r = solve(N, A, B);
		cout << "Case #" << test_case+1 << ": " << r << endl;
	}
	
	return 0;
}
