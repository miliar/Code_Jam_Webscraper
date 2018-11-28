#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long int lli;
#define ZER(X) memset(X,0,sizeof(X));

const int MAX = 22;
int M[MAX];

void swap(int & a, int & b){
	int t = a;
	a = b;
	b = t;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int _;
	cin >> _;
	char buf[200];
	cin.getline(buf,sizeof(buf));
	for(int __=0; __<_; ++__){
		cin.getline(buf,sizeof(buf));
		//cout << buf << endl;

		ZER(M);
		int len = strlen(buf);
		for(int i=0; i<len; i++){
			M[i+1]=buf[i]-'0';
		}

		//for(int i=0; i<=len; i++){
		//	cout << M[i] << ' ';
		//}

		//cout << endl;

		int i;
		
		for(i = len-1; i>=0; --i){
			if(M[i]<M[i+1])
				break;
		}

		std::sort(M+i+1,M+len+1);

		int j;
		for(j = i+1; j<len+1; j++){
			if(M[j]>M[i])
				break;
		}

		swap(M[i],M[j]);
		std::sort(M+i+1,M+len+1);

		//cout << i << ' ' << j << endl;


		cout << "Case #" << __+1 << ": ";
		if(M[0])
			cout << M[0];
		for(int i=1; i<=len; i++){
			cout << M[i];
		}
		cout << endl;


	}
	return 0;
}