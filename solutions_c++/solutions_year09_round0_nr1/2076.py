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


int main()
{

int L, D, N;

fstream In("A-large.in", ios::in);
fstream Out("A-large.out", ios::out);

In >> L >> D >> N;

vector<vector<int> > board(D, vector<int> (L, 0));

for(int i=0; i<D; i++)
{
string temp;
In >> temp;

for(int j=0; j<L; j++)
	board[i][j] = 1<<(temp[j]-'a');

}

vector<int> word(L, 0);

for(int i=0; i<N; i++)
{
	Out << "Case #" << i+1 << ": ";
	string temp;
	In >> temp;
	int k = 0;
	int ret = 0;
	for(int j=0; j<L; j++,k++)
	{
		int m = 0;
		if(temp[k]=='(')
		{
			while(temp[++k]!=')')
			{
				m |= 1<<(temp[k]-'a');
			}
		}
		else m = 1<<(temp[k]-'a');
		word[j] = m;
	}

	for(int j=0; j<D; j++)
	{
		int k;
		for(k=0; k<L; k++)
			if(word[k] & board[j][k]) continue;
			else break;
		if(k==L) ret++;
	}

	Out << ret << endl;
}

In.close();

Out.close();

return 0;

}
