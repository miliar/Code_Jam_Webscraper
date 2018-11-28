#include<iostream>
#include<vector>
#include<string>
using namespace std;

int getAmari( int n, string s ){
	if( n == 2 ){
		char c = s[s.size()-1] - '0';
		c %= 2;
		//cout << n << "%" << s << " " << (int)c << endl;
		return c;
	}
	if( n == 3 ){
		int ans = 0;
		for( int i = 0; i < s.size(); i ++ ){
			char c = s[i] - '0';
			ans += c;
		}
		ans %= 3;
		return ans;
	}
	if( n == 5 ){
		char c = s[s.size()-1] - '0';
		c %= 5;
		return c;
	}

	int kSage = 0;
	for( int i = 0; i < s.size(); i ++ ){
		char c = s[i] - '0';
		int a = kSage * 10 + c;
		int b = a / n;
		kSage = a  - b * n;
	}
	int ans = kSage;
	ans %= n;
	return ans;
}

long long int getugly( int n, string s ){
	long long int t[s.size()+1][n];
	for( int j = 0; j < n; j++ ){
		t[0][j] = 0;
	}
	t[0][0] = 1;
	
	for( int i = 0; i < s.size(); i++ ){
		for( int j = 0; j < n; j++ ){
			t[i+1][j] = 0;
		}
		for( int j = 0; j <= i; j++ ){
			for( int k = 0; k < n; k++ ){
				string ss = s.substr( j, i-j+1 );
				int amari = getAmari( n, ss );
				t[i+1][(k+amari)%n] += t[j][k];
				if( j != 0 )
					t[i+1][(n+k-amari)%n] += t[j][k];
			}
		}
	}
	for( int j = 0; j < n; j++ ){
		for( int i = 0; i <= s.size(); i++ ){
			//cout << t[i][j] << " ";
		}
		//cout << endl;
	}
	//cout << n << ": " << t[s.size()][0] << endl;
	return t[s.size()][0];
}


int main(){
	int n;
	cin >> n;
	cin >> ws;
	for( int i = 0; i< n; i++ ){
		string s;
		getline( cin, s );

		long long int ans = 0;
		ans += getugly( 2, s );
		ans += getugly( 3, s );
		ans += getugly( 5, s );
		ans += getugly( 7, s );

		ans -= getugly( 6, s );
		ans -= getugly( 10, s );
		ans -= getugly( 14, s );
		ans -= getugly( 15, s );
		ans -= getugly( 21, s );
		ans -= getugly( 35, s );
		

		ans += getugly( 30, s );
		ans += getugly( 42, s );
		ans += getugly( 70, s );
		ans += getugly( 105, s );

		ans -= getugly( 210, s );

		cout << "Case #" << (i+1) << ": " << ans << endl;
	}
}
