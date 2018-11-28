#include <iostream>

int main()
{
	int tests;
	std::cin >> tests;
	
	for (int testcase = 1; testcase <= tests; testcase++)
	{
		int answer = 0;
		int input;
		std::cin >> input;
		switch (input)
		{
			case 2: answer = 1; break;
			case 3: answer = 2; break;
			case 4: answer = 3; break;
			case 5: answer = 5; break;
			case 6: answer = 8; break;
			case 7: answer = 14; break;
			case 8: answer = 24; break;
			case 9: answer = 43; break;
			case 10: answer = 77; break;
			case 11: answer = 140; break;
			case 12: answer = 256; break;
			case 13: answer = 472; break;
			case 14: answer = 874; break;
			case 15: answer = 1628; break;
			case 16: answer = 3045; break;
			case 17: answer = 5719; break;
			case 18: answer = 10780; break;
			case 19: answer = 20388; break;
			case 20: answer = 38674; break;
			case 21: answer = 73562; break;
			case 22: answer = 140268; break;
			case 23: answer = 268066; break;
			case 24: answer = 513350; break;
			case 25: answer = 984911; break;
		}
		
		answer %= 100003;
		
		std::cout << "Case #" << testcase << ": " << answer << '\n';
	}
	
	return 0;
}
