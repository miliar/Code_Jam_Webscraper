#include <iostream>
using namespace std;

int judge(int num1, int num2);
int main(int argc, char const *argv[])
{
	int a, b, n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cin >> a >> b;
		int rs = 0;
		for (int j = a; j < b; ++j)
		{
			for (int k = j+1; k <= b; ++k)
			{
				rs += judge(j, k);
			}
		}
		cout << "Case #" << i+1 << ": " << rs << endl;
	}
	return 0;
}

int judge(int num1, int num2){
	if (num1 <= 10 || num1 == 1000 || num2 == 1000)
		return 0;
	else if (num1 < 100)
	{
		if (num2 >= 100)
		return 0;
		if ((num1 / 10 == num2 % 10) && (num1 % 10 == num2 / 10))
			return 1;
		else return 0;
	}
	else {
		if ((num2 == (num1 / 10) + (num1 % 10)*100) || (num2 == (num1 / 100) + (num1 % 100) * 10))
		return 1;
		else return 0;
	}
}
