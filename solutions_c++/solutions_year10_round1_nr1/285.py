#include <iostream>
#include <cstring>
using namespace std;

bool onboard(int x,int y, int n){
	if (x>=n || x<0) return false;
	if (y>=n || y<0) return false;
	return true;
}

const int di[4] = {-1, 0,+1,-1};
const int dj[4] = {+1,+1,+1, 0};

int main(){
	char a[50][50];
	int b[50][50][4];
	int n,k,t,test,result;
	int dx,dy;
	// Read test case
	cin >> t;
	test  = 0;
	while (test < t){
		// write test
		test++;
		cout << "Case #" << test << ": ";
		// readin table
		cin >> n >> k;
		cin.getline(a[0],100);
		for (int i =0;i<n;i++){
			cin.getline(a[i],100);
			int now = n-1;
			for (int j=n-1;j>=0;j--)
				if (a[i][j] != '.') a[i][now--] = a[i][j];
			while (now >= 0) a[i][now--] = '.';
		}
		
		// initialize
		result  = 0;
		for (int j=n-1;j>=0;j--)
		for (int i=0;i<n;i++){
			if (a[i][j]=='.'){
				b[i][j][0] = 0;
				b[i][j][1] = 0;
				b[i][j][2] = 0;
			} else {
				for (int ii = 0;ii<4;ii++){
					dx = i + di[ii];
					dy = j + dj[ii];
					b[i][j][ii] = 1;
					if (onboard(dx,dy,n) && (a[dx][dy] == a[i][j])){
						b[i][j][ii] += b[dx][dy][ii];
						//cerr << dx << dy;
					};
					//cerr << i << "," << j << b[i][j][ii] << endl;
					if (b[i][j][ii] >= k){
						if (a[i][j] == 'R' && result != 1){
							result += 1;
						};
						if (a[i][j] == 'B' && result != 2){
							result += 2;
						};
						if (result == 3) break;
					}
				}
			}
			if (result == 3) break;
		}
		switch (result){
			case 0: cout << "Neither" << endl;break;
			case 1: cout << "Red" << endl;break;
			case 2: cout << "Blue" << endl;break;
			case 3: cout << "Both" << endl;break;
		}
	}
	return 0;
}
