#include<iostream>
#include<string>

std::string foo(std::string input)
{
	std::string out = input;
	for(int i=0;i<input.length();i++)
	{
		switch(input[i])
		{
		case 'y':
			out[i] = 'a';
			break;
		case 'n':
			out[i] = 'b';
			break;
		case 'f':
			out[i] = 'c';
			break;
		case 'i':
			out[i] = 'd';
			break;
		case 'c':
			out[i] = 'e';
			break;
		case 'w':
			out[i] = 'f';
			break;
		case 'l':
			out[i] = 'g';
			break;
		case 'b':
			out[i] = 'h';
			break;
		case 'k':
			out[i] = 'i';
			break;
		case 'u':
			out[i] = 'j';
			break;
		case 'o':
			out[i] = 'k';
			break;
		case 'm':
			out[i] = 'l';
			break;
		case 'x':
			out[i] = 'm';
			break;
		case 's':
			out[i] = 'n';
			break;
		case 'e':
			out[i] = 'o';
			break;
		case 'v':
			out[i] = 'p';
			break;
		case 'z':
			out[i] = 'q';
			break;
		case 'p':
			out[i] = 'r';
			break;
		case 'd':
			out[i] = 's';
			break;
		case 'r':
			out[i] = 't';
			break;
		case 'j':
			out[i] = 'u';
			break;
		case 'g':
			out[i] = 'v';
			break;
		case 't':
			out[i] = 'w';
			break;
		case 'h':
			out[i] = 'x';
			break;
		case 'a':
			out[i] = 'y';
			break;
		case 'q':
			out[i] = 'z';
			break;
		default:
			break;
		}
	}
	return out;
}


int main()
{
	int T;
	std::string in;
	std::cin>>T;
	std::getline(std::cin,in);
	for(int i=1;i<=T;i++)
	{
		std::getline(std::cin,in);
		std::cout<<"Case #"<<i<<": "<<foo(in)<<std::endl;
	}
}