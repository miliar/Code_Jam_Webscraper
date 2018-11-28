#include <iostream>
using namespace std;

int main(void)
{
	freopen ("B-large.in", "r" ,stdin);
	freopen ("output.txt", "w", stdout);

	int t;
	int cnt, tri, p;
	int tmp;
	int ccnt = 0;
	cin >> t;
	for (int x=1; x<=t; x++)
	{
		cout << "Case #" << x << ": ";
		cin >> cnt >> tri >> p;
		ccnt = 0;
		for (int i=0; i<cnt; i++)
		{
			cin >> tmp;
			if (tmp >= p*3) 
			{
//				cout << "tmp: " << tmp << endl;
//				cout << 1 << endl;
				ccnt++;
			}
			else if (tmp >= (p-1)*2 + p) 
			{
//				cout << "tmp: " << tmp << endl;
//				cout << 2 << endl;
				ccnt++;
			}
			else if (tmp >= 2*(p-2)+p && tri > 0 && 2*(p-2)+p >= 0)
			{
//				cout << "tmp: " << tmp << endl;
//				cout << 3 << endl;
				tri--;
				ccnt++;
			}
		}
		cout << ccnt << endl;
	}
	return 0;
}
