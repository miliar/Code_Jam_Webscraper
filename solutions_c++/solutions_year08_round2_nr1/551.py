#include <iostream>
#include <algorithm>
#include <iomanip>
#include <sstream>
#include <queue>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
#include<fstream>
using namespace std;

typedef vector <int> vi;
typedef vector<vi> vvi;
typedef vector <string> vs;
typedef vector<vs> vvs;
typedef long long i64;
typedef unsigned long long u64;
typedef pair<int,int> pii;

istringstream din;
ostringstream dout;

int dx[8] = {-1,0,1, 0,-1,-1,1,1};
int dy[8] = { 0,1,0,-1,-1, 1,1,-1};

int dirx[4] = {0, 1, 0, -1};
int diry[4] = {1, 0, -1, 0};
vector< pair<long, long> > v;

void init()
{
  din.clear();dout.str("");
  v.clear();
}
int find(pii p)
{
    for (int i = 0;i < v.size();i++) {
        if (v[i].first == p.first && v[i].second == p.second)
            return 1;
    }
    return 0;
}
int main()
{
    int nc;
    cin >> nc;
    for (int i = 0;i < nc;i++) {
        init();
        cout << "Case #" << (i+1) << ": ";
        cerr << "next case" << endl;
        //................................
        i64 n,a,b,c,d,x0,y0,m;
        cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
        
        v.push_back(make_pair(x0,y0));
        i64 x = x0, y = y0;
        cerr << x0 << " " << y0 << endl;
        for (int j = 1;j < n;j++) {
            x = (a*x+b)%m;
            y = (c*y+d)%m;
            v.push_back(make_pair(x,y));
            cerr << x << " " << y << endl;
        }

        int res = 0;
        for (int j = 0;j < v.size();j++)
            for (int k = j+1;k < v.size();k++)
                for (int l = k+1;l < v.size();l++) {
                    double dx = v[j].first + v[k].first*1.0 + v[l].first;
                    double dy = v[j].second + v[k].second + v[l].second;
                    dx /= 3.0; dy /= 3.0;
                    x = (i64)dx, y = (i64) dy;
                    if (dx - x*1.0 == 0.0 && dy - y*1.0 == 0.0) {
                    //res += find(make_pair(x,y));
                        res++;
                    }
                    
                }

        cout << res;
        //................................
        cout << endl;
    }
    return 0;
}
