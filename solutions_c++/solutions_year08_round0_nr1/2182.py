#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main () 
{
	FILE *fp, *fp2;
	int flag = 0;
	int dcnt = 0;
	int rcnt = 0;
	int nCnt, nCnt2;
	vector <string> ses;
	vector <string> wd;
	vector <string> se;
	char szBuf [ 256 ];
	string strtemp;

	if ( ! ( fp = fopen ( "input.txt", "r" ) ) ) {
		cout << "error in opening input.txt" << endl;
		return 0;

	}
	fp2 = fopen ( "output.txt", "w" );
	fscanf ( fp, "%d\n", &nCnt );
	for ( int i = 0; i < nCnt; i++ ) {
		dcnt++;
		fscanf ( fp, "%d\n", &nCnt2 );
		se.clear ();
		cout << "se:" << endl;
		for ( int j = 0; j < nCnt2; j++ ) {
//			fscanf ( fp, "%s\n", szBuf );
			fgets ( szBuf, sizeof ( szBuf ), fp );
			se.push_back ( szBuf );
			cout << szBuf;

		}
		wd.clear ( );
		cout << "wd:" << endl;
		fscanf ( fp, "%d\n", &nCnt2 );
		for ( int j = 0; j < nCnt2; j++ ) {
//			fscanf ( fp, "%s\n", szBuf );
			fgets ( szBuf, sizeof ( szBuf ), fp );
			strtemp = szBuf;
			cout << szBuf;
			flag = 0;
			for ( int k = 0; k < wd.size ( ); k++ ) {
				if ( wd [ k ] == strtemp ) {
					flag = 1;
					break;

				}

			}
			if ( ! flag ) {
				wd.push_back ( strtemp );

			}
			if ( wd.size ( ) == se.size ( ) ) {
				rcnt++;
				wd.clear ( );
				wd.push_back ( strtemp );

			}

		}
		fprintf ( fp2, "Case #%d: %d\n", dcnt, rcnt );
		cout << rcnt << "\n----------------------" << endl;
		rcnt = 0;

	}
	fclose ( fp );
	fclose ( fp2 );
	return 0;


}
