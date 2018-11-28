#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("A-large.in");
//ifstream fin("A-large-practice.in");
ofstream fout("1.out");
#define cin fin
#define cout fout

#define N 1010 
int a[N];
int main()
{
	int tcase;
	cin >> tcase;
	int icase = 1;
	int k, n;

	int cur;
	while (icase <= tcase)
	{
		cout << "Case #" << icase << ": ";
		cin >> n >> k;
		cur = 1 << n;
		if((k % cur) == (cur -1))
		{
			cout << "ON" << endl;
		}
		else
		{
			cout << "OFF" << endl;
		}
		icase ++;
	}
	return 0;
}


