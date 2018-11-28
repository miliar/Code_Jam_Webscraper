#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int GORE = 0, DOLE = 2, LEVO = 3, DESNO = 1;
const int move[4][2] = { {0,1}, {1,0}, {0,-1}, {-1,0} }; // gore dole levo desno

int N;
int L;

short V[6011][6011], H[6011][6011];
bool used[6011][6011];

string compress(string s)
{
    string r = "";
    for (int i = 0; i < s.size(); ++i)
    {
        if (s[i] == 'F') { r += "F"; continue; }
        int chdir = 0;
        while (i < s.size() && s[i] != 'F')
        {
            if (s[i] == 'R') ++chdir;
            else --chdir;
            ++i;
        }
        --i;
        r += string((chdir + 1000000000) % 4, 'R');
    }
    return r;
}

int main()
{
    scanf("%d", &N);
    
    for (int test = 1; test <= N; ++test)
    {
        memset(V,0,sizeof V);
        memset(H,0,sizeof H);
        memset(used, 0, sizeof used);
        
        scanf("%d", &L);
        
        string S;
        int T;
        int x = 3002, y = 3002, dir = 0;
        
        int minx = x, miny = y, maxx = x, maxy = y;
        
        for (int i = 0; i < L; ++i)
        {
            cin >> S >> T;
            S = compress(S);
            
            //cout << "compressed string: " << S << endl;
            
            if (S.size() == 0) continue;
            if (S.find("F") == string::npos)
            {
                dir = ((int) S.size() * T % 4 + dir) % 4;
            }
            else
            {
                for (int j = 0; j < T; ++j)
                {
                    for (int k = 0; k < S.size(); ++k)
                    {
                        if (S[k] == 'F')
                        {
                            int nx = x + move[dir][0];
                            int ny = y + move[dir][1];
                            if (dir == GORE) V[x][y] = 1;
                            else if (dir == DOLE) V[nx][ny] = 1;
                            else if (dir == LEVO) H[nx][ny] = 1;
                            else H[x][y] = 1;
                            x = nx;
                            y = ny;
                            //printf("x = %d, y = %d\n", x, y);
                            minx = min(minx, x);
                            miny = min(miny, y);
                            maxx = max(maxx, x);
                            maxy = max(maxy, y);
                        }
                        else if (S[k] == 'R')
                            dir = (dir + 1) % 4;
                        else
                            dir = (dir - 1 + 4) % 4;
                    }
                }
            }
        }
        
        minx = max(minx - 10, 0);
        miny = max(miny - 10, 0);
        maxx = min(maxx + 10, 6010);
        maxy = min(maxy + 10, 6010);
        
        int result = 0;
        
        // horizontal
        short P[6011];
        for (int y = miny; y < maxy; ++y)
        {
            memset(P,0,sizeof P);
            P[0] = V[0][y];
            for (int x = max(minx,1); x < maxx; ++x)
                P[x] = V[x][y] + P[x - 1];
            
            //printf("za y = %d\n", y);
            //for (int x = 3002; x <= 3004; ++x)
              //  printf("%d, ", P[x]);
            //puts("");
            for (int s = 0, x = maxx - 2; x >= minx; --x)
            {
                s += V[x + 1][y];
                //if (x >= 3002 && x <= 3004) printf("{s = %d, P[%d] = %d}\n", s, x, P[x]);
                if (!(P[x] & 1) && !(s & 1) && P[x] && s)
                {
                    ++result;
                    used[x][y] = true;
                }
            }
        }
        
        // vertical
        for (int x = minx; x < maxx; ++x)
        {
            memset(P,0,sizeof P);
            P[0] = H[x][0];
            for (int y = max(miny,1); y < maxy; ++y)
                P[y] = H[x][y] + P[y - 1];
            for (int s = 0, y = maxy - 2; y >= miny; --y)
            {
                s += H[x][y + 1];
                if (!(P[y] & 1) && !(s & 1) && P[y] && s && !used[x][y])
                {
                    ++result;
                }
            }
        }
        printf("Case #%d: %d\n", test, result);
    }
	return 0;
}
