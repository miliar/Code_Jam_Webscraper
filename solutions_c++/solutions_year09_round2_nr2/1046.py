#include <iostream>
#include <algorithm>
using namespace std;
int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int ca = 1;
	cin >> t;
	while (t--)
	{
		char n[50];
		while (cin >> n)
		{
			int k = strlen(n);
			int a[50];
			for (int i = strlen(n)-1; i >= 0; i--)
			{
				a[k-i-1] = n[i]-'0';
			}
			int mark;
			int i;
			int flag = 0;
			for (i = 0; i < k; i++)
			{
				int j;
				for (j = 0; j < i; j++)
				{
					if (a[i] < a[j])
					{
						flag = 1;
						break;
					}
				}
				if (j != i)
				{
					
					//cout << "hello\n";
					int mmin = 10;
					for (j = 0; j < i; j++)
						if (a[j] < mmin && a[j] > a[i])
						{
							mmin = a[j];
							mark = j;
						}
						//cout << i << endl;
						break;
						
				}
			}
			if (flag == 1)
			{
			int temp = a[mark];
			a[mark] = a[i];
			a[i] = temp;
			//cout << a[i]<< endl;
			//cout << a[mark] << endl;
			int ttt[50];
			int zz = 0;
			for (int x = 0; x < i;x++)
				ttt[zz++] = a[x];
			sort (ttt, ttt+zz);
			printf ("Case #%d: ", ca++);
			for (int x = k-1; x >= i; x--)
				cout << a[x];
			for (int x = 0; x < i; x++)
				cout <<ttt[x];
			cout << endl;
			}
			else 
			{
				sort (a, a+k);
				printf ("Case #%d: ", ca++);
				//cout << a[0] <<"0";
				for (int x = 0; x < k; x++)
				{
					if (a[x] != 0)
					{
						cout << a[x] <<"0";
						mark = x;
						break;
					}
				}
				for (int x = 0; x < k; x++)
					if (x != mark)cout << a[x];
				cout << endl;
			}
		}
	}
}