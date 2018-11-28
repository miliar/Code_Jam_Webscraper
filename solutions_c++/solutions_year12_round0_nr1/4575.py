#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int C;
	char ch;
	scanf("%d\n", &C);
	
	char mapping[] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

	for ( int i = 0; i < C; i++ ) {
		cout << "Case #" << i+1 << ": ";	
		while ( ( ch = getchar() ) != '\n' ) {
			if ( ch == ' ' )
				cout << " ";
			else
				cout << (mapping[ch-97]);
		}
		cout << endl;
	}

	return 0;
}
