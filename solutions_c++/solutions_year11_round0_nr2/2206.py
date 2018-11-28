#include<iostream>

template<class T>
T abs(T x) {return (x<0)?-x:x;}

char id(char in)
{
	switch(in)
	{
		case'Q':return 0;break;
		case'W':return 1;break;
		case'E':return 2;break;
		case'R':return 3;break;
		case'A':return 4;break;
		case'S':return 5;break;
		case'D':return 6;break;
		case'F':return 7;break;
		default:return -1;break;
	}
}

int main()
{
	std::ios::sync_with_stdio(0);
	unsigned short T; std::cin >> T;
	for(unsigned short i = 0; i < T; i++)
	{
		char tab[8][8];
		for(char i = 0; i < 8; i++)
			for(char j = 0; j < 8; j++)
				tab[i][j] = 0;
		unsigned short C; std::cin >> C;
		for(unsigned short i = 0; i < C; i++)
		{
			char x,y,z; std::cin >> x >> y >> z;
			char xi = id(x), yi = id(y);
			tab[xi][yi] = z; tab[yi][xi] = z;
		}
		unsigned short D; std::cin >> D;
		for(unsigned short i = 0; i < D; i++)
		{
			char x,y; std::cin >> x >> y;
			char xi = id(x), yi = id(y);
			if(tab[xi][yi])
			{
				tab[xi][yi] *= -1;
				tab[yi][xi] *= -1;
			}
			else
				tab[xi][yi] = tab[yi][xi] = -1;
		}
		unsigned short N; std::cin >> N;
		char obecne[8];for(char i = 0; i < 8; i++) obecne[i] = 0;
		char len = 0, *tekst = new char[N+1]; tekst[0] = 0;
		for(unsigned short i = 0; i < N; i++)
		{
			char el; std::cin >> el;
			tekst[len++] = el; obecne[id(el)]++;
			if(len == 1) continue;
			char eli = id(el), pi = id(tekst[len-2]);
			if(pi > -1 && tab[eli][pi] && tab[eli][pi] != -1)
				{tekst[--len-1] = abs(tab[eli][pi]);obecne[eli]--;obecne[pi]--;continue;}
			bool clear = 0;
			for(char i = 0; i < 8; i++)
				if(obecne[i]>0 && tab[eli][i] < 0)
				{
					clear = true; break;
				}
			if(clear)
			{
				for(char i = 0; i < 8; i++) obecne[i] = 0; len = 0;
			}
		}
		std::cout << "Case #" << i+1 << ": [";
		for(char i = 0; i < len-1; i++)
			std::cout << tekst[i] << ", ";
		if(len) std::cout << tekst[len-1];
		std::cout << "]\n";
		delete[] tekst;
	}
	return 0;
}
