#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <cstring>
#include <set>
using namespace std;

#define rev(x) reverse((x).begin(), (x).end())
#define sor(x) sort(x.begin(), x.end())
#define sz size()
#define pb push_back
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define ll long long
#define fill(var,val) memset(var, val, sizeof(var))
#define rep(i, n) for(i = 0; i < n; i++)
#define repa(i, a, n) for(i = a; i < n; i++)
#define s(n) scanf("%d", &n);
#define p(n) printf("%d\n", n);

int arr[1010];
int n;
int decimal_sum, xor_sum;

int main()
{
	int t, i, k = 0;
	s(t);
	
	while(t--)
	{
		k++;
		s(n);
		decimal_sum = 0; xor_sum = 0;
		int smallest = 10000000;
		rep(i, n)
		{
			s(arr[i]); 
			decimal_sum += arr[i];
			xor_sum ^= arr[i];
			smallest = min(smallest, arr[i]);
		}
		
		
		cout << "Case #" << k << ": ";
		if(xor_sum != 0) { cout << "NO" << endl; continue; }
		else cout << decimal_sum - smallest << endl;
	}
	return 0;
}
