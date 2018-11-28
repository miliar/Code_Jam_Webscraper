#include<iostream>

template<class T>
T abs(T x) {return (x<0)?-x:x;}

int main()
{
	std::ios::sync_with_stdio(0);
	unsigned short T; std::cin >> T;
	for(unsigned short i = 0; i < T; i++)
	{
		unsigned short y = 0, N, b_p = 1, o_p = 1; short o_s = 0, b_s = 0;
		std::cin >> N;
		for(unsigned short i = 0; i < N; i++)
		{
			char c; std::cin >> c;
			unsigned short dist; std::cin >> dist;
			if(c == 'O')
			{
				short time = abs(dist-o_p)- o_s;
				if(time > 0)
				{
					y += time;
					b_s += time;
				}
				y++;
				b_s++;
				o_s = 0;
				o_p = dist;
				continue;
			}
			if(c == 'B')
			{
				short time = abs(dist-b_p) - b_s;
				if(time > 0)
				{
					y += time;
					o_s += time;
				}
				y++;
				o_s++;
				b_s = 0;
				b_p = dist;
				continue;
			}
		}
		std::cout << "Case #" << i+1 << ": " << y << '\n';
	}
	return 0;
}
