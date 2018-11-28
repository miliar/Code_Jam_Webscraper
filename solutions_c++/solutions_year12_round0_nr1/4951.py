#include <iostream>
#include <string>

char Tab[]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

void DoTest()
{
	std::string L;
	std::getline(std::cin, L);
	for (int i=0;i<L.size();i++)
	{
		if (L[i]!=' ')
			L[i]=Tab[L[i]-'a'];
	}
	std::cout << L << '\n';
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	int t;
	std::cin >> t;
	std::cin.get();
	for (int i=1;i<=t;i++)
	{
		std::cout << "Case #" << i << ": ";
		DoTest();
	}
}