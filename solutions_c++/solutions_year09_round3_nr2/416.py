#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

double crd[3], spd[3];

double calc(double t)
{
	double res = 0;
	for (int i = 0; i < 3; i++)
	{
		double tmp = crd[i] + spd[i] * t;
		res += tmp * tmp;
	}
	return sqrt(res);
}

double findTime()
{
	double left = 0;
	double right = 1000000;
	while (right - left >= 1e-10)
	{
		
		double leftThird = (left*2+right)/3;
		double rightThird = (left+right*2)/3;
		if (calc(leftThird) > calc(rightThird))
			left = leftThird;
		else
			right = rightThird;
	}
	return right;
}

double calc2()
{
	int non = -1;
	for (int i = 0; i < 3; i++)
		if (spd[i] > 1e-10)
			non = i;
	if (non == -1)
		return 0;
	swap(crd[non], crd[0]);
	swap(spd[non], spd[0]);
	double a = crd[0] * (spd[1] + spd[2]);
	double b = (spd[1] * crd[1] + spd[2] * crd[2]) * spd[0];
	double c = spd[0] * spd[0] + spd[1] * spd[1] + spd[2] * spd[2];
	double res = (a - b) / c;
	res = (res - crd[0]) / spd[0];
}

int main()
{
	ifstream input("Input.txt");
	ofstream output("output.txt");
	int tt;
	input >> tt;
	for (int ttt = 1; ttt <= tt; ttt++)
	{
		int n;
		input >> n;
		memset(crd, 0, sizeof(double) * 3);
		spd[0] = spd[1] = spd[2] = 0;
		for (int i = 0; i < n; i++)
		{
			double tmp;
			for (int j = 0; j < 3; j++)
			{
				input >> tmp;
				crd[j] += tmp;
			}
			for (int j = 0; j < 3; j++)
			{
				input >> tmp;
				spd[j] += tmp;
			}
		}
		for (int i = 0; i < 3; i++)
		{
			spd[i] /= n;
			crd[i] /= n;
		}
		double t = findTime();
		printf("Case #%d: %0.10f %0.10f\n",ttt, calc(t), t);

	} 

	return 0;
}