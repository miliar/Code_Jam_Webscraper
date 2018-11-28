#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
 
#define SZ(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define INF (int)1e9
 
#define ll long long
#define vi vector<int>
#define vs vector<string>
 
using namespace std;

string convert(char ch)
{
       switch(ch)
       {
                 case '0': return "WWWW";
                 case '1': return "WWWB";
                 case '2': return "WWBW";
                 case '3': return "WWBB";
                 case '4': return "WBWW";
                 case '5': return "WBWB";
                 case '6': return "WBBW";
                 case '7': return "WBBB";
                 case '8': return "BWWW";
                 case '9': return "BWWB";
                 case 'A': return "BWBW";
                 case 'B': return "BWBB";
                 case 'C': return "BBWW";
                 case 'D': return "BBWB";
                 case 'E': return "BBBW";
                 default: return "BBBB";
       }
}

void invalidate(vs &board, int x, int y, int len)
{
    // cout << "called " << x << " " << y << endl;
    
    for(int i = 0; i < len; i++)    
             for(int j = 0; j < len; j++)
                     board[x + i][y + j] = 'X';
}

int testBoard(vs &board, int x, int y, int len)
{
     string a1 = "", a2 = "";
     for(int i = 0; i < len; i++)
     {
             a1 += (i % 2 == 0) ? "W" : "B";
             a2 += (i % 2 == 0) ? "B" : "W";
     }
     
     bool s = false, ans = true;
     for(int i = 0; i < len; i++)
     {
             if(s)
             {
                 if(a1 != board[x + i].substr(y, len)) 
                 {
                       ans = false;
                       break;
                 }
             }
             else
             {
                 if(a2 != board[x + i].substr(y, len)) 
                 {
                       ans = false;
                       break;
                 }
             }
             s = !s;
     }
     if(ans)
     {
            invalidate(board, x, y, len);
            /*
            cout << "Found " << x << " " << y << endl;
            cout << "Printing Board" << endl;
                                for(int a = 0; a < SZ(board); a++)
                                        cout << board[a] << endl;
                                             cout << endl;
            */
            return 1;
     }
            
     ans = true; 
     s = false;
     for(int i = 0; i < len; i++)
     {
             if(s)
             {
                 if(a2 != board[x + i].substr(y, len)) 
                 {
                       ans = false;
                       break;
                 }
             }
             else
             {
                 if(a1 != board[x + i].substr(y, len)) 
                 {
                       ans = false;
                       break;
                 }
             }
             s = !s;
     }
     if(ans)
     {
            invalidate(board, x, y, len); 
            /*
            cout << "Found " << x << " " << y << endl;
            cout << "Printing Board" << endl;
                                for(int a = 0; a < SZ(board); a++)
                                        cout << board[a] << endl;
                                             cout << endl;
            */
            return 1;
     }
     return 0;
}

int main()
{
    int T;
    cin >> T;
    
    for(int cas = 1; cas <= T; cas++)
    {
            int M, N;
            cin >> M >> N;
            
            vs board(M, "");
            for(int i = 0; i < M; i++)
            {
                    string temp;
                    cin >> temp;
                    
                    for(int j = 0; j < N / 4; j++)
                            board[i] += convert(temp[j]);
            }
            
            vi sizes, counts;
            int area = M * N;
            for(int len = min(M, N); len > 1; len--)
            {
                    int cnt = 0;
                    for(int i = 0; i + len <= M; i++)
                    {
                            for(int j = 0; j + len <= N; j++)
                            {
                                cnt += testBoard(board, i, j, len);    
                            }
                    }       
                    if(cnt)
                    {
                           sizes.PB(len);
                           counts.PB(cnt);
                           area -= cnt * len * len;
                           
                    }
                    
                    
            }
            
            if(area != 0)
            {
                    sizes.PB(1);
                    counts.PB(area);
            }
            
            cout << "Case #" << cas << ": " << SZ(counts) << endl;
            for(int i = 0; i < SZ(counts); i++)
            {
                    cout << sizes[i] << " " << counts[i] << endl;
            }
    }
    return 0;
}
