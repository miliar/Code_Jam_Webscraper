#include <fstream>
using namespace std;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int N;
	cin >> N;
	for (int tc = 1; tc <= N; tc++)
	{
		int n, s, p, score;
		cin >> n >> s >> p;
		
		int nValid = 0;
		int nCanValidate = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> score;
			nValid += ((score % 3 == 0 && score / 3 >= p) || (score % 3 != 0 && score / 3 + 1 >= p));
			if (score != 0)
			{
				nCanValidate += ((score % 3 == 0 && score / 3 + 1 == p) || (score % 3 == 2 && score / 3 + 2 == p));
			}
		}

		cout << "Case #" << tc << ": " << nValid + min(s, nCanValidate)  << endl;
	}
	return 0;
}