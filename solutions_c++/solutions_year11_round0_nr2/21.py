#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;
typedef long long ll;

ifstream in("B.in");
ofstream out("B.out");

int T, C, D, N;

string intToBase[8] = "QWERASDF";
int baseToInt(char base)
{
    switch (base)
    {
        case 'Q': return 0;
        case 'W': return 1;
        case 'E': return 2;
        case 'R': return 3;
        case 'A': return 4;
        case 'S': return 5;
        case 'D': return 6;
        case 'F': return 7;
        default: return -1;
    }
}

void printList(vector<char>& theList)
{
    out << "[";
    for (int i = 0; i < theList.size(); ++i)
    {
        if (i > 0)
            out << ", ";
        out << theList[i];
    }
    out << "]" << endl;
}

int main()
{
    in >> T;
    for (int tc = 1; tc <= T; ++tc)
    {
        char combine[8][8];
        bool opposed[8][8];
        string invoke;
        vector<char> elemList;
        for (int i = 0; i < 8; ++i)
        for (int j = 0; j < 8; ++j)
        {
            combine[i][j] = '.';
            opposed[i][j] = false;
        }
        
        in >> C;
        for (int i = 0; i < C; ++i)
        {
            in >> invoke;
            combine[baseToInt(invoke[0])][baseToInt(invoke[1])] = invoke[2];
            combine[baseToInt(invoke[1])][baseToInt(invoke[0])] = invoke[2];
        }
        
        in >> D;
        for (int i = 0; i < D; ++i)
        {
            in >> invoke;
            opposed[baseToInt(invoke[0])][baseToInt(invoke[1])] = true;
            opposed[baseToInt(invoke[1])][baseToInt(invoke[0])] = true;
        }
        
        in >> N >> invoke;
        for (int i = 0; i < N; ++i)
        {
            elemList.push_back(invoke[i]);
            int S = elemList.size();
            if (S >= 2)
            {
                char result = '.';
                if (baseToInt(elemList[S-2]) >= 0)
                    result = combine[baseToInt(elemList[S-2])][baseToInt(elemList[S-1])];
                if (result != '.')
                {
                    elemList.pop_back();
                    elemList.pop_back();
                    elemList.push_back(result);
                }
                else
                {
                    int top = baseToInt(elemList[S-1]);
                    for (int i = 0; i < S-1; ++i)
                        if (baseToInt(elemList[i]) >= 0 && opposed[top][baseToInt(elemList[i])])
                        {
                            elemList.clear();
                            break;
                        }
                }
            }
            //printList(elemList);
        }
        out << "Case #" << tc << ": ";
        printList(elemList);
    }
}
