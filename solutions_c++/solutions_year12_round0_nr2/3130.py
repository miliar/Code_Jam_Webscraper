#include <windows.h>
#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <math.h>
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
typedef long s32;
typedef unsigned long u32;


int main(int argc, char* argv[])
{

    HANDLE hStdin = GetStdHandle(STD_INPUT_HANDLE); 
    DWORD mode = 0;
    GetConsoleMode(hStdin, &mode);
    SetConsoleMode(hStdin, mode & (~ENABLE_ECHO_INPUT));

	u32 T,S,N,p;
	u32 ii,jj;

	u32 total_points, current_best, beat_best;
	boolean allow_surprise;

	cin >> T;

	for(ii =0 ; ii < T; ii++)
	{
		cin >> N >> S >> p;

		beat_best = 0;

		for(jj=0; jj<N; jj++)
		{
			cin >> total_points;

			allow_surprise = TRUE;
			current_best = total_points / 3;
			if (total_points % 3 != 0 )
			{
				if (total_points % 3 == 1 )
					allow_surprise = FALSE;
				current_best++;
			}
			if ( ( total_points < 2) || (total_points > 28) )
				allow_surprise = FALSE;

			if(current_best >= p)
			{
				beat_best++;
			}
			else if ( ( S ) && (allow_surprise) && (current_best == p - 1) )
			{
				S--;
				beat_best++;
			}			
		}

		cout << "Case #" << ii + 1 << ": " << beat_best << endl;
	}

}