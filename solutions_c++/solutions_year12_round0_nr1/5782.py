#include <iostream>
#include <string>

std::string decode(std::string Gl)
{
	std::string Sl = Gl;
//		std::cout << "Sl = Gl done, length " << Sl.length() <<"\n";
	for(unsigned short i = 0; i < Sl.length(); i++)
	{
//		std::cout << "decode, iter " << i <<"\n";
		switch(Sl[i])
		{
			case 'a':
				Sl[i] = 'y';
				break;
			case 'b':
				Sl[i] = 'h';
				break;
			case 'c':
				Sl[i] = 'e';
				break;
			case 'd':
				Sl[i] = 's';
				break;
			case 'e':
				Sl[i] = 'o';
				break;
			case 'f':
				Sl[i] = 'c';
				break;
			case 'g':
				Sl[i] = 'v';
				break;
			case 'h':
				Sl[i] = 'x';
				break;
			case 'i':
				Sl[i] = 'd';
				break;
			case 'j':
				Sl[i] = 'u';
				break;
			case 'k':
				Sl[i] = 'i';
				break;
			case 'l':
				Sl[i] = 'g';
				break;
			case 'm':
				Sl[i] = 'l';
				break;
			case 'n':
				Sl[i] = 'b';
				break;
			case 'o':
				Sl[i] = 'k';
				break;
			case 'p':
				Sl[i] = 'r';
				break;
			case 'q':
				Sl[i] = 'z';
				break;
			case 'r':
				Sl[i] = 't';
				break;
			case 's':
				Sl[i] = 'n';
				break;
			case 't':
				Sl[i] = 'w';
				break;
			case 'u':
				Sl[i] = 'j';
				break;
			case 'v':
				Sl[i] = 'p';
				break;
			case 'w':
				Sl[i] = 'f';
				break;
			case 'x':
				Sl[i] = 'm';
				break;
			case 'y':
				Sl[i] = 'a';
				break;
			case 'z':
				Sl[i] = 'q';
				break;
			default:
				break;
		}
	}
	return Sl;
};

int main()
{
	short T;
	std::cin >> T;
	if( T<1 || T>30 ) { std::cout << "Error: 1 > T > 30"; return 1; };
	++T;
	std::string G[T];

	for(short X = 0; X<T; X++)
	{
//		std::cout << "1st for, iter " << X << "\n";
		std::getline(std::cin,G[X]);
	};

	std::string S[T];
	for(short X = 0; X<T; X++)
	{
//		std::cout << "2nd for, iter " << X <<"\n";
		S[X] = decode(G[X]);
	}

	for(short X = 1; X<T; X++)
	{
//		std::cout << "3rd for, iter " << X <<"\n";
		std::cout << "Case #" << X << ": " << S[X] << std::endl;
	};
	return 0;
}
