#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

const int SIZE = 200;
string grid[SIZE];
int N;

struct state{
	double wp, owp, oowp;
} arr[SIZE];

double getWP(int i, int x){
	int cnt = 0;
	double r = 0;
	for(int j = 0 ; j < N ; j++){
		if(grid[i][j] == '.')continue;
		if(j == x)continue;
		cnt++;
		if(grid[i][j]=='1')r++;
	}
	if(cnt)r/=cnt;
	return r;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small-attempt0.out", "wt", stdout);
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		cerr << "Solving testcase " << t+1 << endl;

		cin >> N;
		for(int i = 0 ; i < N ; i++){
			cin >> grid[i];
			arr[i].wp = arr[i].owp = arr[i].oowp = 0;
		}

		//wp
		for(int i = 0 ; i <N; i++)
			arr[i].wp = getWP(i, -1);
		//owp
		for(int i = 0 ; i <N; i++){
			int cnt = 0;
			for(int j = 0 ; j < N ; j++){
				if(grid[i][j] == '.')continue;
				cnt ++;
				arr[i].owp += getWP(j, i);
			}
			if(cnt)arr[i].owp /= cnt;
		}
		//oowp
		for(int i = 0 ; i <N; i++){
			int cnt = 0;
			for(int j = 0 ; j < N ; j++){
				if(grid[i][j] == '.')continue;
				cnt++;
				arr[i].oowp += arr[j].owp;
			}
			if(cnt)arr[i].oowp /= cnt;
		}

		cout << "Case #" << t+1 << ": "<<endl;
		for(int i = 0 ; i < N ; i++)
			printf("%.9lf\n", 0.25 * arr[i].wp + 0.50 * arr[i].owp + 0.25 * arr[i].oowp);
	}

	return 0;
}
