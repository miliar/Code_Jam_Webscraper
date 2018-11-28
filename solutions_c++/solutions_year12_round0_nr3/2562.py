#include <iostream>
#include <cmath>
#include <fstream>
#include <set>

size_t count_digits(size_t a)
{
	size_t div = 10;
	size_t len_a = 0;
	for (size_t nz = 1; nz < 8; ++ nz)
	{
		if (a % div == a)
		{
			len_a = nz;
			break;
		}
		div *= 10;
	}
	return len_a;
}
size_t process_case(size_t a, size_t b)
{
	std::set<std::pair<size_t, size_t> > uniq_pairs;
	size_t k = 0;
	size_t len_a = count_digits(a);

	for (size_t n = a; n < b; ++ n)
	{
		size_t div = 10;
		for (size_t nz = 1; nz < len_a; ++ nz)
		{
			size_t terminal = n % div;
			if (terminal == n)
				break;
			size_t prefix = (n / div);
			size_t m = (terminal * pow(10, len_a - nz)) + prefix;
			//std::cerr << "rotation : " << len_a << " " << n << " " << m << std::endl;
			if ((m > n) && (m <= b)) 
			{
				std::pair<size_t, size_t> mn = std::make_pair(m, n);
				if (uniq_pairs.find(mn) == uniq_pairs.end())
				{
					uniq_pairs.insert(mn);
					++ k;
				}
				else
				{
//std::cerr << "rejecting " << m << " " << n << std::endl;
				}
			}
			div *= 10;
		}
	}
	return k;
}

int main(int argc, char** argv)
{
	std::ifstream infile(argv[1]);
	std::ofstream outfile(argv[2]);

	size_t ncases;
	infile >> ncases;
	size_t A, B;
	for (size_t idx = 0; idx < ncases; ++ idx)
	{
		infile >> A >> B;
		size_t res = process_case(A, B);
		outfile << "Case #" << (idx + 1) << ": " << res << std::endl;
	}
	outfile.close();
	infile.close();
}
