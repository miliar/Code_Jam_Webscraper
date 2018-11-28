#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef struct{
	char a;
	char b;
	char c;
}_C;

const int max_c = 40;
const int max_d = 30;
int nc, nd, nsz;
_C C[max_c];
_C D[max_d];
char input[105];

void Output(int n);

void Invoke_C(int idx)
{
	if( idx == 0 ) return;
	for( int j = 0; j < nc; j++ ){
		if( C[j].a == input[idx] ){
			int tmp = idx-1;
			while( input[tmp] == -1 ){
				tmp--;
				if( tmp == 0 ) break;
			}
			if( C[j].b == input[tmp] ){
				input[tmp] = C[j].c;
				input[idx] = -1;
				return;
			}
		}
		if( C[j].b == input[idx] ){
			int tmp = idx-1;
			while( input[tmp] == -1 ){
				tmp--;
				if( tmp == 0 ) break;
			}
			if( C[j].a == input[tmp] ){
				input[tmp] = C[j].c;
				input[idx] = -1;
				return;
			}
		}
	}
}

void Invoke_D(int idx)
{
	for( int j = 0; j < nd; j++ ){
		if( D[j].a == input[idx] )
		for(int i = 0; i < idx; i++ ){ 
			if( D[j].b == input[i] ){
				for(int k = 0; k <= idx; k++ ){
					input[k] = -1;
				}
				return;
			}
		}
		if( D[j].b == input[idx] )
		for(int i = 0; i < idx; i++ ){ 
			if( D[j].a == input[i] ){
				for(int k = 0; k <= idx; k++ ){
					input[k] = -1;
				}
				return;
			}
		}
	}
}

void Solve()
{
	for( int i = 1; i < nsz; i++ ){
		Invoke_C(i);
		Invoke_D(i);
	}
}

void Output(int n)
{
	cout << "Case #" << n+1 << ": [";
	bool flag = true;
	for( int i = 0; i < nsz; i++ ){
		if( input[i] != -1 ){
			if( !flag ) { cout << ", "; flag = false; }
			else flag = false;
			cout << input[i];
		}
	}
	cout << "]" << endl;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int t;
	cin >> t;
	for( int i = 0; i < t; i++ ){
		cin >> nc;
		for( int j = 0; j < nc; j++ ){
			string tmp;
			cin >> tmp;
			C[j].a = tmp[0];
			C[j].b = tmp[1];
			C[j].c = tmp[2];
		}
		cin >> nd;
		for(int j = 0; j < nd; j++ ){
			string tmp;
			cin >> tmp;
			D[j].a = tmp[0];
			D[j].b = tmp[1];
		}
		cin >> nsz;
		cin >> input;
		Solve();
		Output(i);
	}

	return 0;
}
