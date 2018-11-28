#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) (i)=(c).begin();i!=(c).end();i++)
#define present(c,x) ((c).find(x)!=(c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;

typedef vector<string> VS;
typedef vector<VS> VVS;
typedef vector<VVS> VVVS;

typedef pair<int,int> II;

typedef vector<char> VC;
typedef vector<VC> VVC;

void rotate(VVC& board)
{
	int N=board[0].size();
	for(int i=0; i<N; i++)
	{
		int left = -1;
		int right = -1;
		//find the first empty slot
		while(1)
		{
			int j,k;
			for(j=N-1; j>=0; j--)
			{
				if(board[i][j] == '.')
				{
					right = j;
					break;
				}
			}
			for(k=j-1; k>=0; k--)
			{
				if(board[i][k] != '.')
				{
					left = k;
					break;
				}
			}
			if(right == -1 || left == -1)
				break;
			
			for(int l=left; l>=0; l--)
			{
				board[i][right]=board[i][l];
				board[i][l]='.';
				right--;
			}
			right = -1;
			left = -1;
		}
	}
}

bool check(const int K, const VVC& board, const char r, const int i, const int j)
{
	int N = board[0].size();
	if(board[i][j] != r) return false;
	int len = 0;

	//right
	len = 0;
	for(int k=j;k<N;k++)
	{
		if(board[i][k] != r)
			break;
		len++;
		if(len==K)
			return true;
	}

	//down
	len =0;
	for(int k=i; k<N; k++)
	{
		if(board[k][j] != r)
			break;
		len++;
		if(len==K)
			return true;
	}

	//down right
	len = 0;
	{
		int k,l;
		k=i;
		l=j;
		while(k<N && l <N)
		{
			if(board[k][l]!=r)
				break;
			len++;
			if(len==K)
				return true;
			k++;
			l++;
		}
	}

	//down left
	len=0;
	{ 
		int k,l;
		k=i;
		l=j;
		while(k<N && l>=0)
		{
			if(board[k][l] != r)
				break;
			len++;
			if(len==K)
				return true;
			k++;
			l--;
		}
	}
	return false;
}


string process(VVC& board, int K)
{
	int N=board[0].size();

	int blue = 0;
	int red = 0;
	for(int i=0; i<N; i++)
		for(int j=0; j<N; j++)
		{
			if(check(K,board,'R',i,j))
				red = 1;
			if(check(K,board,'B',i,j))
				blue = 1;
		}
	if(red == 1 && blue == 0)
		return "Red";
	if(red ==1 && blue == 1)
		return "Both";
	if(red==0 && blue == 1)
		return "Blue";
	if(red==0 && blue == 0)
		return "Neither";
}


void wei_print(const VVC& board)
{
	int N=board[0].size();
	cout<<endl;
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<N; j++)
			cout<<board[i][j];
		cout<<endl;
	}
}

main()
{
	int T;
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		cout<<"Case #"<<i<<": ";
		int K,N;
		cin>>N>>K;
		VVC board(N,VC(N));
		for(int j=0; j<N; j++)
		{
			for(int k=0; k<N; k++)
				cin>>board[j][k];
		}
//		wei_print(board);//debug
		rotate(board);
//		wei_print(board);//debug
		cout<<process(board,K)<<endl;
	}
}

		


