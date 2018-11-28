#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int max(int a,int b)
{
	return ((a>b)?a:b);
}
int main()
{
	int T,N;
	char ch, p=0;
	int n1, n, co, cb,t, po, pb, m=0;
	cin >> T;
	while(T--)
	{
		m++;
		cin >> N;
		co=1, cb=1;
		t=0;
		po=0, pb=0;
		for(int i=0;i<N;i++)
		{
			cin >> ch;
			if (ch=='O')
			{
				cin >> n1;
				n = abs(n1-co);
				co = n1;
				n++;
				if(t-po < n)
					t = n+po;
				else
					t++;
				po=t;
		//		cout << t << endl;
			}
			else
			{
				cin >> n1;
				n = abs(n1-cb);
				cb = n1;
				n++;
				if(t-pb < n)
					t = n+pb;
				else
					t++;
				pb=t;
		//		cout << t << endl;
			}
		}
		cout << "Case #" << m << ": " << t << endl;
	}
	return 0;
}
