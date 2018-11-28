#include <iostream>
#include <fstream>
#include <string>
#include <cstring>

char map[55][55];

bool fill(int n, int i)
{
	if(map[n][i]=='#' && map[n+1][i]=='#' && map[n][i+1]=='#' && map[n+1][i+1]=='#')
	{
		map[n][i]='/';
		map[n][i+1]='\\';
		map[n+1][i]='\\';
		map[n+1][i+1]='/';
		return true;
	}
	else
	{
		return false;
	}
}



int main()
{
	std::ifstream in("square.in");
	std::ofstream out("square.out");
	
	
	int T;
	in >> T;
	for(int X=0; X<T; ++X)
	{
		out << "Case #" << X+1 << ":" << '\n';
		std::cout << "Case #" << X+1 << ":" << '\n';
		int R, C;
		in >> R;
		in >> C;
		memset(map, '.', sizeof(map));
		
		for(int n=0; n<R; ++n)
		{
			in.ignore(1, '\n');
			for(int i=0; i<C; ++i)
			{
				map[n][i]=in.get();
			}
		}
		
		for(int n=0; n<R; ++n)
		{
			for(int i=0; i<C; ++i)
			{
				std::cout << map[n][i];
			}
			std::cout << '\n';
		}
		std::cout << '\n';
		
		bool error=false;
		
		start:;
		
		for(int n=0; n<R; ++n)
		{
			for(int i=0; i<C; ++i)
			{
				if(map[n][i]=='#')
				{
					if(fill(n, i))
					{
						goto start;
					}
					else
					{
						error=true;
					}
				}
				if(error)
					break;
			}
			if(error)
				break;
		}
		
		if(error)
		{
			out << "Impossible" << '\n';
		}
		else
		{
			for(int n=0; n<R; ++n)
			{
				for(int i=0; i<C; ++i)
				{
					out << map[n][i];
				}
				out << '\n';
			}
		}
	}
}












