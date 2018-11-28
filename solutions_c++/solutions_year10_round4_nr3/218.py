#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <algorithm>
#include <map>
#include <set>
#include <list>

struct Rect
{
    int x1, x2, y1, y2;
    bool isIntersect(const Rect &r) const
    {
        if (x1 > r.x1)
            return r.isIntersect(*this);
        int left = std::max(x1, r.x1);
        int right = std::min(x2 + 1, r.x2 + 1);
        int top = std::max(y1, r.y1);
        int bottom = std::min(y2 + 1, r.y2 + 1);
        if (left == right && top == bottom
            && left == r.x1 && top == r.y1)
            return false;
        if (left <= right && top <= bottom)
            return true;
/*
        left = std::min(x2, r.x2);
        right = std::max(x1 - 1, r.x1);
        top = std::min(y2 + 1, r.y2);
        bottom = std::max(y1, r.y1);
        if (left <= right && top <= bottom)
            return true;
*/
        return false;
    }
};

std::istream &operator>>(std::istream &stream, Rect &r)
{
    return stream >> r.x1 >> r.y1 >> r.x2 >> r.y2;
}
/*
struct Figure
{
    std::vector<Rect> parts;

    bool isIntersect(const Rect &r) const
    {
        for (size_t i = 0 ; i < parts.size() ; ++i)
            if (parts[i].isIntersect(r))
                return true;

        return false;
    }
    void add(const Rect &r)
    {
        parts.push_back(r);
    }
};
*/
std::vector<int> p;

void init (int max_n)
{
    p.resize (max_n);
    for (int i=0; i<max_n; ++i)
        p[i] = i;
}

int find_set (int x)
{
    if (x == p[x])  return x;
    return p[x] = find_set (p[x]);
}

void unite (int x, int y)
{
    x = find_set (x);
    y = find_set (y);
    if (rand() & 1)
        p[y] = x;
    else
        p[x] = y;
}

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        std::cout << "Case #" << t << ": ";

        int R;
        std::cin >> R;

        std::vector<Rect> rects(R);
        init(R);

        for (int i = 0 ; i < R ; ++i)
        {
            std::cin >> rects[i];
            for (int j = 0 ; j < i ; ++j)
                if (rects[i].isIntersect(rects[j]))
                    unite(i, j);
        }

        std::vector<int> right(R), bottom(R);

        for (int i = 0 ; i < R ; ++i)
        {
            int s = find_set(i);
            right[s] = std::max(right[s], rects[i].x2);
            bottom[s] = std::max(bottom[s], rects[i].y2);
        }

        int best = 0;
        for (int i = 0 ; i < R ; ++i)
        {
            int s = find_set(i);
            int dist = right[s] - rects[i].x1 + bottom[s] - rects[i].y1 + 1;
            if (dist > best)
                best = dist;
        }

        std::cout << best << "\n";
    }
    return 0;
}
