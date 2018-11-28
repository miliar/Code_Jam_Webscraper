#include <iostream>
#include <string>
#include <vector>

using namespace std;

void main1( int t1 )
{
	int i, j, k, flag, x, o, t;
	vector<string> v;
	flag = 0;
	char m[4][4];
	string s1, s2, s3, s4, s;
	s1 = "X won";
	s2 = "O won";
	s3 = "Game has not completed";
	s4 = "Draw";
	char ch;
	
	for ( i = 0; i < 4; i ++ ) {
		cin >> s;
		v.push_back( s );
		if ( flag == 0 ) {
			for ( j = 0; j < 4; j ++ )  {
				if ( s[j] == '.' ) {
					flag = 1;
				}
			}
		}
	}
	
	x = 0;
	o = 0;
	t = 0;
	
	for ( i = 0; i < 4; i ++ ) {
		if ( v[i][i] == 'O' ) {
			o ++;
		} else
		if ( v[i][i] == 'X' ) {
			x ++;
		} else
		if ( v[i][i] == 'T' ) {
			t ++;
		}
	}
	
	if ( o == 4 || ( o == 3 && t == 1 ) ) {
		cout << "Case #" << t1 << ": " << s2 << "\n";
		return;
	}
	if ( x == 4 || ( x == 3 && t == 1 ) ) {
		cout << "Case #" << t1 << ": " << s1 << "\n";
		return ;
	}

	x = 0;
	o = 0;
	t = 0;
	
	for ( i = 0; i < 4; i ++ ) {
		if ( v[i][3 - i] == 'O' ) {
			o ++;
		} else
		if ( v[i][3 - i] == 'X' ) {
			x ++;
		} else
		if ( v[i][3 - i] == 'T' ) {
			t ++;
		}
	}
	
	if ( o == 4 || ( o == 3 && t == 1 ) ) {
		cout << "Case #" << t1 << ": " << s2 << "\n";
		return;
	}
	if ( x == 4 || ( x == 3 && t == 1 ) ) {
		cout << "Case #" << t1 << ": " << s1 << "\n";
		return ;
	}
	
	for ( j = 0; j < 4; j ++ ) {
		x = 0;
		o = 0;
		t = 0;
		
		for ( i = 0; i < 4; i ++ ) {
			if ( v[j][i] == 'O' ) {
				o ++;
			} else
			if ( v[j][i] == 'X' ) {
				x ++;
			} else
			if ( v[j][i] == 'T' ) {
				t ++;
			}
		}
	
		if ( o == 4 || ( o == 3 && t == 1 ) ) {
			cout << "Case #" << t1 << ": " << s2 << "\n";
			return;
		}
		if ( x == 4 || ( x == 3 && t == 1 ) ) {
			cout << "Case #" << t1 << ": " << s1 << "\n";
			return ;
		}
		
		x = 0;
		o = 0;
		t = 0;
		
		for ( i = 0; i < 4; i ++ ) {
			if ( v[i][j] == 'O' ) {
				o ++;
			} else
			if ( v[i][j] == 'X' ) {
				x ++;
			} else
			if ( v[i][j] == 'T' ) {
				t ++;
			}
		}
	
		if ( o == 4 || ( o == 3 && t == 1 ) ) {
			cout << "Case #" << t1 << ": " << s2 << "\n";
			return;
		}
		if ( x == 4 || ( x == 3 && t == 1 ) ) {
			cout << "Case #" << t1 << ": " << s1 << "\n";
			return ;
		}
	}
	
	if ( flag ) {
		cout << "Case #" << t1 << ": " << s3 << "\n";
	} else {
		cout << "Case #" << t1 << ": " << s4 << "\n";
	}
	
	return;
}

int main()
{
	int i, t;
	cin >> t;
	
	for ( i = 1; i <= t; i ++ ) {
		main1( i );
	}
	
	return 0;
}