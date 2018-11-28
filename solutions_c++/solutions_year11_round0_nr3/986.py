#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstdlib>
using namespace std;

typedef string answer_type;

string itoa(int a)
{
    stringstream ss;
    ss << a;
    string str;
    ss >> str;
    return str;
}

answer_type solve()
{
	int n;
	cin >> n;
	int best = -1;
	int A[1005];
	int xsum = 0, sum = 0;
	for (int i = 0; i < n; i++)
		cin >> A[i], xsum ^= A[i], sum += A[i];;
	sort(A, A + n);
	if (xsum != 0)
		return "NO";
	
	return itoa(sum - A[0]);
}

int main()
{
	int T;
	cin >> T;
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
