#include<iostream>
using namespace std;
char arr[5][5];
char solve()
{
	for ( int i=0 ; i<4 ; i++ )
	{
		if ( arr[i][0]!='.' && arr[i][0]==arr[i][1] && arr[i][0]==arr[i][2] && arr[i][0]==arr[i][3] )
			return arr[i][0];
		if ( arr[i][0]=='T' && arr[i][1]!='.' && arr[i][1]==arr[i][2] && arr[i][1]==arr[i][3] )
			return arr[i][1];
		if ( arr[i][1]=='T' && arr[i][0]!='.' && arr[i][0]==arr[i][2] && arr[i][0]==arr[i][3] )
			return arr[i][0];
		if ( arr[i][2]=='T' && arr[i][0]!='.' && arr[i][0]==arr[i][1] && arr[i][0]==arr[i][3] )
			return arr[i][0];
		if ( arr[i][3]=='T' && arr[i][0]!='.' && arr[i][0]==arr[i][2] && arr[i][1]==arr[i][0] )
			return arr[i][0];
	}
	for ( int i=0 ; i<4 ; i++ )
	{
		if ( arr[0][i]!='.' && arr[0][i]==arr[1][i] && arr[0][i]==arr[2][i] && arr[0][i]==arr[3][i] )
			return arr[0][i];
		if ( arr[0][i]=='T' && arr[1][i]!='.' && arr[3][i]==arr[1][i] && arr[3][i]==arr[2][i] )
			return arr[1][i];
		if ( arr[1][i]=='T' && arr[0][i]!='.' && arr[3][i]==arr[0][i] && arr[3][i]==arr[2][i] )
			return arr[0][i];
		if ( arr[2][i]=='T' && arr[1][i]!='.' && arr[3][i]==arr[1][i] && arr[3][i]==arr[0][i] )
			return arr[0][i];
		if ( arr[3][i]=='T' && arr[1][i]!='.' && arr[0][i]==arr[1][i] && arr[0][i]==arr[2][i] )
			return arr[0][i];
	}
	if ( arr[0][0]!='.' && arr[0][0]==arr[1][1] && arr[1][1]==arr[2][2] && arr[3][3]==arr[2][2] )
		return arr[0][0];
	if ( arr[0][0]!='.' && arr[0][0]==arr[1][1] && arr[1][1]==arr[2][2] && arr[3][3]=='T' )
		return arr[0][0];
	if ( arr[0][0]!='.' && arr[0][0]==arr[1][1] && arr[1][1]==arr[3][3] && arr[2][2]=='T' )
		return arr[0][0];
	if ( arr[0][0]!='.' && arr[0][0]==arr[3][3] && arr[3][3]==arr[2][2] && arr[1][1]=='T' )
		return arr[0][0];
	if ( arr[3][3]!='.' && arr[3][3]==arr[1][1] && arr[1][1]==arr[2][2] && arr[0][0]=='T' )
		return arr[3][3];
	if ( arr[0][3]!='.' && arr[0][3]==arr[1][2] && arr[1][2]==arr[2][1] && arr[3][0]==arr[2][1] )
		return arr[0][3];
	if ( arr[0][3]!='.' && arr[0][3]==arr[1][2] && arr[1][2]==arr[2][1] && arr[3][0]=='T' )
		return arr[0][3];
	if ( arr[0][3]!='.' && arr[0][3]==arr[1][2] && arr[1][2]==arr[3][0] && arr[2][1]=='T' )
		return arr[0][3];
	if ( arr[0][3]!='.' && arr[0][3]==arr[3][0] && arr[3][0]==arr[2][1] && arr[1][2]=='T' )
		return arr[0][3];
	if ( arr[1][2]!='.' && arr[3][0]==arr[1][2] && arr[1][2]==arr[2][1] && arr[0][3]=='T' )
		return arr[1][2];
	return 'D';
}
int main()
{
	//freopen ( "input.in" , "r" , stdin );
	//freopen ( "output.out" , "w" , stdout);
	int t,num;
	char c;
	cin>>t;
	for ( int i=0 ; i<t ; i++ )
	{
		num=0;
		for ( int j=0 ; j<4 ; j++ )
		{
			for ( int k=0 ; k<4 ; k++ )
			{
				cin>>arr[j][k];
				if ( arr[j][k] != '.' )
					num++;
			}
		}
		c=solve();
		cout<<"Case #"<<i+1<<": ";
		if ( c=='X' )
			cout<<"X won\n";
		else if ( c=='O' )
			cout<<"O won\n";
		else if ( num==16 && c=='D' )
			cout<<"Draw\n";
		else
			cout<<"Game has not completed\n";
	}
}