#include "Slarbo.hpp"


int Slarbo::PGCD(int a, int b)
{
    return (b)?PGCD(b, a%b):a;
}


int main()
{
	Slarbo s;

	s.processFile("B.in");
}