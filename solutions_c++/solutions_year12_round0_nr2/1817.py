#include <map>
#include <string>
#include <iostream>

using namespace std;

int getp(int t)
{
    if (t == 0)
        return 0;
    else
        return (t + 2) / 3;
}

int getsp(int t)
{
    if (t <= 1)
        return t;
    else
        return (t + 4) / 3;
}

int main()
{
	int T, N, S, p;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cin >> N >> S >> p;
		int y = 0;
		for (int j = 0; j < N; ++j)
		{
			int t;
			cin >> t;

			if (getp(t) >= p)
				y++;
			else if (getsp(t) >= p && --S >= 0)
				y++;
		}
		cout << "Case #" << i + 1 << ": " << y << endl;
	}
}
