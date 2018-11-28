#include<iostream>
#include<vector>
using namespace std;


vector<int> getBin(int val)
{
	vector<int> v;
	if(val & 8)
		v.push_back(1);
	else
		v.push_back(0);
	
	if(val & 4)
		v.push_back(1);
	else
		v.push_back(0);
	
	if(val & 2)
		v.push_back(1);
	else
		v.push_back(0);
	
	if(val & 1)
		v.push_back(1);
	else
		v.push_back(0);
	
	return v;
	

}


bool check(vector<vector<int> > board, int i, int j, int size)
{
	//check cols
	
	//cout << "col check " << endl;
	for(int ii = i; ii < i + size;ii++)
	{
		if(ii >= board.size())
			return false;
		
		int last = -2;
		for(int jj = j; jj < j + size;jj++)
		{
			if(jj >= board[ii].size() )
				return false;
			
			if(board[ii][jj] == last)
				return false;
			if(board[ii][jj] == -1)
				return false;
			last = board[ii][jj];
		}
	}
	
	
	//cout << "row check " << endl;
	for(int jj = j; jj < j + size;jj++)
	{
		if(jj >= board[0].size())
			return false;
		
		int last = -2;
		for(int ii = i; ii < i + size;ii++)
		{
			if(ii >= board.size() )
				return false;
			if(board[ii][jj] == -1)
				return false;
			if(board[ii][jj] == last)
				return false;
			
			last = board[ii][jj];
		}
	}
	//cout << "over " << endl;
	return true;

}

void cut(vector<vector<int> > & board, int i, int j, int size)
{
	//check cols
	
	
	for(int ii = i; ii < i + size;ii++)
	{
	
		for(int jj = j; jj < j + size;jj++)
		{
			board[ii][jj] = -1;
		}
	}
	








}


vector<int> cutBoard(vector<vector<int> > board, int startSize)
{

	//cout << "cutBoard called " << endl;
	for(int size = startSize; size >= 1; size--)
	{
		for(int i = 0; i < board.size();i++)
		{
			for(int j = 0; j < board[i].size();j++)
			{
				if(board[i][j] == -1)
					continue;
				if( check(board, i, j, size) )
				{
					vector<int> v;
					v.push_back(i);
					v.push_back(j);
					v.push_back(size);
					return v;
				
				
				
				}
			}
		}
	}
	
	
	vector<int> q;
	//cout << "cutBoard returned " << endl;
	return q;
	
	
}
	
	


int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T;t++)
	{
		int M, N;
		cin >> M >> N;
		vector<string> v;
		for(int i = 0; i < M;i++)
		{
			string g;
			cin >> g;
			v.push_back(g);
		}
		//cout << "Passed" << endl;
		vector< vector<int> > board;
		for(int i = 0; i < M;i++)
		{
			vector<int> x;
			for(int j = 0; j < v[i].size();j++)
			{
				int val;
				if(v[i][j] >= '0' && v[i][j] <= '9')
					val = v[i][j] - '0';
				else
					val = 10 + (v[i][j] - 'A');
				
				vector<int> temp = getBin(val);
				for(int k = 0; k < temp.size();k++)
					x.push_back(temp[k]);
			}
			board.push_back(x);
		}
		
		//cout << "passed 2" << endl;
		int ans[1000];
		int numDiff = 0;
		memset(ans,0,sizeof(ans));
		int startSize = min(M,N);
		while(1)
		{
			vector<int> blah = cutBoard(board, startSize);
			if(blah.size() == 0)
				break;
			
			
			cut(board, blah[0], blah[1], blah[2]);
			
			if(ans[blah[2]] == 0)
				numDiff++;
			ans[blah[2]]++;		
			startSize = blah[2];
		}
		
		cout << "Case #" << t+1 << ": " << numDiff << endl;
		for(int i = 999; i >= 1;i--)
		{
			if(ans[i] != 0)
				cout << i << " " <<  ans[i] << endl;
		}
		
	}


}
