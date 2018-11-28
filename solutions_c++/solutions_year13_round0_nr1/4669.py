#include <iostream>
#define For(i, a, b) for(int i=a; i<b; ++i)
using namespace std;

char A[5][5];

bool ganaX()
{
	For(i, 0, 4)
	{
		if ((A[i][0] == 'X' or A[i][0] == 'T') and (A[i][1] == 'X' or A[i][1] == 'T') and (A[i][2] == 'X' or A[i][2] == 'T') and (A[i][3] == 'X' or A[i][3] == 'T'))
			return true;
		if ((A[0][i] == 'X' or A[0][i] == 'T') and (A[1][i] == 'X' or A[1][i] == 'T') and (A[2][i] == 'X' or A[2][i] == 'T') and (A[3][i] == 'X' or A[3][i] == 'T'))
			return true;
	}	
	
	if ((A[0][0] == 'X' or A[0][0] == 'T') and (A[1][1] == 'X' or A[1][1] == 'T') and (A[2][2] == 'X' or A[2][2] == 'T') and (A[3][3] == 'X' or A[3][3] == 'T'))
		return true;
	
	if ((A[0][3] == 'X' or A[0][3] == 'T') and (A[1][2] == 'X' or A[1][2] == 'T') and (A[2][1] == 'X' or A[2][1] == 'T') and (A[3][0] == 'X' or A[3][0] == 'T'))
		return true;
		
	return false;
}

bool ganaO()
{
	For(i, 0, 4)
	{
		if ((A[i][0] == 'O' or A[i][0] == 'T') and (A[i][1] == 'O' or A[i][1] == 'T') and (A[i][2] == 'O' or A[i][2] == 'T') and (A[i][3] == 'O' or A[i][3] == 'T'))
			return true;
		if ((A[0][i] == 'O' or A[0][i] == 'T') and (A[1][i] == 'O' or A[1][i] == 'T') and (A[2][i] == 'O' or A[2][i] == 'T') and (A[3][i] == 'O' or A[3][i] == 'T'))
			return true;
	}	
	
	if ((A[0][0] == 'O' or A[0][0] == 'T') and (A[1][1] == 'O' or A[1][1] == 'T') and (A[2][2] == 'O' or A[2][2] == 'T') and (A[3][3] == 'O' or A[3][3] == 'T'))
		return true;
	
	if ((A[0][3] == 'O' or A[0][3] == 'T') and (A[1][2] == 'O' or A[1][2] == 'T') and (A[2][1] == 'O' or A[2][1] == 'T') and (A[3][0] == 'O' or A[3][0] == 'T'))
		return true;
		
	return false;
}

bool lleno()
{
	For(i, 0, 4)
		For(j, 0, 4)
			if (A[i][j] == '.')
				return false;
	return true;
}

int main()
{
	int T;
	cin>>T;
	For(i, 0, T)
	{
		For(j, 0, 4)
			cin>>A[j];
		if (ganaX())
			cout<<"Case #"<<i+1<<": X won"<<endl;
		else if (ganaO())
			cout<<"Case #"<<i+1<<": O won"<<endl;
		else if (lleno())
			cout<<"Case #"<<i+1<<": Draw"<<endl;
		else 
			cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
	}
	return 0;
}
