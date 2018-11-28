// Paste me into the FileEdit configuration dialog

#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <iostream>
#include <cmath>
#include <ctime>
#include <queue>

using namespace std;

const int MAX = 10000;

vector<pair<int,double>> PointsTotal;

int W, L, U, G, n, m, y, x;

vector<pair<int,int>> PointsFirst[2];

bool revert[100][100];
bool has[100][100];
int sym_x[1256];
int sym_y[1256];
char a[100][100];

bool ook();

int main(int argc, char *argv[]) {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_case_count;
	cin >> test_case_count;

	for (int test_case = 1; test_case<=test_case_count; ++test_case)
	{	
		sym_x['|']=0; sym_y['|']=1;
		sym_x['-']=1; sym_y['-']=0;
		sym_x['/']=1; sym_y['/']=-1;
		sym_x['\\']=1; sym_y['\\']=1;
		cin>>n>>m;
		gets(a[0]);		
		for (int i = 0; i < n; ++i){
			gets(a[i]);
		}
		int res=0;
		for (int k = 0; k < 1<<(n*m); ++k)
		{
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < m; ++j) {
					revert[i][j] = !!(k&(1<<(m*i+j)));
				}
			if(ook()){
				++res;
			}
		}
		cout << "Case #" << test_case << ": ";		
		cout<<res<<endl;					
	}

	fclose(stdout);
}

bool ook()
{
	for (int i = 0; i < n; ++i)
		for(int j = 0; j < m;++j)
			has[i][j]=false;	
	for (int i = 0; i < n; ++i) {
		for(int j = 0; j < m;++j) {
			x=sym_x[a[i][j]];
			y=sym_y[a[i][j]];

			if(revert[i][j])
			{
				x=-x;
				y=-y;
			}
			
			int a=(i+y+n)%n;
			int b=(j+x+m)%m;
			
			if(has[a][b])
				return false;
			has[a][b]=true;
		}
	}
	return true;
}
