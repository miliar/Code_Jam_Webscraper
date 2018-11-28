#include<iostream>
#include<vector>

using namespace std;
int main2()
{
	int R,C;
	cin >> R >> C;
	bool poss=true;
	vector<string> v(R);
	string tmp;
	getline(cin,tmp);
	for(int i=0;i<R;i++)
	{
		getline(cin,tmp);
		v[i]=tmp;
	}
	for(int i=0;i<R;i++)
	{
		for(int j=0;j<C;j++)
		{
			if(v[i][j]=='#')
			{
				v[i][j]='/';
				if(i+1 >= R || j+1>=C || v[i+1][j]!='#' || v[i+1][j+1]!='#' || v[i][j+1]!='#')
				{
					poss=false;
					break;
				}
				v[i+1][j]='\\';
				v[i][j+1]='\\';
				v[i+1][j+1]='/';
			}
		}
	}
	
	if(!poss)
	{
		cout << "Impossible" << endl;
		return 1;
	}
	for(int i=0;i<R;i++)
		cout << v[i] << endl;
		
}
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		cout << "Case #" << t << ":" <<endl;
		main2();
	}
}

