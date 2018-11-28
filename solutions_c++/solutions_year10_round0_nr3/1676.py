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

int n,k,r,a[2000];

void Solve_the_test_case()
{
	long long p[2000],t[2000],s=0,h;
	cin >> r >> k >> n;
	h=r;
	fi(i,n)
		cin >> a[i];
	fi(i,n)
	{
		long long q=0,w=s;
		while (q+a[s]<=k)
		{
			q+=a[s];
			++s;
			s%=n;
			if (w==s)
				break;
		}
		p[w]=q;
		t[w]=s;
	}
	long long cl=0,cc=0,cs;
	bool u[2000];
	fi(i,n)
		u[i]=0;
	s=0;
	fi(i,n*3)
	{
		if (u[s])
		{
			cs=s;
			break;
		}
		else
		{
			u[s]=1;
			s=t[s];
		}
	}
	s=cs;
	do
	{
		cc+=p[s];
		++cl;
		s=t[s];
	}
	while (s!=cs);
	s=0; long long e=0;
	while (r>0)
	{
		if (cs==r && r>cl*2)
		{
			long long g=r/cl;
			r%=cl;
			e+=g*cc;
		}
		e+=p[s];
		s=t[s];
		--r;
	}
	cout << e;
	r=h;
}

void Solve_stupid()
{
	int e=0;
	queue<int> q;
	fi(i,n)
		q.push(a[i]);
	fi(i,r)
	{
		int s=0,d=0;
		while (s+q.front()<=k && d<n)
		{
			int w=q.front();
			s+=w;
			q.pop();
			q.push(w);
			++d;
		}
		e+=s;
	}
	cout << e;
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
		//printf(" / ");
		//Solve_stupid();
		printf("\n");
	}
	return 0;
}
