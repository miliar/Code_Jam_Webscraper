#include<iostream>
#include<algorithm>
using namespace std;

int n;

int pos[2];
int lt[2];

int dis( int x,int y )
{
	if( x<y ) return y-x;else return x-y;
}
int main()
{
	int TT;
	cin>>TT;

	for( int T = 1;T<=TT;T++ )
	{
		cout << "Case #"<<T<<": ";
		cin>>n;

		int cur = 0;
		pos[0] = pos[1] = 1;
		lt[0] = lt[1] = 0;

		char ch;
		int x;

		while(n--)
		{
			cin>>ch>>x;
			ch = (ch=='O');

			lt[ch] = max( lt[ch] + dis( pos[ch],x ),lt[1-ch] ) + 1;
			pos[ch] = x;
		}
		cout << max( lt[0],lt[1] ) << endl;
	}
	return 0;
}
