#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>

int power = 0;

inline int permut(int n)
{
    return n/10 + (n%10)*power;
}

int main()
{
	int T, A, B;
	std::ifstream file("test.txt");
	std::ofstream file2("result.txt");

	file >> T;
	for(int it = 0; it < T; ++it)
	{
		file >> A;
		file >> B;
		int n = (int) log10(A);
		power = (int) pow(10,n);
		int ret = 0;

		for (int i = A; i < B; ++i)
		{
		    int k = i;
            for(int j = 0; j < n; j++)
            {
                k = permut(k);
                if (k == i)
                    break;

                if (k > i && k <= B )
                    ++ret;
            }
		}

		file2 << "Case #" << it+1 << ": " << ret << std::endl;
	}
	return 0;
}
