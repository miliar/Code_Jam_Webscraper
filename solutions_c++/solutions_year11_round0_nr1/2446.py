#include <iostream>

using namespace std;

int botid(char bot)
{
	return bot=='O' ? 0 : 1;
}

int abs(int a)
{
	return a>=0 ? a : -a;
}

int main(int argc, char ** argv, char ** env)
{
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t)
	{
		int N, lastbot=2, lastmoves=0, totmoves=0, 
		    botpos[2] = {1, 1};
		cin >> N;
		for(int n=0; n<N; ++n) {
			char B;
			int p, b, m;
			cin >> B >> p;
			b = botid(B);
			m = abs(p-botpos[b]);
			botpos[b] = p;
			if(lastbot == b)
			{
				lastmoves += m + 1;
				totmoves += m + 1;
			}
			else
			{
				int md = m>lastmoves ? m-lastmoves : 0;
				totmoves += md + 1;
				lastbot = b;
				lastmoves = md+1;
			}
		}

		cout << "Case #" << t << ": " << totmoves << endl;
	}
	return 0;
}
