#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;

const int MAXN = 2000001;
int a[MAXN];

class Number
{
public:
	char ch[10];
	int len;
	Number(int n)
	{
		if (n <= 0 || n >= 100000000) throw "Error";

		len = 0;
		while (n != 0)
		{
			ch[len] = n % 10 + '0';
			len++;
			n /= 10;
		}
		reverse(ch, ch + len);
	}

	void Increase()
	{
		int pass = 1;
		for (int i = len - 1; i >= 0 && pass != 0; i--)
		{
			ch[i] = ch[i] + pass;

			if (ch[i] == '9' + 1)
			{
				ch[i] = '0';
				pass = 1;
			}
			else
			{
				pass = 0;
			}
		}
	}

	void RotateLeft()
	{
		char temp = ch[0];
		for (int i = 0; i < len - 1; i++)
		{
			ch[i] = ch[i + 1];
		}

		ch[len - 1] = temp;
	}

	int Compare(const Number& right)
	{
		if (this->len != right.len) throw "Error";

		for (int i = 0; i < this->len; i++)
		{
			if (this->ch[i] > right.ch[i])
			{
				return 1;
			}
			else if (this->ch[i] < right.ch[i])
			{
				return -1;
			}
		}
		return 0;
	}

	int GetNumber()
	{
		int ret = 0;
		for (int i = 0; i < len; i++)
		{
			ret = ret * 10 + ch[i] - '0';
		}
		return ret;
	}
};

int run(int A, int B)
{
	memset(a, 0, sizeof(a));
	int ret = 0;
	int current = A;
	Number CurrentNumber(A);
	Number ANumber(A);
	Number BNumber(B);
	for (int i = A; i <= B; i++)
	{
		if (a[i] == 0)
		{
			int count = 0;
			bool loop = false;
			for (int j = 0; j < CurrentNumber.len; j++)
			{
				CurrentNumber.RotateLeft();
				if (CurrentNumber.Compare(ANumber) >= 0 && CurrentNumber.Compare(BNumber) <= 0)
				{
					a[CurrentNumber.GetNumber()] = 1;
					count++;
				}

				if (CurrentNumber.GetNumber() == i)
				{
					break;
				}
			}
			// cout << ret << endl;
			ret += count * (count - 1) / 2;
		}

		CurrentNumber.Increase();
	}

	return ret;
}

bool isPair(int left, int right)
{
	ostringstream leftS, rightS;
	leftS << left;
	rightS << right;
	string current = leftS.str();

	while(true)
	{
		char c = current[0];

		for (int i = 0; i < (int) current.size() - 1;i++)
		{
			current[i] = current[i + 1];
		}

		current[current.size() - 1] = c;

		if (current == leftS.str())
		{
			return false;
		}

		if (current == rightS.str())
		{
			return true;
		}
	}

	return false;
}

int run2(int A, int B)
{
	int ret = 0;
	for (int i = A; i <= B; i++)
	{
		for (int j = i + 1; j <= B; j++)
		{
			if (isPair(i, j))
			{
				ret++;
			}
		}
	}

	return ret;
}
int main()
{
	int T;
	cin >> T;

	// cout << run(10, 99) << " " << run2(10, 99) << endl;
//	cout << run(100, 999) << " " << run2(100, 999) << endl;
	/*cout << run(50, 99) << " " << run2(50, 99) << endl;
	cout << run(500, 999) << " " << run2(500, 999) << endl;*/

	for (int i = 0; i < T; i++)
	{
		int  A, B;
		cin >> A >> B;
		printf("Case #%d: %d\n", i + 1, run(A, B));
	}
}