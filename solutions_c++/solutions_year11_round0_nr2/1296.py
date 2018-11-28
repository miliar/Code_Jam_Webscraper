#include<iostream>
using namespace std;

char a[300][300];
int app[300];

char opx[100],opy[100];
int opt;
char q[1000];
int top;

int main()
{
	int TT;
	cin>>TT;
	int n;
	char c1,c2,c3;
	for( int T = 1;T<=TT;T++ )
	{
		cout << "Case #"<<T<<": ";
		for( char i = 'A';i<='Z';i++ )
		{
			app[i] = 0;
			for( char j = 'A';j<='Z';j++ )
				a[i][j] = 0;
		}
		cin>>n;
		while(n--)
		{
			cin>>c1>>c2>>c3;
			a[c1][c2] = a[c2][c1] = c3;
		}
		cin>>opt;
		for( int i = 0;i<opt;i++ )
			cin>>opx[i]>>opy[i];

		cin>>n;top = 0;
		while(n--)
		{
			cin>>c1;
			q[++top] = c1;app[c1]++;
			while( top > 1 && a[q[top-1]][q[top]]!=0 )
			{
				app[ q[top] ]--;
				app[ q[top-1] ]--;
				q[top-1] = a[q[top-1]][q[top]];
				top--;
				app[ q[top] ] ++;
			}
			for( int k=0;k<opt;k++ )
			if( app[opx[k]]>0 && app[ opy[k] ] >0 )
			{
				for( int i = 1;i<=top;i++ )
					app[ q[i] ] = 0;
				top = 0;
				break;
			}
		}
		cout << "[";
		for( int i = 1;i<=top;i++ )
		{
			cout << q[i];
			if( i<top ) cout << ", ";
		}
		cout << "]"<<endl;
	}
	return 0;
}
