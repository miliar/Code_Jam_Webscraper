#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> M;

int check(string &tmp)
{
	int ret = 0;
	for (int i=0; i<M.size(); i++)
	{
		int pos = 0;
		int j;
		for (j=0; j<M[i].size(); j++)
		{
			if (tmp[pos] == '(')
			{
				bool was = false;
				while (tmp[pos] != ')')
				{
					if (tmp[pos] == M[i][j])
						was = true;
					pos++;
				}
				if (!was)
					break;
			}
			else
				if (tmp[pos] != M[i][j])
					break;
			pos++;
		}			
		if (j == M[i].size())
			ret++;
	}
	return ret;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int L, D, N;
	M.clear();
	cin >> L >> D >> N;
	M.resize(D);
	for (int i=0; i<D; i++)
		cin >> M[i];
	for (int I=1; I<=N; I++)
	{
		string tmp;
		cin >> tmp;
		cout << "Case #" << I << ": " << check(tmp) << endl;
	}
}