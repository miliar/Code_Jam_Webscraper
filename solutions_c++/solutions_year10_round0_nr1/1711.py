#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <ctime>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <stack>
#include <deque>
#include <queue>

#define fi(i,n) for (int i=0; i<n; ++i)
#define fv(i,v) for (int i=0; i<v.size(); ++i)
#define fs(i,s) for (int i=0; i<s.length(); ++i)
#define fab(i,a,b) for (int i=a; i<=b; ++i)
#define fba(i,b,a) for (int i=b; i>=a; --i)

#define VI vector<int>
#define VS vector<string>
#define VL vector<long long>
#define SI set<int>
#define SS set<string>
#define SL set<long long>
#define MSI multiset<int>
#define MSS multiset<string>
#define MSL multiset<long long>

#define P pair
#define V vector
#define S set
#define MS multiset
#define LL long long

#define all(v) v.begin(), v.end()
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define sz size()

#define X first
#define Y second

#define dbg if (is_debugging) 

using namespace std;

// system vars

bool is_debugging=0;
#define problem_name "problem"
char filetype='C';
/*
C = console
T = input.txt/output.txt
I = problem_name.in/problem_name.out
*/

// solution area

void Solve_the_test_case()
{
	int n,k,a[50],c=0;
	fi(i,50) a[i]=0;
	cin >> n >> k;
	while (k>0)
	{
		a[c++]=k%2;
		k/=2;
	}
	fi(i,n)
		if (a[i]==0)
		{
			cout << "OFF";
			return;
		}
	cout << "ON";		
}

// end of solution area

int main()
{
	//===================================================//
	//DON'T FORGET TO COMMENT THIS JUST BEFORE SUBMISSION//
	//===================================================//
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int num;
	scanf("%d", &num);
	fi(i,num)
	{
		printf("Case #%d: ", i+1); 
		Solve_the_test_case();
		printf("\n");
	}
	return 0;
}
