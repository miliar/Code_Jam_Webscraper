#include <iostream>
#include <fstream>

using namespace std;

#define cin fin
#define cout fout

#ifdef cin
ifstream fin("snapper.in");
#endif

#ifdef cout
ofstream fout("snapper.out");
#endif

//the pre-calculated list of n < 30 using s(n)
long h[] = 
{1, 3, 7, 15, 31, 63, 127, 255, 511, 1023,
2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575,
2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, };

//steps needed to turn ON and power the n th snapper
long s(int n)
{
	if (n == 0)
		return 1;

	return  s(n-1) + 1 + s(n-1);
}

void main()
{
	int t; //number of cases
	bool *op; //result list

	//input t
	cin>>t;

	//initialize op
	op = new bool[t];

	//handling the t cases
	for (int i=0; i<t; i++)
	{
		int n; //number of snappers
		long k; //number of snaps

		//input n, k
		cin>>n>>k;

		op[i] = (k % (h[n-1]+1) == h[n-1])? true : false;
	}

	//output op in the required format
	for (int i=0; i<t; i++)
	{
		if (op[i])
		{
			cout<<"Case #"<<i+1<<": "<<"ON"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": "<<"OFF"<<endl;
		}
	}	

	system("PAUSE");
}