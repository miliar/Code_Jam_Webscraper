#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T;

struct point
{
    int x, y;

    point(int xx = 0, int yy = 0): x(xx), y(yy) {}

    bool operator < (const point &other) const
    {
        return T == 1 ? x != other.x ? x < other.x : y < other.y :
               T == 2 ? y != other.y ? y < other.y : x < other.x :
               x+y != other.x + other.y ? x+y < other.x + other.y : y < other.y;
    }

    bool operator == (const point &other) const
    {
        return x == other.x && y == other.y;
    }
};

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int n;
        vector<point> cur, next;
        cin >> n;
        for (int i=0; i<n; i++)
        {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            for (int x=x1; x<=x2; x++)
                for (int y=y1; y<=y2; y++)
                    cur.push_back(point(x, y));
        }

        double start = clock();

        int ans = 0;
        for (; cur.size(); ans++)
        {
            T = 1;
            sort(cur.begin(), cur.end());
            cur.resize(unique(cur.begin(), cur.end()) - cur.begin());

            for (int i = 1; i < cur.size(); i++)
                if (cur[i].x == cur[i-1].x && cur[i].y == cur[i-1].y + 1)
                    next.push_back(cur[i]);

            T = 2;
            sort(cur.begin(), cur.end());

            for (int i = 1; i < cur.size(); i++)
                if (cur[i].y == cur[i-1].y && cur[i].x == cur[i-1].x + 1)
                    next.push_back(cur[i]);

            T = 3;
            sort(cur.begin(), cur.end());

            for (int i = 1; i < cur.size(); i++)
                if (cur[i].x == cur[i-1].x - 1 && cur[i].y == cur[i-1].y + 1)
                    next.push_back(point(cur[i].x + 1, cur[i].y));

            cur.swap(next);
            next.clear();
        }

                
        cout << "Case #" << tt << ": " << ans << endl;
//        cout << (clock() - start)/CLOCKS_PER_SEC << endl;
    }
    return 0;
}
