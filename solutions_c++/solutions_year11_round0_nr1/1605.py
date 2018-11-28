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

#define SZ(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define INF (int)1e9
#define vi vector<int>
#define vs vector<string>

using namespace std;

vector <string> splitString(string a, char c)
{
    vector <string> res;
    string buff = "";
    a += c;
    
    for(int i = 0; i < a.size(); i++)
    {
   	 if(a[i] == c)
   	 {
   		 if(buff.size() > 0)
   			 res.push_back(buff);
   		 buff = "";
   	 }    
   	 else
   		 buff.push_back(a[i]);
    }
    return res;
}

int toInt(string num)
{
    stringstream ss;
    ss << num;
    int ret;
    ss >> ret;
    return ret;
}

int main()
{
    int T;
    
    cin >> T;

    for(int t = 0; t < T; t++)
    {
        int N;
        cin >> N;
        char buf[100001];
        cin.getline(buf, 100001);
        vs ip = splitString((string)buf, ' ');
        
        long long oPos = 1, bPos = 1, oT = 0, bT = 0, curPos;
        for(int j = 0; j < SZ(ip); j += 2)
        {
            curPos = toInt(ip[j + 1]);
            if(ip[j] == "O")
            {
                oT = max(oT + abs(curPos - oPos) + 1, bT + 1);
                oPos = curPos;
            }
            else
            {
                bT = max(bT + abs(curPos - bPos) + 1, oT + 1);
                bPos = curPos;
            }
        }

        cout << "Case #" << t + 1 << ": " << max(oT, bT) << endl;
        
    }
    return 0;
}
