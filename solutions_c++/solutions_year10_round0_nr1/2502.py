#include <iostream>

int main()
{
    int t;
    std::cin >> t;
    for(int i = 1; i<= t; ++i)
    {
	int n, k;
	std::cin >> n;
	std::cin >> k;
	
	if((k&((1<<n)-1))==((1<<n)-1))
	    std::cout << "Case #" << i << ": " << "ON" << std::endl;
	else
	    std::cout << "Case #" << i << ": " << "OFF" << std::endl;
    }

    return 0;
}
