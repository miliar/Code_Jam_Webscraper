#include <iostream>
#include <cstdio>

using namespace std;

int n,l,h;
int freq[10000];

int main(){
	int tc,t;
	int i,j,k;
	int f;
	bool can,done;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tc;
	for (t=0; t<tc; t++){
		cin >> n >> l >> h;
		for (i=0; i<n; i++)
			cin >> freq[i];

		done = false;
		for (i=l; i<h+1; i++){
			can = true;
			for (j=0; j<n; j++){
				if ((freq[j]%i!=0)&&(i%freq[j]!=0))
					can = false;
			}
			if (can){
				done = true;
				f=i;
				i=h+1;
			}
		}

		printf("Case #%d: ", t+1);
		if (done)
			cout << f << endl;
		else
			cout << "NO\n";
	}

	return 0;
}