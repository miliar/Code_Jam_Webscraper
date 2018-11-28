#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> flowmap;

struct Point 
{
    int r,c;
    Point(int a,int b) : r(a),c(b) {}
    bool operator==(const Point & ref) const {return r == ref.r && c == ref.c;}
};

Point WhereNext(flowmap & mp,Point cur)
{
    int lowalt = mp[cur.r][cur.c]-1;
    int R = mp.size();
    int C = mp[0].size();

    Point best = cur;
    
    if (cur.r+1 < R && mp[cur.r+1][cur.c] <= lowalt)
    {
        lowalt = mp[cur.r+1][cur.c];
        best = Point(cur.r+1,cur.c);
    }
    
    if (cur.c+1 < C && mp[cur.r][cur.c+1] <= lowalt)
    {
        lowalt = mp[cur.r][cur.c+1];
        best = Point(cur.r,cur.c+1);
    }

    if (cur.c > 0 && mp[cur.r][cur.c-1] <= lowalt)
    {
        lowalt = mp[cur.r][cur.c-1];
        best = Point(cur.r,cur.c-1);
    }

    if (cur.r > 0 && mp[cur.r-1][cur.c] <= lowalt)
    {
        lowalt = mp[cur.r-1][cur.c];
        best = Point(cur.r-1,cur.c);
    }

    return best;
}

void Solve(flowmap & mp)
{
    int R = mp.size();
    int C = mp[0].size();
    char * resmap = new char [R*C];
    memset(resmap,0,sizeof(char)*R*C);
    char c='a';
    for (int i=0;i < R;++i)
        for (int j=0;j < C;++j)
        {
            queue<Point> path;
            Point cur (i,j);

            while (1)
            {
                if (resmap[cur.r*C+cur.c] != 0) break;
                path.push(cur);
                //Where i go next?
                Point res = WhereNext(mp,cur);
                if (res == cur) //sink
                    break;
                cur = res;
            }
            char toset=c;
            if (resmap[cur.r*C+cur.c] == 0) c++;
            else toset = resmap[cur.r*C+cur.c];
            while (!path.empty())
            {
                Point p = path.front();
                resmap[p.r*C+p.c] = toset;
                path.pop();
            }
        }
    for (int i=0;i < R;++i)
    {
        for (int j=0; j< C;++j)
        {
            cout << resmap[i*C+j] << " ";
        }
        cout << endl;
    }
}

int main(int argc,char * argv[])
{
    int T;
    cin >> T;
    for (int i=0;i < T;++i)
    {
        int H,W;
        cin >> H >> W;
        flowmap mp;
        for (int j=0;j < H;++j)
        {
            vi row;
            for (int k=0;k < W;++k)
            {
                int c;
                cin >> c;
                row.push_back(c);
            }
            mp.push_back(row);
        }
        cout << "Case #" << i+1 <<":" << endl;
        Solve(mp);
    }
    return 0;
}
