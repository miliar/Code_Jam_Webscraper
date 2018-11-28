#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>
#include <assert.h>

using namespace std;

#define rep(i,N) for(int i = 0; i < (int)(N); ++i)

struct Problem
{
    int N;
    vector<int> a;


    Problem()
    {
        cin >> N;
        a.resize(N,0);
        rep(i,N) cin >> a[i];

    }

    double expectationFits()
    {
        vector< pair<int,int> > goal(N);

        map<int,int> lo, hi;

        rep(i,N) goal[i] = make_pair(a[i],i);

        sort(goal.begin(), goal.end());

        rep(i,N) lo[a[i]] = (1<<30), hi[a[i]] = -(1<<30);

        rep(i,N)
        {
            if(lo[goal[i].first] > i) lo[goal[i].first] = i;
            if(hi[goal[i].first] < i) hi[goal[i].first] = i;
        }

        vector<int> p(N,-1);

        rep(i,N) if(lo[a[i]] <= i && i <= hi[a[i]])
        {
            p[i] = i;
        }

        vector<int> cycleSZ;
        int ans = 0;

        while( true )
        {
            int start = 0;
            while(start < N && p[start]!=-1) start++;
            if(start == N) break;

            int c_sz = 0;
            int i = start;

            do
            {
                assert( lo[a[i]] <= hi[a[i]] );

                while( p [ lo[a[i]] ] == lo[a[i]] ) lo[a[i]]++;

                p[i]=lo[a[i]]++;

                i = p[i];

                c_sz += 1;
            }
            while(i != start);

            cycleSZ.push_back(c_sz);
        }

//        cout << " p " << endl;
//        rep(i,N) cout << "i " << i << " p[i] " << p[i] << endl;
//        cout << endl;

        return accumulate(cycleSZ.begin(),cycleSZ.end(),0);
    }
};

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("D-large.in","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    for(int c = 1; c <= T; ++c) printf("Case #%d: %f%7 \n",c, Problem().expectationFits() );

	return 0;
}
