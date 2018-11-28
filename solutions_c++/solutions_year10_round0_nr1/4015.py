#include<iostream>
#include<stdio.h>
inline bool test(int a,int b);

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out-large1.txt","w",stdout);
	int n = 0;
	std::cin >> n;
	int i = 1, a,b;
	while(i <= n)
	{

		std::cin >> a >> b;

		std::cout << "Case #" << i ;
		if(test(a,b))
			std::cout << ": ON" ;
		else
			std::cout << ": OFF";

		std::cout << std::endl;
		i += 1;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}


inline bool test(int a,int b)
{
	int k = 1;
	while(a)
	{
		k *= 2;
		a -= 1;
	}
	return ((b%k)==(k-1))?true:false;
}