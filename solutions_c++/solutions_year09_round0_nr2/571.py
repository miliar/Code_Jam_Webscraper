#include<iostream>
#include<vector>

using namespace std;
int a[120][120];
int b[120][120];
char rez[120][120];
vector<pair<int, int> > q;

void solve(int test, int n, int m){
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));


	for (int i = 0; i <= n+1; i++)
		for (int j = 0; j <= m+1; j++){
			a[i][j] = -1;
			b[i][j] = 0;
			rez[i][j] = '0';
		}


	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			cin >> a[i][j];


	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++){
			int direct = 0;
			int mini = 0;
			if (a[i-1][j] != -1 && a[i][j] > a[i-1][j]){
				direct = 1;
				mini = a[i-1][j]; 
		        }

		        if (a[i][j-1] != -1 && a[i][j] > a[i][j-1]){
		        	if (direct == 0){
		        		direct = 2;
		        		mini = a[i][j-1];
		        	} else if(a[i][j-1] < mini)
		        	{
		        		direct = 2;
		        		mini = a[i][j-1];
		        	}
		        }
		        if (a[i][j+1] != -1 && a[i][j] > a[i][j+1]){
		        	if (direct == 0){
		        		direct = 3;
		        		mini = a[i][j+1];
		        	} else if(a[i][j+1] < mini)
		        	{
		        		direct = 3;
		        		mini = a[i][j+1];
		        	}
		        }
		        if (a[i+1][j] != -1 && a[i][j] > a[i+1][j]){
		        	if (direct == 0){
		        		direct = 4;
		        		mini = a[i+1][j];
		        	} else if(a[i+1][j] < mini)
		        	{
		        		direct = 4;
		        		mini = a[i+1][j];
		        	}
		        }
		        b[i][j] = direct;
		}

	
	char t = 'a';
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			if (rez[i][j] == '0'){
				q.clear();
				rez[i][j] = t;
				t++;
				q.push_back(make_pair(i,j));
				int uk = 0;
				while (uk < q.size()){
					int x = q[uk].first;
					int y = q[uk].second;
					if (b[x][y] == 1 && rez[x-1][y] == '0'){
						q.push_back(make_pair(x-1,y));
						rez[x-1][y] = rez[x][y];
				        }
					if (b[x][y] == 2 && rez[x][y-1] == '0'){
						q.push_back(make_pair(x,y-1));
						rez[x][y-1] = rez[x][y];
				        }
					if (b[x][y] == 3 && rez[x][y+1] == '0'){
						q.push_back(make_pair(x,y+1));
						rez[x][y+1] = rez[x][y];
				        }
					if (b[x][y] == 4 && rez[x+1][y] == '0'){
						q.push_back(make_pair(x+1,y));
						rez[x+1][y] = rez[x][y];
				        }

//--------------------------------------------
				        if (b[x][y+1] == 2 && rez[x][y+1] == '0'){
						q.push_back(make_pair(x,y+1));
						rez[x][y+1] = rez[x][y];
				        }
				        if (b[x][y-1] == 3 && rez[x][y-1] == '0'){
						q.push_back(make_pair(x,y-1));
						rez[x][y-1] = rez[x][y];
				        }
				        if (b[x+1][y] == 1 && rez[x+1][y] == '0'){
						q.push_back(make_pair(x+1,y));
						rez[x+1][y] = rez[x][y];
				        }
				        if (b[x-1][y] == 4 && rez[x-1][y] == '0'){
						q.push_back(make_pair(x-1,y));
						rez[x-1][y] = rez[x][y];
				        }

					uk++;
				}
			}
	cout << "Case #" << test + 1 << ":" << endl;
	for (int i = 1; i <= n; i++){
		for (int j = 1; j <= m; j++)
			cout << rez[i][j] << " ";
		cout << endl;
	}

}

int main(){
	int test;
	cin >> test;
	for (int i = 0; i < test; i++){
		int n, m;
		cin >> n >> m;
		solve(i,n,m);
	}
	return 0;
}
