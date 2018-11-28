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


#define MAX_STRING_SIZE 7
char string_a[MAX_STRING_SIZE];
char string_b[MAX_STRING_SIZE];

void rotate_once(char *buf)
{
	char end;
	u32 ii;

	ii = strlen(buf) -1;
	end = buf[ii];
	for(; ii > 0; ii--)
	{
		buf[ii] = buf[ii-1];
	}
	buf[0] = end;
}


int main(int argc, char* argv[])
{
    HANDLE hStdin = GetStdHandle(STD_INPUT_HANDLE); 
    DWORD mode = 0;
    GetConsoleMode(hStdin, &mode);
    SetConsoleMode(hStdin, mode & (~ENABLE_ECHO_INPUT));

	u32 T;
	u32 A, B;
	u32 n, m;
	u32 length;
	boolean result_found;
	u32 pair_count;
	u32 ii;

	cin >> T;

	for (int t=0; t < T; t++) {

		cin >> A >> B;
		sprintf_s(string_a, "%u", A);
		length = strlen(string_a);
		pair_count = 0;

		for( n = A; n < B; n ++ )
		{
			for( m = B; m > n ; m--)
			{
				sprintf_s(string_a, "%u", n);
				sprintf_s(string_b, "%u", m);
				result_found = FALSE;
				for(ii = 0; (ii < length) && (!result_found); ii++ )
				{
					rotate_once(string_a);
					if(strcmp(string_a,string_b) == 0)
					{
						pair_count++;
						result_found = TRUE;
					}
				}
			}
		}

		cout << "Case #" << (t+1) << ": " << pair_count << endl;
	}


    return 0;
}


