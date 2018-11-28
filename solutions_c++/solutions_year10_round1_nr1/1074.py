

#include <iostream>
#define N 50
using namespace std;

bool isKRow(char b[][N], int k, int n, char ch)
{
	int len;
	for (int j = n - 1; j >= 0; --j)
	  for (int i = 0; i <= n - k + 1; ++i)
	  if (b[i][j] == ch) {
		  len = 0;
		  while(b[i+len][j] == ch && i + len < n) ++len;
		 // cout << endl <<  ch<<":"<<  i<< ":col:" << j <<':' << len;
		  if (len >= k) return 1;
	  }
	for (int i = 0; i < n; ++i)
	  for (int j = n - 1; j >= 0; --j)
	  if (b[i][j] == ch) {
		  len = 0;
		  while(b[i][j-len] == ch && j-len >= 0) ++len;
		  //cout << endl << ch<<":"<<   i<< ":row:" << j <<':' << len;
		  if (len >= k) return 1;
	  }
	for (int i = 0; i < n; ++i)
	  for (int j = 0; j < n; ++j)
	  if (b[i][j] == ch) {
		  len = 0;
		  while(b[i+len][j-len] == ch && j-len >= 0 && i+len < n) ++len;
		  //cout << endl << ch<<":"<<   i<< ":diag1:" << j <<':' << len;
		  if (len >= k) return 1;
	  }
	for (int i = 0; i < n; ++i)
	  for (int j = 0; j < n; ++j)
	  if (b[i][j] == ch) {
		  len = 0;
		  while(b[i-len][j-len] == ch && j-len >= 0 && i-len >= 0) ++len;
		 // cout << endl <<  ch<<":"<<  i<< ":diag2:" << j <<':' << len;
		  if (len >= k) return 1;
	  }
	return 0;
}

int main()
{
	char board[N][N];
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t)
	{
	  int n, k;
	  cin >> n >> k;
	  for (int i = 0; i < n; ++i)
	    for (int j = 0; j < n; ++j)
	    cin >> board[i][j];
	   
	  bool b = isKRow(board, k, n, 'B');
	  bool r = isKRow(board, k, n, 'R');
	  
	  for (int i = 0; i < n; ++i)
	    for (int j = n - 2; j >= 0; --j)
	    if (board[i][j] != '.')
	  {
		  int p = j;
		  while(board[i][p + 1] == '.' && p < n - 1) {
		    board[i][p + 1] = board[i][p];
		    board[i][p] = '.';
		    ++p;
	      } 
	  }
	  //cout << "---------------" <<endl;
	  if (!b) b = isKRow(board, k, n, 'B');
	  if (!r) r = isKRow(board, k, n, 'R');
	  
      //~ for (int i = 0; i < n; ++i){
		  //~ cout << endl;
	    //~ for (int j = 0; j < n; ++j)
	    //~ cout << board[i][j];
	//~ }
	  cout << "Case #"<<t<<": ";
	  if (b & r) cout << "Both";
	  else if (b) cout << "Blue";
	  else if (r) cout << "Red";
	  else cout << "Neither";
	  cout << endl;
	}
	
	return 0;
}
