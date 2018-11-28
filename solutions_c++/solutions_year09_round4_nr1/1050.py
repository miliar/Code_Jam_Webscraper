#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long int lli;
#define ZER(X) memset(X,0,sizeof(X));

const int MAX = 60;
int M[MAX][MAX];
int n;

int find(int k){
	for(int i=k;i<n;++i){
		int j;
		for(j=k+1;j<n;j++)
			if(M[i][j])
				break;
		if(j>=n)
			return i;
	}
}

void swap(int &i, int &j){
	int t = i;
	i = j;
	j = t;
}

void swapR(int i, int j){
	for(int k=0; k<n; ++k)
		swap(M[i][k],M[j][k]);
}


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int _;
	cin >> _;
	for(int __=0; __<_; ++__){
		cin >> n;
		char buf[MAX+2];
		cin.getline(buf,MAX);
		for(int i=0; i<n; ++i){
			cin.getline(buf,MAX);
			//cout << buf << endl;
			for(int j=0; j<n; ++j){
				M[i][j]=buf[j]-'0';
			}
		}

		int sum = 0;
		for(int i=0; i<n; ++i){
			int x = find(i);
			//cout << x << endl;
			//sum += x-i;
			for(int j=x; j>i; --j){
				sum++;
				swapR(j,j-1);
			}
			
			
		}
		//cout << endl;


		cout << "Case #" << __+1 << ": " << sum <<endl;
		//for(int i=0; i<n; ++i){
		//	for(int j=0; j<n; ++j)
//				cout << M[i][j] << ' ';
//			cout << endl;
		//}

	}
	return 0;
}