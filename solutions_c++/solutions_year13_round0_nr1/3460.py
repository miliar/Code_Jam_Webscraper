#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
using namespace std;
int main(int argc, char *argv[]){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int test_count; cin >> test_count;
    for(int test = 0; test < test_count; ++test){
        vector<string> field(4);
        for(int i = 0; i < 4; ++i)
            cin >> field[i];
        
        //for(int i = 0; i < 4; ++i)
        //    cout << field[i] << endl;

        bool x_won = false, o_won = false, dot_present = false;

        for(int i = 0; i < 4; ++i){
            map<char, int> cnt;
            for(int j = 0; j < 4; ++j){
                cnt[field[i][j]]++;
            }
            dot_present |= (cnt['.'] != 0);
            x_won |= ( cnt[ 'X' ] + cnt[ 'T' ] == 4 );
            o_won |= ( cnt[ 'O' ] + cnt[ 'T' ] == 4 );
        }
        
        for(int i = 0; i < 4; ++i){
            map<char, int> cnt;
            for(int j = 0; j < 4; ++j){
                cnt[field[j][i]]++;
            }
            x_won |= ( cnt[ 'X' ] + cnt[ 'T' ] == 4 );
            o_won |= ( cnt[ 'O' ] + cnt[ 'T' ] == 4 );
        }

        {
            map<char, int> cnt;
            for(int i = 0; i < 4; ++i){
                cnt[field[i][i]]++;
            }
            //cout << cnt['O'] << "+" << cnt['T'] << endl;
            x_won |= ( cnt [ 'X' ] + cnt [ 'T' ] == 4 );
            o_won |= ( cnt [ 'O' ] + cnt [ 'T' ] == 4 );
        }
        
        {
            map<char, int> cnt;
            for(int i = 0; i < 4; ++i){
                cnt [ field[ i ][ 3 - i ] ]++;
            }
            //cout << cnt['O'] << "+" << cnt['T'] << endl;
            x_won |= ( cnt [ 'X' ] + cnt[ 'T' ] == 4 );
            o_won |= ( cnt [ 'O' ] + cnt[ 'T' ] == 4 );
        }

        cout << "Case #" << (test + 1) << ": ";
        if(x_won) cout << "X won" << endl;
        else if(o_won) cout << "O won" << endl;
        else if(dot_present) cout << "Game has not completed" << endl;
        else cout << "Draw" << endl;
    }
    return 0;
}