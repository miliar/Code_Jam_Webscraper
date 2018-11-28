#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <set>

using namespace std;

int n;
char str[14];
int znak[13];
long long rez;
set<long long> nums;

void Init()
{
	rez = 0;
	memset(str, 0, sizeof(str));
	memset(znak, 0, sizeof(znak));
	nums.clear();
}

long long Abs(long long a)
{
	if (a < 0)
		a = -a;
	return a;
}

long long GetNum()
{
	long long s = 0;
	for (int i = 0; i < strlen(str) - 1; i++)
		s = s * 10 + long long(znak[i]);
	return s;
}

void Insert()
{
	nums.insert(GetNum());
}

bool IsUgly(long long number)
{
	number = Abs(number);

	if ((number % 2) == 0)
		return true;

	if ((number % 5) == 0)
		return true;

	int tmp = 0;
	long long cp = number;

	while(cp >= 10)
	{
		tmp += cp % 10;
		cp /= 10;
	}

	if (cp > 0)
		tmp += cp;

	if ((tmp % 3) == 0)
		return true;

	cp = number;

	number = (cp / 10) - 2 * (cp % 10);

	if ((number % 7) == 0)
		return true;

	return false;
}

long long Calculate()
{
	long long s = 0;
	long long number = 0;
	int zn = 1;

	number = int(str[0]) - 48;

	for (int i = 0; i < strlen(str) - 1; i++)
	{
		if (znak[i] != 0)
		{
			if (zn == 1)
				s += number;
			else if (zn == 2)
				s -= number;

			number = 0;
			zn = znak[i];
		}

		number = number * 10 + (int(str[i + 1]) - 48);
	}

	if (number != 0)
	{
		if (zn == 1)
			s += number;
		else
			s -= number;
	}

	return s;
}

long long DoIt(int pos, int zn)
{
	long long s = 0;
	long long r = 0;

	if (pos >= strlen(str) - 1 && pos != 0)
		return 0;
	
	znak[pos] = zn;

	s = Calculate();

	if (nums.find(GetNum()) == nums.end())
	{
		Insert();
		if (IsUgly(s) || s == 0)
			r++;
	}

	for (int i = 2; i >= 0; i--)
		r += DoIt(pos + 1, i);

	return r;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		Init();
		scanf("%s", &str);
		if (strlen(str) == 1)
			rez = DoIt(0, 0);
		else
		{
			for (int j = 2; j >= 0; j--)
				rez += DoIt(0, j);
		}
		printf("Case #%d: %lld\n", i + 1, rez);
	}
	return 0;
}