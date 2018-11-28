#include <iostream>

using namespace std;
 char board[16]={0}; // input board state
 short int playerOstate[10];	//R1,R2,R3,R4,C1,C2,C3,C4,D1,D2
 short int playerXstate[10];
 int emptysq;

void initialize()
{
	memset(playerOstate,0,10*sizeof( short int));
	memset(playerXstate,0,10*sizeof( short int));
	emptysq = 0;

};
int fillstates()	//(char* board,short int* playerOstate,short int* playerXstate )
{
	// Fill board
	for (int i=0;i<4;++i)
	{
		for (int j=0;j<4;j++)
		{
			cin>>board[i*4+j];
		}
	}
	// Fill states for Players
 	for (int i=0;i<4;++i)
	{
		for (int j=0;j<4;++j)
		{
			//for player X
			if (board[i*4+j]=='X' || board[i*4+j]=='T')
			{
				++playerXstate[i];
				++playerXstate[j+4];
				if (i==j)
				{
					++playerXstate[8];
				} 
				else if((i+j)==3)
				{
					++playerXstate[9];
				}
			}
			//for player O
			if (board[i*4+j]=='O' || board[i*4+j]=='T')
			{
				++playerOstate[i];
				++playerOstate[j+4];
				if (i==j)
				{
					++playerOstate[8];
				} 
				else if((i+j)==3)
				{
					++playerOstate[9];
				}
			}
			// Count empty squares
			if (board[i*4+j]=='.')
			{
				++emptysq;
			}
		}
	}
	return 0;
}
void solve_case(int test_case)
{
	initialize();
	fillstates();
	for (int i=0;i<10;++i)
	{
		if (playerOstate[i]==4)
		{
			cout<<"Case #"<<test_case<<": "<<"O won"<<endl;
			return;
		}
		if (playerXstate[i]==4)
		{
			cout<<"Case #"<<test_case<<": "<<"X won"<<endl;
			return;
		}
	}
	if (emptysq>0)
	{
		cout<<"Case #"<<test_case<<": "<<"Game has not completed"<<endl;
		return;
	}
	else
	{
		cout<<"Case #"<<test_case<<": "<<"Draw"<<endl;
		return;
	}


};

int main()
{
	freopen("Alarge.in","r",stdin);
	freopen("Alarge.out","w",stdout);
	initialize();
	int T; scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);

	return 0;
}