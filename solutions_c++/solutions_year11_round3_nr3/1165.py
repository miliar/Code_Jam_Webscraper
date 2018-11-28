#include<string>
#include<fstream>
#include<iostream>

using namespace std;

typedef unsigned long long LL;

#define MAX	100000

LL a[MAX];

int main(){

	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());

	LL ntc,r,c,l,h,n;

	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n >> l >> h;
		for (int i=0;i<n;i++)
			cin >> a[i];
		LL res = -1;
		for (int k=l;k<=h;k++){
			int i;
			for (i=0;i<n;i++){
				if (a[i]%k && k%a[i])
					break;
			}
			if (i==n){
				res = k;
				break;
			}
		}
		cout << "Case #" << tc << ": ";		
		if (res==-1)
			cout << "NO" << endl;
		else
			cout << res << endl;

	}

	return 0;
}