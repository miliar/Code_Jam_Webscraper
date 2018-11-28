/**
	Written by Gaurav Ahuja
	gauravahuja9@gmail.com
**/


#include <iostream>
#include <cstdio>

namespace IO
{
	const int SIZE = 1 << 20;
	char buff[SIZE], *p = buff + SIZE;

	inline char read_char()
	{
	    if( p == buff + SIZE )
	    {
	        fread( buff, 1, SIZE, stdin );
	        p = buff;
	    }
	    return *(p++);
	}

	inline int read_int()
	{
	    char c;
	
	    while( !isdigit( c = read_char() ) );
	
	    int r = c-'0';
	    while( isdigit( c = read_char() ) ) r = 10*r + c - '0';

	    return r;
	}
}

using namespace IO;
using namespace std;

inline int calcbss(int ti, int &bs, int &bss)
{
	if(ti == 0)
	{
		bs = 0;
		bss = 0;
		return 0;
	}
	int mod = ti%3;
	if(mod == 1)
	{
		bs = ti/3 +1;
		bss = bs;
	}
	else if(mod == 0)
	{
		bs = ti/3;
		bss = bs + 1;
	}
	else
	{
		bss = ti/3 + 2;
		bs = bss - 1;
	}
	return 0;
}
int main()
{
	int t, td = 1;
	t = read_int();
	
	int n, s, p, ti;
	int bs, bss;
	int count;
	while(td <= t)
	{
		bs = 0;
		bss = 0;
		count = 0;
		n = read_int();
		s = read_int();
		p = read_int();
		for(int i = 0; i < n; i++)
		{
			ti = read_int();
			
			calcbss(ti, bs, bss);

			if (bss < p)
			{
			}
			else if(bs >= p)
			{
				count++;
			}
			else //if(bss == p)
			{
				if(s)
				{
					s--;
					count++;
				}
			}
		}
		printf("Case #%d: %d\n", td, count);
		td++;
	}
		
	return 0;
}
