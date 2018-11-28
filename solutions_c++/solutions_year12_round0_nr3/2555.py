#include "iostream"

int num_digits(int i)
{
	int number_of_digits = 0;
	while(i > 0)
	{
		i/=10; ++number_of_digits;
	}

	return number_of_digits;
}

int int_power(int base, int exponent)
{
	int exponentiation = 1;

	for (int i = 0; i < exponent; ++i)
		exponentiation*=base;
	return exponentiation;
}

int rotations_inside(int lower_bound, int upper_bound)
{
	int number_satisfy_constraint = 0;
	for (int itr = lower_bound; itr <= 2000000; ++itr)
		{
			int rotations_of_itr[7];
			int num_length = num_digits(itr);
			for (int i = 0; i < num_length; ++i) // perform the rotations
			{
				int bottom_digits = itr % int_power(10,i+1);
				int top_digits = itr / int_power(10,i+1);
				rotations_of_itr[i] = top_digits + (bottom_digits*int_power(10,num_length-(i+1)));

				if ((rotations_of_itr[i] > itr) and (rotations_of_itr[i] <= upper_bound))
				{
					bool no_duplicates = true;
					for (int j = 0; j < i; ++j) // Check for duplicates
					{
						if (rotations_of_itr[j] == rotations_of_itr[i]) no_duplicates = false;
					}

					if (no_duplicates)
						++number_satisfy_constraint;
				}

			}
		}
	return number_satisfy_constraint;
}

int main()
{
	int test_number = 0;

	std::cin >> test_number;
	std::cin.ignore(1,'\n');

	for (int test_case = 0; test_case < test_number; ++test_case)
	{
		std::cout << "Case #" << test_case+1 << ": ";
		int lower_bound, upper_bound;
		std::cin >> lower_bound >> upper_bound;
		std::cout << rotations_inside(lower_bound,upper_bound) << std::endl;
	}
}