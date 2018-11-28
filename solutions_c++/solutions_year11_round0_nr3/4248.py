#include <iostream>
#include <algorithm>
using namespace std;

int set1(int i , int num)
{
	return num | 1 << i;
}

bool getbit(int i , int num)
{
	return num & 1 << i;
}

int PatrickSum(int a , int b)
{
	bool bita , bitb;
	int  result = 0;

	for(int i = 0;i < 30;i++)
	{
		bita = getbit(i , a);
		bitb = getbit(i , b);

		if(bita != bitb)
			result = set1(i , result);
	}
	return result;
}

int Candy , TestCases , CandyNumber;

//int Find (int index , int PatrickSean , int c , int Patrick , int d , int Sean)
//{
//	if(index == CandyNumber)
//	{
//		if(PatrickSean == Patrick)
//		{
//			if(c == 0 || d == 0)
//				return -1;
//			return Sean;
//		}
//		else
//		{
//			return -1;
//		}
//	}
//	else
//	{
//		int a = Find(index+1 , PatrickSum(PatrickSean , Candy[index]) , c+1 , Patrick , d , Sean + Candy[index]);
//		int b = Find(index+1 , PatrickSean , c , PatrickSum(Patrick , Candy[index]) , d+1 , Sean);
//		return max(a , b);
//	}
//}

int main () 
{
	freopen("Input.txt" , "r" , stdin);
	freopen("Output.txt" , "w" , stdout);

	int Sean , Patrick , PatrickSean , Max , XOR , Sum , Min;

	cin >> TestCases;

	for(int i = 1;i <= TestCases;i++)
	{
		cin >> CandyNumber;

		XOR = Sum = 0;
		Min = INT_MAX;

		for(int j = 0;j < CandyNumber;j++)
		{
			cin >> Candy;

			Sum += Candy;
			XOR = XOR ^ Candy;
			if(Candy < Min)
				Min = Candy;
		}

		//Max = Find(0 , 0 , 0 , 0 , 0 , 0);

		if(XOR == 0)
			cout << "Case #" << i << ": " << Sum - Min << endl;
		else
			cout << "Case #" << i << ": NO\n";

		/*if(Max == -1) 
			cout << "Case #" << i << ": NO\n";
		else
			cout << "Case #" << i << ": " << Max << endl;*/
	}

	return 0;
}