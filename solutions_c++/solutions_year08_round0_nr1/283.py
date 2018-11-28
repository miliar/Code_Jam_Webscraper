#include<iostream>
#include<string>
using namespace std;


int main(){
	int n;
	cin >> n;
	for( int m = 0; m < n; m++ ){
		int s;
		cin >> s;
		string se[s];
		cin >> ws;
		for( int i=0; i<s; i++ ){
			getline(cin, se[i]);
		}
		int q;
		cin >> q;
		string sq[q];
		cin >> ws;
		for( int i=0; i<q; i++ ){
			getline(cin, sq[i]);
		}

		int ans = 0;
		int c = 0;
		int flag[s];
		fill_n( flag, s, 0 );
		for( int j=0; j<q; j++ ){
			for( int i=0; i<s; i++ ){
				if( !flag[i] && se[i] == sq[j] ){
					c++;
					flag[i] = 1;
					if( c == s ){
						ans ++ ;
						fill_n( flag, s, 0 );
						c = 1;
						flag[i] = 1;
					}
					break;
				}
			}
		}

		cout << "Case #" << (m+1) << ": " << ans << endl;
	}
}
