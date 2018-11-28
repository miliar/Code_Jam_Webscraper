#include <iostream>

int main()
{
	int T, N;
	char line[50][50];
	std::cin >> T;
	for (int test_case = 0; test_case<T; test_case++)
	{
		std::cin >> N;
		for (int i=0; i<N; i++)
		{
			char buf[50];
			std::cin >> buf;
			strcpy(line[i], buf);
			//std::cout << line[i] << std::endl;
		}
		int ans = 0;
		for (int k=1; k<N; k++)
		{
			int sub_ans = 0;
			for (int i=0; i<N; i++)
			{
				if (line[i][0] == 0)
					continue;
				bool there_is_one = false;
				for (int j=k; j<N; j++)
				{
					if (line[i][j] != '0')
					{
						there_is_one = true;
						break;
					}
				}
				if (there_is_one == false) // all zero
				{
					ans += sub_ans;
					memset(line[i], 0x00, 50);
					break;
				}
				sub_ans++;
			}
		}
		std::cout << "Case #" << (test_case+1) << ": " << ans << std::endl;
	}
}