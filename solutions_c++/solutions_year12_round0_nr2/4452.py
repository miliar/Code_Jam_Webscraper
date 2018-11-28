#include <cstdlib>
#include <iostream>

using namespace std;

int
main ()
{
	int T;
	int N, S, p;
	
	cin >> T;
	
	for (int t = 1; t <= T; t++)
	{
		int tot = 0;
		int x;
		
		cin >> N >> S >> p;
		
		while (N--)
		{
			cin >> x;
			
			if (x%3 == 0) {
				if (x/3 >= p) {
					tot++;
				} else if (S > 0 && x >= 3 && x/3 == p-1) {
					tot++;
					S--;
				}
			} else if (x%3 == 1) {
				if ((x+2)/3 >=p) {
					tot++;
				}
			} else {
				if ((x+1)/3 >= p) {
					tot++;
				} else if (S > 0 && x >= 2 && (x+1)/3 == p-1) {
					tot++;
					S--;
				}
			}
		}
		
		cout << "Case #" << t << ": " << tot << endl;
	}
	
	return EXIT_SUCCESS;
}
