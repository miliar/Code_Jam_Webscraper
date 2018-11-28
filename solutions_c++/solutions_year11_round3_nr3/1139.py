#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
int main ()
{
    int num_games, game_num, n, l, h;
    string result;

    cin >> num_games;

    for (game_num = 1; game_num <= num_games; game_num++ )
    { 
        cin >> n >> l >> h;

        vector<int> orchestra;
        for ( int i = 0; i < n; ++i ) {
            int freq;
            cin >> freq;
            orchestra.push_back(freq);
        }

        bool works = false;
        int i = 0, answer = 0;
        for ( i = l; i <= h; ++i ) {
            bool failed = false;
            for ( vector<int>::iterator it = orchestra.begin(); it < orchestra.end(); ++it ) {
                if ( !( (i % (*it) == 0) || ((*it) % i) == 0 ) )
                    failed = true;
            }
            if (!failed){
                works = true;
                answer = i;
                break;
            }
        } 

        result += "Case #";
        stringstream cvert;
        cvert.flush();
        cvert << game_num;
        result += cvert.str();
        result += ": ";

        if (works) {
            stringstream cvert2;
            cvert2.flush();
            cvert2 << answer;
            result += cvert2.str();
            result += "\n";
        } else {
            result += "NO\n";
        }

    }


    cout << result;
    return 0;
}
