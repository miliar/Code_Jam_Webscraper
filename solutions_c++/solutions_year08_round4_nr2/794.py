#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
	unsigned int num_casos;

	cin >> num_casos;
	for(unsigned int c = 1; c <= num_casos; c++)
	{
		long long int N, M, A;
		bool found = false;
		cin >> N >> M >> A;

		if(N * M < A) cout << "Case #" << c << ": IMPOSSIBLE" << endl;
		else
		{
			for(int ax = 0; ax <= N; ax++)
			{
				for(int ay = 0; ay <= M; ay++)
				{
					for(int bx = 0; bx <= N; bx++)
					{
						for(int by = 0; by <= M; by++)
						{
							for(int cx = 0; cx <= N; cx++)
							{
								for(int cy = 0; cy <= M; cy++)
								{
									if(abs(ax*by - ay*bx + ay*cx - ax*cy + bx*cy - cx*by) == A)
									{
										cout << "Case #" << c << ": " << ax << " " << ay << " " << bx << " " << by << " " << cx << " " << cy << " " << endl;
										found = true;
										break;
									}
									if(found) break;
								}
								if(found) break;
							}
							if(found) break;
						}
						if(found) break;
					}
					if(found) break;
				}
				if(found) break;
			}
			if(!found) cout << "Case #" << c << ": IMPOSSIBLE" << endl;
		}
	}
}
