#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

ifstream in("C.in");
ofstream out("C.txt");

bool game (int A, int B)
{
	if (A==B)
		return false;
	else
	{
		if (A/B >= 2)
			return true;
		else
			return (!game(B, A-B));
	}
}

int main()
{
	int T;
	in>>T;
	for (int t=1; t<=T; t++)
	{
		int A1, A2, B1, B2;
		in>>A1>>A2>>B1>>B2;
		
		long long winning = 0;
		for (int A=A1; A<=A2; A++)
		{
			for (int B=B1; B<=B2; B++)
			{
				if (A < B)
				{
					if (game (B, A))
						winning++;
				}
				else
				{
					if (game (A, B))
						winning++;
				}
			}
		}
		out<<"Case #"<<t<<": "<<winning<<endl;
	}
    return 0;
}
