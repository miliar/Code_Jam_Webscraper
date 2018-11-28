#include <iostream>

using namespace std;

const int maxR = 50;
const int maxC = 50;
char A[maxR][maxC];

int main()
{
	//cout << "Hello!!!" << endl;
	//return 0;
	int T;
	bool is_possible;

	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
		*	Input Data
		*************************************/
		int R,C;
		cin >> R >> C;
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
				cin >> A[i][j];
		/************************************
		*	Solve the Problem
		*************************************/
		is_possible = false;
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
				if(A[i][j]=='#')
				{
					if(i+1==R || j+1==C)
						goto exit;
					if(A[i][j+1]!='#' || A[i+1][j]!='#' || A[i+1][j+1]!='#')
						goto exit;
					A[i][j]='/'; A[i][j+1]='\\'; 
					A[i+1][j]='\\'; A[i+1][j+1]='/'; 
				}
		is_possible = true;
		exit:
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": " << endl;
		if(is_possible)
		{
			for(int i=0; i<R; i++)
			{
				for(int j=0; j<C; j++)
					cout << A[i][j];
				cout << endl;
			}
		}
		else
			cout << "Impossible" << endl;
	}

	return 0;
}
