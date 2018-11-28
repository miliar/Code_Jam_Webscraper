#include <iostream>

using namespace std;

int main()
{
	int t, n, l, h, temp;
	bool solved, works;
	int* sounds;

	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ": ";
		cin >> n >> l >> h;
		sounds = new int[n];
		for(int j = 0; j < n; j++)
		{
			cin >> sounds[j];
		}
		solved = false;
		for(int k = l; k <= h; k++)
		{
			works = true;
			for(int m = 0; m < n; m++)
			{
				if(k % sounds[m] != 0 && sounds[m] % k != 0)
				{
					works = false;
					break;
				}
			}
			if(works)
			{
				solved = true;
				cout << k << endl;
				break;
			}
		}

		if(!solved)
		{
			cout << "NO" << endl;
		}
	}
}
			
