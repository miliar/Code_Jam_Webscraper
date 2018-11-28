#include<iostream>
#include<fstream>

using namespace std;

int f[200];
int c[200];
int sum;
int n;
int ans;

bool decide() {
	int a=0, b=0;
	for (int i=0; i<n; i++) {
		if (f[i]) 	a ^= c[i];
		else 		b ^= c[i];
	}
	//cout << a << " " << b << endl;
	if (a==b) 	return true;
	else		return false;
}

void solve(int k) {
	if (n==k) {
		if (decide()) {
			int ret=0;
			for (int i=0; i<n; i++) {
				if (f[i]) {
					ret+=c[i];
				}
			}
			if (ret==0 || sum==ret) return ;
			if (sum-ret > ans) ans = sum-ret;
			if (ret > ans) ans = ret;
		}
		return ;
	}
	int temp;
	for (int t=0; t<2; t++) {
		f[k]=t;
		solve(k+1);
		f[k]=0;
	}
	return ;
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for (int h=0; h<t; h++) {
		fin >> n;
		sum=0;
		ans=-1;
		memset(f, 0, sizeof(f));
		for (int i=0; i<n; i++) {
			fin >> c[i];
			sum += c[i];
		}
		solve(0);
		
		fout << "Case #" << h+1 << ": ";
		if (ans==-1) 	fout << "NO" << endl;
		else 			fout << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
