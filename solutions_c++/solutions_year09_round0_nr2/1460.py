#include <iostream>
#include <vector>
#include <map>

#include <cstring>

//#define debug

using namespace std;

vector <vector <int> > heights;
vector <vector <char> > results;

vector <pair <int, int> > splyniete;
char napotkane = ' ';
int result, W, H;

void splyw(int x, int y) {
    #ifdef debug
    fprintf(stderr, "splyw: %d %d\n", x, y);
    #endif

    if (results[x][y] != ' ') {
        napotkane = results[x][y];
        return;
    }

    pair <int, int> lowest = pair <int, int> (0,0);
    if (y-1 >= 0)
    if (heights[x][y-1] < heights[x+lowest.first][y+lowest.second])
        lowest = pair <int, int> (0, -1);
    if (x-1 >= 0)
    if (heights[x-1][y] < heights[x+lowest.first][y+lowest.second])
        lowest = pair <int, int> (-1, 0);
    if (x+1 < W) 
    if (heights[x+1][y] < heights[x+lowest.first][y+lowest.second])
        lowest = pair <int, int> (1, 0);
    if (y+1 < H)
    if (heights[x][y+1] < heights[x+lowest.first][y+lowest.second])
        lowest = pair <int, int> (0, 1);

    splyniete.push_back(pair <int, int> (x,y));

    if ((lowest.first != 0) || (lowest.second != 0))
        splyw(x+lowest.first, y+lowest.second);
}


int main() {
    unsigned int N;
    cin >> N;

    heights.resize(100);
    for (int i = 0; i < 100; i++)
        heights[i].resize(100, 0);

        results.resize(100);
        for (int k = 0; k < 100; k++)
            results[k].resize(100, ' ');

    for (int i = 0; i < N; i++) {
        result = 0;
        

        cin >> H >> W;
        int tmp;
        for (int y = 0; y < H; y++)
           for (int x = 0; x < W; x++) {
               cin >> tmp;
               heights[x][y] = tmp;
               results[x][y] = ' ';
            }

        results[0][0] = ' ';
        char last = (char)(((int)'a')-1);

        for (int y = 0; y < H; y++)
            for (int x = 0; x < W; x++) 
                if (results[x][y] == ' ') {
                    // spływamy
                    splyniete.clear();
                    napotkane = ' ';
                    splyw(x,y);          
                    if (napotkane == ' ') {
                        last = (char)(((int)last)+1);
                        #ifdef debug
                        fprintf(stderr, "last :  %c\n", last);
                        #endif
                        napotkane = last;
                    }
                    for (int k = 0; k < splyniete.size(); k++) {
                        #ifdef debug
                        fprintf(stderr, "splyniete k: %d (%d, %d) \n", k, splyniete[k].first, splyniete[k].second);
                        #endif
                        results[splyniete[k].first][splyniete[k].second] = napotkane;
                    }
                }
        
        cout << "Case #" << i+1 << ":" << endl;
        for (int y = 0; y < H; y++) {
            for (int x = 0; x < W; x++)
                cout << results[x][y] << " ";
            cout << endl;
        }
    }
    
    return 0;
}
