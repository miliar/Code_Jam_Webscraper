#include <iostream>

using namespace std;

int main()
{
	static const int MAX_ROTATIONS = 6;

	int T;
	cin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int A, B;
		cin >> A >> B;
		
		int nRotations = -1;
		for (int a = A; a; a /= 10, nRotations++);

		int exp = 1;
		for (int i = 0; i < nRotations; i++)
			exp *= 10;

		int found[MAX_ROTATIONS];
		int nFound = 0;

		int y = 0;

		for (int n = A; n < B; n++)
		{
			found[0] = n;
			nFound = 1;

			int rot = n;
			for (int nRot = 0; nRot < nRotations; nRot++)
			{
				rot = rot / 10 + (rot % 10) * exp;

				if (rot <= n || rot > B)
					continue;

				int i;
				for (i = 0; i < nFound; i++)
					if (found[i] == rot)
						break;
				if (i < nFound)
					continue;

				y++;
				found[nFound++] = rot;
			}
		}

		cout << "Case #" << nTestCase << ": " << y << endl;
	}
}
