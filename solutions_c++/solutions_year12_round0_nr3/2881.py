#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int num_digit(int num)	{
	if(num == 0)	return 1;
	int ant = 0;
	while(num > 0)	{
		num /= 10;
		ant++;
	}
	return ant;
}

int recycle(int num, int digits, int tot)	{
	int div = pow(10, digits);
	int pluss = num%div;
	if(pluss < (div/10))	return -1;
	int div2 = pow(10, tot-digits);
	pluss *= div2;
	num /= div;
	num += pluss;
	return num;
}

int main()	{
	int rounds, num1, num2, num1D, num2D, temp, tot;

	cin >> rounds;
	for(int i = 0; i < rounds; i++)	{
		cin >> num1 >> num2;
		tot = 0;
		num1D = num_digit(num1);	//num2D = num_digits(num2);
		for(int j = num2; j > num1; j--)	{
			for(int k = num2-1; k >= num1; k--)	{
				for(int l = 1; l < num1D; l++)	{
					temp = recycle(k, l, num1D);
					if(temp == j && j > k)	{
						tot++;
						break;
					}
				}
			}
		}
		cout <<"Case #" << i+1 <<": " << tot <<'\n';
	}
	return 0;
}
