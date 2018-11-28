#include <iostream>
#include <vector>
using namespace std;

const int O = 0;
const int B = 1;

int main()
{
	int T;
	cin>>T;

	for(int i = 0; i < T; ++i)
	{
		int N;
		cin>>N;

		int pos[2];
		pos[O] = pos[B] = 1;
		int t = 0;
		int extra = 0;
		char prev = 0;
		for(int j = 0; j < N; ++j)
		{
			char R;
			int P;
			cin>>R>>P;

			if(R == 'O')
			{
				if(pos[O] == P) // stay
				{
					t += 1;
					extra = 1;
				}
				else // move and push
				{
					int tmp = abs(pos[O]-P) + 1;
					if(prev != R)
					{
						if(extra < tmp) 
						{
							t += tmp-extra; // move & push
							extra = tmp-extra;
						}
						else
						{
							t += 1; // push
							extra = 1;
						}
					}
					else // can't use extra
					{
						extra += tmp;
						t += tmp;
					}
					pos[O] = P;
				}
				prev = R;
			}
			else
			{
				if(pos[B] == P) // stay
				{
					t += 1;
					extra = 1;
				}
				else
				{
					int tmp = abs(pos[B]-P) + 1;

					if(prev != R)
					{
						if(extra < tmp)
						{
							t += tmp - extra;
							extra = tmp - extra;
						}
						else
						{
							t += 1;
							extra = 1;
						}
					}
					else
					{
						extra += tmp;
						t += tmp;
					}

					pos[B] = P;
					
				}
				prev = R;
			}
		}

		cout<<"Case #"<<i+1<<": "<<t<<endl;
	}

	return 0;
}