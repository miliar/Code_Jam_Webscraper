#include <iostream>

using namespace std;

int main()
{
	int numCase;
	cin >> numCase;

	int i, j;
	long long N, M, A, y2, x2, x3, y3;
	for (i = 0; i < numCase; i++)
	{
		cin >> N >> M >> A;
        j = 0;
		for (x2 = 0; x2 <= N; x2++)
		{
            for (y2 = 0; y2 <= M; y2++)
                if ( x2 + y2 > 0)
                {
                    for (x3 = 0; x3 <= N; x3++)
                    {
                        for (y3 = 0; y3 <= M; y3++)
                            if (!((x2==x3)&&(y2==y3)) && (x3+y3>0))
                            {
                                if (x2*y3 - x3*y2== A)
                                {cout << "Case #" << (i+1) << ": 0 0 " << x2 << " " << y2 << " " << x3 << " " << y3 << endl; j=1; break;}

                                if (j==1) break;
                            }
                    if (j==1) break;
                    }
                if (j==1) break;
                }
            if (j==1) break;
		}

        if (j == 0)
            cout << "Case #" << (i+1) << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
