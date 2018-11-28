#include <iostream>

void DoTest()
{
	int n,s,p,Wyn=0;
	std::cin >> n >> s >> p;
	for (int i=0;i<n;i++)
	{
		int a;
		std::cin >> a;
		int divided=a/3;
		if (a%3==0)
		{
			if (divided>=p)
				Wyn++;
			else
			{
				if (s && divided && divided+1>=p)
				{
					s--;
					Wyn++;
				}
			}
		} else if (a%3==1)
		{
			if (divided+1 >= p)
				Wyn++;
			else
			{
				if (s && divided+1>=p)
				{
					s--;
					Wyn++;
				}
			}
		} else // a%3 == 2
		{
			if (divided+1 >= p)
				Wyn++;
			else
			{
				if (s && divided+2>=p)
				{
					s--;
					Wyn++;
				}
			}
		}
	}
	std::cout << Wyn << '\n';
}

int main()
{
	std::ios::sync_with_stdio(0);
	std::cin.tie(NULL);
	int t;
	std::cin >> t;
	for (int i=1;i<=t;i++)
	{
		std::cout << "Case #" << i << ": ";
		DoTest();
	}
}