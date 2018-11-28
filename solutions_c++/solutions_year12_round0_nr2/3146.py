#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int N;
		int S;
		int p;
		int point[100];
		int rs = 0;
		cin >> N >> S >> p;
		for (int j = 0; j < N; ++j)
		{
			cin >> point[j];
			int avg = point[j] / 3;
			int last = point[j] % 3;
			if (last == 0){
				if (avg >= p)
				rs++;
				else {
					if (avg+1 >= p)
						if (S > 0 && avg-1 >= 0){
							rs++;
							S--;
						}
				}
			}
			else if (last == 1){
				if (avg+1 >= p)
				rs++;
			}
			else {
				if (avg+1 >= p)
				rs++;
				else {
					if (avg+2 >= p)
						if (S > 0)
						{
							rs++;
							S--;
						}
				}
			}
		}
		cout << "Case #" << i+1 << ": " << rs << endl;
	}
	return 0;
}
