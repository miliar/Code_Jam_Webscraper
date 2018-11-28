#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cassert>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>

using namespace std;

typedef ostream_iterator<int> output;

int main()
{
    freopen("as.txt", "rt", stdin);
	freopen("aos.txt", "wt", stdout);

	int num;
	scanf("%d", &num);

    vector< int > t1;
    vector< int > t2;
	for (int count=0; count<num; count++)
	{
        int nv, t;
        scanf("%d\n", &nv);
        for (int c1=0; c1<nv; c1++)
        {
            scanf("%d", &t);
            t1.push_back(t);
        }
        for (int c1=0; c1<nv; c1++)
        {
            scanf("%d", &t);
            t2.push_back(t);
        }

        sort(t1.begin(), t1.end());
        sort(t2.begin(), t2.end());
        reverse (t1.begin(), t1.end());


        cout<<"Case #"<<count+1<<": ";
        int val = 0;
        for (int z=0; z<nv; z++)
        {
            val = val + t1[z]*t2[z];
        }
        cout<<val<<"\n";
        t1.clear();
        t2.clear();
	}

	exit(0);
}
