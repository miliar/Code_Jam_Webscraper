#include<iostream>
#include<set>
using namespace std;

#define big long long
big x[100000], y[100000];
big n, A, B, C, D, x0, y0, M;

int main(){

	//freopen("1.in", "rt", stdin);
	freopen("A-small.in", "rt", stdin);
	freopen("A-small.out", "wt", stdout);
	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);
	
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		
		cin >> n>> A>> B>> C>> D>> x0>> y0>> M;
		big X = x0, Y = y0;
		int i = 0;
		x[i] = X;
		y[i] = Y;
		for(i = 1 ; i < n ; i++){
			X = (A * X + B) %M;
			Y = (C * Y + D) %M;
			x[i] = X;
			y[i] = Y;
		}
		
		big r = 0;
		for(i = 0 ; i < n ; i++)
			for(int j = i+1 ; j < n ; j++)
				for(int k = j+1 ; k < n ; k++){
					if((x[i]+x[j]+x[k])%3 == 0 &&
					(y[i]+y[j]+y[k])%3 == 0)
						r++;
				}
		
		cout << "Case #" << t+1 << ": " << r << endl;
	}

	return 0;	
}
