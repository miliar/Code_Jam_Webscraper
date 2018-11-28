#include <iostream>

char string[500];
char match[] = "welcome to code jam";

int how_many(int string_s, int string_e, int match_s, int match_e)
// do not test "string[string_e]"
{
	int string_len = string_e - string_s;
	int match_len = match_e - match_s;
	if (match_len < 0) std::cout << "unexpected";
	if (string_len < 0) std::cout << "unexpected";
	if (match_len == 0) return 1;
	if (string_len == 0) return 0;
	if (match_len > string_len) return 0;

	int ret = 0;

	if (match_len == 1)
	{
		for (int i=0; i<string_len; i++)
			if (string[string_s+i] == match[match_s])
				ret++;
		return ret;
	}

	if (match_len == string_len)
	{
		for (int i=0; i<string_len; i++)
			if (string[string_s+i] != match[match_s+i])
				return 0;
		return 1;
	}

	if (string_len < 5)
	{
		switch (string_len)
		{
		case 4:
			switch (match_len)
			{
			case 3: 
				if (string[string_s]==match[match_s] && string[string_s+1]==match[match_s+1] && string[string_s+2]==match[match_s+2]) ret++;
				if (string[string_s]==match[match_s] && string[string_s+1]==match[match_s+1] && string[string_s+3]==match[match_s+2]) ret++;
				if (string[string_s]==match[match_s] && string[string_s+2]==match[match_s+1] && string[string_s+3]==match[match_s+2]) ret++;
				if (string[string_s+1]==match[match_s] && string[string_s+2]==match[match_s+1] && string[string_s+3]==match[match_s+2]) ret++;
				return ret;
			case 2:
				if (string[string_s]==match[match_s] && string[string_s+1]==match[match_s+1]) ret++;
				if (string[string_s]==match[match_s] && string[string_s+2]==match[match_s+1]) ret++;
				if (string[string_s]==match[match_s] && string[string_s+3]==match[match_s+1]) ret++;
				if (string[string_s+1]==match[match_s] && string[string_s+2]==match[match_s+1]) ret++;
				if (string[string_s+1]==match[match_s] && string[string_s+3]==match[match_s+1]) ret++;
				if (string[string_s+2]==match[match_s] && string[string_s+3]==match[match_s+1]) ret++;
				return ret;
			}
			break;
		case 3:
			switch (match_len)
			{
			case 2: if (string[string_s]==match[match_s] && string[string_s+1]==match[match_s+1]) ret++;
				if (string[string_s]==match[match_s] && string[string_s+2]==match[match_s+1]) ret++;
				if (string[string_s+1]==match[match_s] && string[string_s+2]==match[match_s+1]) ret++;
				return ret;
			}
			break;
		default:
			std::cout << "unexpected";
		}
	}

	int half = string_len/2;
	for (int i=0; i<=match_len; i++)
	{
		ret += how_many(string_s, string_s+half, match_s, match_s+i) * 
			how_many(string_s+half, string_e, match_s+i, match_e);
	}
	return ret%10000;	
}

int main()
{
	int n;
	std::cin >> n;
	char hay[100][500];
	int hay_nums[100];
	std::cin.getline(hay[0], 500);
	for (int i=0; i<n; i++)
	{
		std::cin.getline(hay[i], 500);
		hay_nums[i] = strlen(hay[i]);
	}

	for (int i=0; i<n; i++)
	{
		int answer = 0;
		if (hay_nums[i] == 0)
			answer = 0;
		else
		{
			strcpy(string, hay[i]);
			//std::cout << hay_nums[i] << " " << match << "\n";
			answer = how_many(0, strlen(string), 0, strlen(match));
		}
		printf("Case #%d: %04d\n", (i+1), answer);
	}
}