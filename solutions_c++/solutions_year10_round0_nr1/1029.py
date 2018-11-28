#include <iostream>

using namespace std;

inline unsigned long long f(unsigned n)
{
    return n == 1 ? 1 : 1 + 2 * f(n - 1);
}

int main()
{
    unsigned T, c = 0;
    while (cin >> T)
    {
	while (T--)
	{
	    unsigned N;
	    unsigned long long K;
	    cin >> N >> K;
	    //cout << "f(" << N << ") = " << f(N) << endl;
	    cout << "Case #" << (++c) << ": " 
		 << ((K % (f(N) + 1)) == f(N) ? "ON" : "OFF") 
		 << endl;
	}
    }
    return 0;
}
