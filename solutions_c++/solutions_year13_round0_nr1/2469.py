#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<math.h>
using namespace std;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	int T;
	cin>>T;
	for(int CASE=1 ; CASE<=T ; CASE++)
	{
		char arr[4][4]={0};
		int DOT_Count=0;
		for(int i=0 ; i<4 ; i++)
		{
			for(int j=0 ; j<4 ; j++)
			{
				cin>>arr[i][j];
				if(arr[i][j]=='.')
					DOT_Count++;
			}
		}
		bool X_WIN=false,O_WIN=false,Draw=false;
		for(int i=0 ; i<4 ; i++)
		{
			int Number_X_Row=0,Number_T_Row=0,Number_O_Row=0,Number_X_Col=0,Number_T_Col=0,Number_O_Col=0;
			for(int j=0 ; j<4 ; j++)
			{
				if(arr[i][j]=='X')
					Number_X_Row++;
				else if(arr[i][j]=='O')
					Number_O_Row++;
				else if(arr[i][j]=='T')
					Number_T_Row++;
				///////////////////
				if(arr[j][i]=='X')
					Number_X_Col++;
				else if(arr[j][i]=='O')
					Number_O_Col++;
				else if(arr[j][i]=='T')
					Number_T_Col++;
			}
			if( ( Number_X_Row==4 ) || ( Number_X_Row==3 && Number_T_Row==1 ) )
			{
				X_WIN=true;
			}
			else if( ( Number_O_Row==4 ) || ( Number_O_Row==3 && Number_T_Row==1 ) )
			{
				O_WIN=true;
			}
			////////////////////////////
			if( ( Number_X_Col==4 ) || ( Number_X_Col==3 && Number_T_Col==1 ) )
			{
				X_WIN=true;
			}
			else if( ( Number_O_Col==4 ) || ( Number_O_Col==3 && Number_T_Col==1 ) )
			{
				O_WIN=true;
			}
			/////////////////////
			if(X_WIN || O_WIN )
			{
				break;
			}
		}
		if( !X_WIN && !O_WIN && DOT_Count==0)
		{
			Draw=true;
		}
		if( !X_WIN && !O_WIN && !Draw )
		{
			int X_L_Count=0,X_R_Count=0,O_L_Count=0,O_R_Count=0,T_L_Count=0,T_R_Count=0;
			for(int i=0 ; i<4 ; i++)
			{
				if(arr[i][i]=='X')
					X_L_Count++;
				else if(arr[i][i]=='O')
					O_L_Count++;
				else if(arr[i][i]=='T')
					T_L_Count++;

				//////////////////////

				if(arr[i][3-i]=='X')
					X_R_Count++;
				else if(arr[i][3-i]=='O')
					O_R_Count++;
				else if(arr[i][3-i]=='T')
					T_R_Count++;
			}
			if( ( X_L_Count==4 ) || ( X_L_Count==3 && T_L_Count==1 ) || ( X_R_Count==4 ) || ( X_R_Count==3 && T_R_Count==1 ) )
			{
				X_WIN=true;
			}
			else if( ( O_L_Count==4 ) || ( O_L_Count==3 && T_L_Count==1 ) || ( O_R_Count==4 ) || ( O_R_Count==3 && T_R_Count==1 ) )
			{
				O_WIN=true;
			}
		}
		cout<<"Case #"<<CASE<<": ";
		if(X_WIN)
			cout<<"X won\n";
		else if(O_WIN)
			cout<<"O won\n";
		else if(Draw)
			cout<<"Draw\n";
		else
			cout<<"Game has not completed\n";

	}
	return 0;
}