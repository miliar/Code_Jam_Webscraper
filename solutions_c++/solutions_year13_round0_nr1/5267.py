#include <iostream>

//#define _DEBUG_

using namespace std;

	const int N = 4;

	char a[N][N];

bool has_won_in_line(char c, int si, int sj, int di, int dj)
{
   int i,j,cnt;
   for(i=si, j=sj, cnt=0; cnt<N; cnt++, i+=di, j+=dj )
      if(a[i][j]!=c && a[i][j]!='T')
        return false;
   return true;
}

bool has_won(char c)
{
   for(int i=0; i<N; i++)                  // rows
      if(has_won_in_line(c,i,0,0,1))
         return true;
   for(int i=0; i<N; i++)                  // columns
      if(has_won_in_line(c,0,i,1,0))
         return true;
   if(has_won_in_line(c,0,0,1,1))          // main diag
         return true;
   if(has_won_in_line(c,0,N-1,+1,-1))    // sec diag
         return true;
   return false;
}

int main()
{
	int T;
	char*res = NULL;
	bool there_is_a_dot;

	cin >> T;
	for(int t=1; t<=T; t++)
	{
		/************************************
		*	Input Data
		*************************************/
		there_is_a_dot = false;
		for(int i=0; i<N; i++)
		   for(int j=0; j<N; j++)
		   {
                      cin >> a[i][j];
                      if(a[i][j]=='.')
                         there_is_a_dot = true;
                   }
		cin.ignore();
		cin.ignore();
		#ifdef _DEBUG_
		for(int i=0; i<N; i++)
		{
		   for(int j=0; j<N; j++)
                      cout << a[i][j];
                   cout<<endl;
                }
                #endif
		/************************************
		*	Solve the Problem
		*************************************/
		if(has_won('X'))
		   res = "X won";
		else if(has_won('O'))
		   res = "O won";
		else if(there_is_a_dot)
		   res = "Game has not completed";
		else
		   res = "Draw";
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}
