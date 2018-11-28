#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <cstring>
#include <ctype.h>
#include <map>


#define inputfilename "a_4.in"
#define outputfilename "a_4.out"

using namespace std;

map <string , int> a;
vector<int> q;
int times, number;
int dp[1005][1005];
int n , m;

int search(int depth , int pos)
{
	if (depth >= m) return 0;
	if (dp[depth][pos] != -1) return dp[depth][pos];
	//if (q[depth] == pos) { dp[depth][pos] = -2; continue;}
	int j , k;
	for (j = depth+1; j < m ; j++)
	{
		if (q[j] == pos) break;
	}
	int res = m+1;
	if (j == m) res = 0;
	else
	{
		for (k = 0 ;k < n ; k++)
		{
			if (k == pos) continue;
			int r =  search(j , k )+1;
			res = min(res, r);
		}
	}
	dp[depth][pos] =res;
	return res;
}

int main ()
{
	freopen(inputfilename , "r" , stdin);
	freopen(outputfilename , "w" , stdout);
	
	cin >> number;
	for (times = 0 ;times < number ; times++)
	{
		a.clear();
		q.clear();
		cin >> n ;
		int i ;
		char buf[200];
		getchar();
		for(i = 0; i< n ; i++)
		{
			gets(buf);
	
	//		cout << "&&& " << buf << endl;
	
			a[buf] = i;
		}
		cin >> m;
		getchar();
		if (m ==0){ printf("Case #%d: 0\n" , times+1); continue;}
	
		for (i = 0; i < m ; i++)
		{
			gets(buf);
		
	//		cout << "--- " << buf << endl;
			int p;
			if (a.find(buf) == a.end()) p = -1;
			else p = a[buf];
			q.push_back(p);
		}
		memset(dp , -1 , sizeof(dp));
		int res = m+1;
		
		for (i = 0; i < n ; i++)
		{
			if (i == q[0]) continue;
			int r = search(0, i);
			res = min(res, r);
		}
		printf("Case #%d: %d\n" , times+1 ,res);


	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}

 
