#include<iostream>
#include<vector>
#include<string>
#include<cassert>
#include<set>

using namespace std;

bool playgame(int i,int j,bool condition)
{
//	cerr << "At: " << i << ", " << j << " and condition: " << condition << endl;
	if(!i || !j)
	{
		return condition;
	}
	if(i==j)
	{
		return condition;
	}
	if(j>i)
	{
		swap(i,j);
	}

	//Either:
	//a) Subtract as much as possible
	//b) Leave 1 behind to force the opponent to remove it (you end up at subtract as much as possible)

	int optionA = i%j;
	int optionB = optionA + j;
	if(optionB<i)
	{
		if(!condition)
		{
			if(playgame(optionB,j,!condition) | playgame(j,optionA,!condition))
			{
				return true;
			}
		}
		else
		{
			if(!(playgame(optionB,j,!condition) & playgame(j,optionA,!condition)))
			{
				return false;
			}
		}
		//consider b)
/*		bool result = playgame(optionB,j,!condition);
		if(result && !condition)
		{
			return true;
		}
*/	}
	//	else
	//	There is no optionB, you were forced to remove the last

	//consider a)
	return playgame(j,optionA,!condition);
//	if(!condition && result)
//	{
//		return true;
//	}
//	return false;
//	return playgame(j,optionA,!condition);
}

int main()
{
	int num;
	cin >> num;
	for(int x=1;x<=num;x++)
	{
		int retval = 0;
		int a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		for(int i=a1;i<=a2;i++)
		{
			for(int j=b1;j<=b2;j++)
			{
				retval += playgame(i,j,false);
			}
		}
		cout << "Case #" << x << ": " << retval << endl;
			
	}
	return 0;	
}
