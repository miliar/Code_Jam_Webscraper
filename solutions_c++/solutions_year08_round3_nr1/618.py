#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve()
{
    int P, K, L;
    cin >> P >> K >> L;
    vector<int> a(L,0);
    for(int i=0; i<L; i++)
	cin >> a[i];
    sort(a.begin(), a.end());
    reverse(a.begin(), a.end());

    if(P*K < L)
	return -1;

    int result = 0;
    for(int i=0; i<L; i++)
	result += (i/K+1)*a[i];
    return result;
}

int main()
{
    int N;
    cin >> N;
    for(int i=1; i<=N; i++) {
	int r = solve();
	if(r!=-1)
	    cout << "Case #" << i << ": " << r << endl;
	else
	    cout << "Case #" << i << ": " << "Impossible" << endl;
    }
    return 0;
}
