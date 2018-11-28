#include <iostream>
#include <fstream>

using namespace std;

const char BLUE = 'B';
const char ORANGE = 'O';
const int MAX_N = 100;

int N, T;

struct Button
{
	char robot;
	int place;
};

Button B[MAX_N];

int dest(char c, int now)
{
	for(int i=now; i<N; i++)
	{
		if(B[i].robot == c)
		{
			return B[i].place;
		}
	}
	
	return -1;
}

int solve()
{
	int now = 0;
	int oPos = 1;
	int bPos = 1;
	int oDst = dest(ORANGE, now);
	int bDst = dest(BLUE, now);
	char turn = B[0].robot;
	int sec = 0;
	while( 1 )
	{
		if(oDst == -1 && bDst == -1)
		{
			break;
		}

		sec++;
		turn = B[now].robot;

		if(oDst != -1)
		{
			if(oDst < oPos)
				oPos--;
			else if(oDst > oPos)
				oPos++;
			else if(oDst == oPos && turn == ORANGE)
			{
				now++;
				oDst = dest(ORANGE, now);
			}
		}

		if(bDst != -1)
		{
			if(bDst < bPos)
				bPos--;
			else if(bDst > bPos)
				bPos++;
			else if(bDst == bPos && turn == BLUE)
			{
				now++;
				bDst = dest(BLUE, now);
			}
		}
	}

	return sec;
}


int main()
{
	ifstream ifs("C:\\Users\\Tatsuya\\Desktop\\codejam\\input", ios::in);
	ofstream ofs("C:\\Users\\Tatsuya\\Desktop\\codejam\\output", ios::out);
		
	ifs >> T;
	for(int t=0; t<T; t++)
	{
		ifs >> N;
		for(int n=0; n<N; n++)
		{
			ifs >> B[n].robot;
			ifs >> B[n].place;
		}

		int res = solve();
		ofs << "Case #" << t+1 << ": " << res << endl;
	}
}
