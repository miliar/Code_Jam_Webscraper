#include <cstdio>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

const int MAX_N = 1024;
//typedef vector<int> VI;

int n;
int A[MAX_N];
int S; // xor sum
int ans;

map<int,int> M[MAX_N];

void input()
{
	int i;
	
	scanf("%d", &n);

	S = 0;
	M[0].clear();
	M[0][0] = 0;
	for(i=1; i<=n; i++) {
		scanf("%d", &A[i]);
		cerr << A[i] << " ";
		S ^= A[i];
	}

	cerr << endl;
}

int solve(int sum)
{
	int i, j;
	map<int,int>::iterator it, itnew;

	for(i=1; i<=n-1; i++) {
		M[i].clear();
		
		for(it=M[i-1].begin(); it!=M[i-1].end(); it++) {
			if( (itnew=M[i].find(it->first ^ A[i])) == M[i].end()) {
				M[i][ it->first ^ A[i] ] = it->second + A[i];
				//itnew = M[i].find(it->first ^ A[i]);
				//printf("#1 i=%d: it=(%d,%d) itnew=(%d,%d)\n", i, it->first, it->second, itnew->first, itnew->second);
			} else {
				//itnew = M[i].find(it->first ^ A[i]);
				itnew->second = max(it->second + A[i], itnew->second);
				//printf("#2 i=%d: it=(%d,%d) itnew=(%d,%d)\n", i, it->first, it->second, itnew->first, itnew->second);
			}

			//continue;
			if((itnew=M[i].find(it->first)) == M[i].end()) {
				M[i][ it->first ] = it->second;
				//itnew = M[i].find(val);
				//printf("#1 i=%d: it=(%d,%d) itnew=(%d,%d)\n", i, it->first, it->second, itnew->first, itnew->second);
			} else {
				itnew->second = max(it->second, itnew->second);
				//printf("#2 i=%d: it=(%d,%d) itnew=(%d,%d)\n", i, it->first, it->second, itnew->first, itnew->second);
			}
		}

//		for (it=M[i].begin(); it!=M[i].end(); it++)
//			cerr << i << ": " << it->first << " " << it->second << endl;
	}

	if (M[n-1].find(sum) == M[n-1].end())
		return -1;
	else
		return M[n-1][sum];
}

void all()
{
	int i, c;

	ans=-1;
	for(i=1; i<=n; i++) {
		swap(A[i], A[n]);

		c = solve(A[n]);
		cerr << "Answer #" << i << ": " << c << endl;
		if (c>ans) ans=c;
		
		swap(A[i], A[n]);
	}
}

void output(int t)
{
	printf("Case #%d: ", t);

	if (S || ans<=0) printf("NO\n");
	else printf("%d\n", ans);
}

int main()
{
	int i, t;
	scanf("%d", &t);

	for(i=1; i<=t; i++) {
		input();
		all();
		output(i);
	}
	
	return 0;
}
