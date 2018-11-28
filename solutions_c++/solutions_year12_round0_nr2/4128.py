#include <iostream>

using namespace std;

int main()
{
	int t;
	int n;
	int s;
	int p;
	int googlers[100];
	int y;
	
	cin >> t;
	
	for (int i = 0; i < t; i++)
	{
		cin >> n;
		cin >> s;
		cin >> p;
		
		for (int j = 0; j < n; j++)
		{
			cin >> googlers[j];
		}
		
		y = 0;
		int s_remaining = s;
		
		for (int j = 0; j < n; j++)
		{
			int base_score = googlers[j] / 3;
			
			if (base_score >= p)
			{
				y++;
			}
			else
			{
				int adjust = googlers[j] % 3;
				
				if (adjust == 0)
				{
					if ((base_score + 1 >= p) &&
						(base_score >= 1) &&
						(s_remaining > 0))
					{
						y++;
						s_remaining--;
					}
				}				
				else if (adjust == 1)
				{
					if (base_score + 1 >= p)
					{
						y++;
					}
				}
				else if (adjust == 2)
				{
					if (base_score + 1 >= p)
					{
						y++;
					}
					else if ((base_score + 2 >= p) &&
							 (s_remaining > 0))
					{
						y++;
						s_remaining--;
					}
				}
			}
		}
		
		cout << "Case #" << i + 1 << ": " << y << '\n';
	}
}
