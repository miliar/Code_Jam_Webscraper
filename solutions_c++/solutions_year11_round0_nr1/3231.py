#include  <iostream>
#include <list>
//#include <vector>
using namespace std;

void main ()
{

	int testCases=0;
	int i=1;
	int N,R;
	char P;

	freopen("A-large.in","r",stdin);
	freopen("output1l.txt","w",stdout);

	for (cin >> testCases; i <= testCases; i++)
    {
		list <int> Orange;
		list <int> iOrange;
		list <int> Blue;
		list <int> iBlue;
		int O=1,B=1;
		
		cin >> N;
		for (int j =1; j <= N; j++)
		{
			cin >> P >> R;
			if (P == 'O')
			{
				Orange.push_back(R);
				iOrange.push_back(j);
			}
			else if (P == 'B')
			{
				Blue.push_back(R);
				iBlue.push_back(j);
			}
		}

		int k = 1;
		int count =0;

		while (k <= N)
		{
			count++;
			bool press = false;
			if (!Orange.empty())
			{
				if (O < Orange.front())
					O++;
				else if (O > Orange.front())
					O--;
				else
				{
					if ( k==iOrange.front() && O==Orange.front() && !press)
					{
						Orange.pop_front();
						iOrange.pop_front();
						k++;
						press=true;
					}
				}
			}
			if (!Blue.empty())
			{
				if (B < Blue.front())
					B++;
				else if (B > Blue.front())
					B--;
				else
				{
					if ( k==iBlue.front() && B==Blue.front() && !press)
					{
						Blue.pop_front();
						iBlue.pop_front();
						k++;
						press=true;
					}
				}
			}
		}
		cout<< "Case #" << i << ": " << count << endl;
	}


}