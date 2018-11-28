#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>


using namespace std;


void solve(int n,int m,int a){

	int x1 = 0;
	int y1 = 0;

			for (int x2 = 0;x2 <= n; ++x2)
				for (int y2 = 0;y2 <= m; ++y2)
					for (int x3 = 0;x3 <= n; ++x3)
						for (int y3 = 0;y3 <= m; ++y3){
							int xa = x2 - x1;
							int xb = x3 - x1;
							int ya = y2 - y1;
							int yb = y3 - y1;

							if (abs(xa*yb - xb*ya) == a){
								cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
								return;
							}
						}
	cout << "IMPOSSIBLE"<<endl;

}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int test;
	cin >> test;

	for (int t = 1;t <= test; ++t){
		int n,m,a;
		cin >> n >> m >> a;		
		cout << "Case #"<<t<<": ";
		solve(n,m,a);		
	}

	return 0;
}