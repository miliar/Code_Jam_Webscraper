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

long sets(int j, int k, vector<long>& map, vector<long>& s, int H, int W, int& cnts)
{
        if(s[j*W+k] > 0) {
                return s[j*W+k];
        }
        if(j > 0 && map[(j*W)+k] > map[(j-1)*W+k]) {
                s[j*W+k] = sets(j-1,k,map,s,H,W,cnts);
        } else if(k > 0 && map[(j*W)+k] > map[(j*W)+k-1]) {
                s[j*W+k] = sets(j,k-1,map,s,H,W,cnts);
        } else if(k < W - 1 && map[(j*W)+k] > map[(j*W)+k+1]) {
                s[j*W+k] = sets(j,k+1,map,s,H,W,cnts);
        } else if(j < H - 1 && map[(j*W)+k] > map[(j+1)*W+k]) {
                s[j*W+k] = sets(j+1,k,map,s,H,W,cnts);
        } else {
                ++cnts;
                s[j*W+k] = cnts;
        }
        return s[j*W+k];
}


int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	for( int i = 0; i < N; ++i ) {
                int H, W;
                cin >> H >> W;
                vector<long> map = vector<long>(H*W);
        	for( int j = 0; j < H; ++j ) {
                	for( int k = 0; k < W; ++k ) {
                                cin >> map[j*W + k];
                        }
                }
                vector<long> s = vector<long>(H*W);
                int cnts = 0;

        	for( int j = 0; j < H; ++j ) {
                	for( int k = 0; k < W; ++k ) {
                                sets(j,k,map,s,H,W,cnts);
                        }
                }
                vector<char> bnam = vector<char>(cnts + 1);
                char clet = 'a';

                cout << "Case #" << i+1 << ": " << endl;

        	for( int j = 0; j < H; ++j ) {
                	for( int k = 0; k < W; ++k ) {
                                if(bnam[s[j*W+k]]=='\0') {
                                        bnam[s[j*W+k]] = clet++;
                                }
                                cout << bnam[s[j*W+k]];
                        }
                        cout << endl;
                }

	}
	return 0;
}
//---------------------------------------------------------------------------
