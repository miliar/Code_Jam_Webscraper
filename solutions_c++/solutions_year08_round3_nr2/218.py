#include <string>
#include <iostream>
using namespace std;
string s;
long long int arr[40];
long long int size;
long long int ans;
long long int get_number(int f, int t)
{
	long long int ans = 0, mn = 1;
	for (int i = t; i>=f; i--)
	{
		ans+=arr[i]*mn;
		mn*=10;
	}
//	cout << s << " " << f << " " << t << " " << ans << endl;
	return ans;
}

void rec(long long int n, long long int sum)
{
	if (n==size)
	{
		if (sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0)
			ans++;
			
		return;
	}
	for (int j = n; j<=size; j++)
	{
		rec(j+1,sum + get_number(n, j));
		rec(j+1,sum - get_number(n, j));
	}
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int N,testcase;
	cin >> N;
	for(testcase=1; testcase<=N; testcase++)
	{
		cin >> s;
		size = s.length();
		for (int i=0; i<size; i++)
			arr[i] = s[i]-'0';
		ans = 0;
		rec(0,0);
		cout << "Case #" << testcase << ": " << ans/2 << endl;
	}
	return 0;
}
