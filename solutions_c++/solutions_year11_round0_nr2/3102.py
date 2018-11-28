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

	freopen("input1.txt","r",stdin);
	//freopen("output1.txt","w",stdout);

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
			if (!Orange.empty())
			{
				if (O < Orange.front())
				{
					O++;
					cout << 'O' << O << "++" << " " ;
				}
				else if (O > Orange.front())
				{
					O--;
					cout << 'O' << O << "--" << " " ;
				}
				else
				{
					if ( k==iOrange.front() && O==Orange.front() )
					{
						Orange.pop_front();
						iOrange.pop_front();
						cout << 'O' << O << "*" << " " ;
						k++;
						cout<< endl;
						continue;
					}
					else
						cout << 'O' << O << " "  ;
				}
			}
			if (!Blue.empty())
			{
				if (B < Blue.front())
				{
					B++;
					cout << 'B' << B << "++" << " " ;
				}
				else if (B > Blue.front())
				{
					B--;
					cout << 'B' << B << "--" << " "  ;
				}
				else
				{
					if ( k==iBlue.front() && B==Blue.front())
					{
						Blue.pop_front();
						iBlue.pop_front();
						cout << 'B' << B << "*" << " " ;
						k++;
						cout<< endl;
						continue;
					}
					else
						cout << 'B' << B << " "  ;
				}
			}
			cout<< endl;
		}
		cout<< "***************"<< endl;
		cout<< "Case # " << i << " : " << count;
	}


}