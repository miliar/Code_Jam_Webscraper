#include <iostream>  
#include <string>  
#include <vector>  
#include <set>  
#include <map>  
#include <algorithm>  
#include <math.h>  
#include <sstream>  
#include <ctype.h>  
#include <queue>  
#include <stack>  
#include <fstream>
using namespace std;  

template<class Item>  
void display(vector<Item> v)  
{  
  for(int i=0; i<v.size(); i++)  
    cout << v[i] << ' ';  
  cout << '\n';  
}   

int N, K;
int board[18][30];
int cancross[18][18];

int check(int a, int b)
{

for(int i=0; i<K; i++)
{
	if(board[a][i]==board[b][i]) return 0;
	
	if(i>0)
	{
		int A = board[a][i-1] > board[b][i-1];
		int B = board[a][i] > board[b][i];
		if(A!=B) return 0;
	}
}

return 1;

}

int oksub[1<<17];
int table[1<<17];

int doit(int n)
{	//cout << n << endl;
	if(n==(1<<N)-1 ) return 0;

	if(table[n] > -1) return table[n];

	table[n] = 100000;
	int t = (1<<N)-1;
	t ^= n;

	for(int i=(1<<N)-1; i>0; i=(i-1)&t)
	{
		if(oksub[i] && !(i&n))
		table[n] = min(table[n], 1+doit(i|n) );
	}
	return table[n];
}

		

int main()
{

fstream In("c-small.in", ios::in);
fstream Out("c-small.out", ios::out);

int T;

In >> T;

for(int h=0; h<T; h++)
{
Out << "Case #" << h+1 << ": ";
cout << h << endl;
In >> N >> K;
memset(board, -1, sizeof(board));

for(int i=0; i<N; i++) for(int j=0; j<K; j++)
	In >> board[i][j];

for(int i=0; i<N; i++) for(int j=0; j<N; j++)
{
	if(i==j) cancross[i][j]=1;
	else cancross[i][j] = check(i, j);
}
//for(int i=0; i<N; i++) { for(int j=0; j<N; j++) cout << cancross[i][j] << ' '; cout << endl;}

memset(oksub, 0, sizeof(oksub));
	for(int i=1; i<(1<<N); i++)
	{
		oksub[i] = 0;
		int j=0, k=N;
		for(j=0; j<N; j++) 
		{	k=N;
			if(i&(1<<j))
				for(k=j+1; k<N; k++)
					if(i&(1<<k))
						if(!cancross[j][k]) break;
			if(k!=N) break;
		}
		//cout << i << ' ' << j << ' ' << k << endl;
		if(j==N) oksub[i] = 1;
		//cout << i << ' ' << oksub[i] << endl;
	}



memset(table, -1, sizeof(table));
Out << doit(0) << endl;

}


In.close();

Out.close();

return 0;

}
