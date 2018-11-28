//#include <math.h>
#include <map.h>
#include <list.h>
#include <vector.h>
#include <iostream.h>
#include <iomanip.h>
//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused

int main(int argc, char* argv[])
{
	int N, L, D;
	cin >> L >> D >> N;
        vector<long> dict = vector<long>(D*L);
	for( int i = 0; i < D; ++i ) {
        	for( int j = 0; j < L; ++j ) {
		        char ch;
                        cin >> ch;
                        dict[i*L + j] = (1L << (ch - 'a'));
                }
	}

	for( int i = 0; i < N; ++i ) {
                vector<long> word = vector<long>(L);
        	for( int j = 0; j < L; ++j ) {
		        char ch;
                        cin >> ch;
                        if(ch != '(') {
                                word[j] = (1L << (ch - 'a'));
                        } else {
                                do {
                                        cin >> ch;
                                        word[j] |= (1L << (ch - 'a'));
                                } while(ch != ')');
                        }
                }
                int cnt = 0;
        	for( int j = 0; j < D; ++j ) {
                        int k = 0;
                	for( ; k < L; ++j ) {
                                if((dict[j*L + k] & word[k]) == 0) {
                                        break;
                                }
                        }
                        if(k == L) {
                                ++cnt;
                        }
                }
                cout << "Case #" << i+1 << ": " << cnt << endl;
	}
	return 0;
}
//---------------------------------------------------------------------------
