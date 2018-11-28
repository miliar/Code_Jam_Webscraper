#include <algorithm>
#include <cstdio>
#include <list>
#include <map>
#include <utility>
#include <set>

using namespace std;

int T, yy, R, N, ii, t, end, len;
list<pair<int, int> > q;
list<pair<list<int>, long long> > part;
list<pair<list<int>, long long> >::iterator it, it1;
list<int> temp;
long long total, otot, ans, k, stot;
set<int> sExist;
map<pair<list<int>, long long>, list<pair<list<int>, long long> >::iterator> lExist;
map<pair<list<int>, long long>, list<pair<list<int>, long long> >::iterator>::iterator it2;

int main(void)
{
    scanf("%d\n", &T);
    for (yy = 1; yy <= T; yy++)
    {
        scanf("%d %lld %d\n", &R, &k, &N);
        for (ii = 0; ii < N; ii++)
        {
            scanf("%d ", &t);
            q.push_back(make_pair(t, ii));
        }

        lExist.clear();
        while (1)
        {
            total = 0;
            temp.clear();
            sExist.clear();
            
            while (total + q.front().first <= k &&
                sExist.find(q.front().second) == sExist.end())
            {
                temp.push_back(q.front().second);
                sExist.insert(q.front().second);
                total += q.front().first;
                q.push_back(q.front());
                q.pop_front();
            }
            //if (!part.empty() && (it1 = find(part.begin(), part.end(),
            //    make_pair(temp, total))) != part.end())
            if (!part.empty() && (it2 = lExist.find(make_pair(temp, total))) != lExist.end())
                break;
            part.push_back(make_pair(temp, total));
            it = part.end();
            it--;
            lExist[make_pair(temp, total)] = it;
        }

        
        it1 = it2->second;
        stot = 0;
        for (it = part.begin(), ii = 0; ii < R && it != part.end();
        ii++, it++)
            stot += it->second;

        ans = stot;

        R -= ii;

        if (R > 0)
        {
            otot = 0;
            for (it = it1, len = 0; it != part.end(); it++, len++)
                otot += it->second;

            ans += otot * (R / len);
            end = R % len;
            for (ii = 0, it = it1; ii < end; ii++, it++)
                ans += it->second;
        }

        printf("Case #%d: %lld\n", yy, ans);

        q.clear();
        part.clear();
    }

    return 0;
}
