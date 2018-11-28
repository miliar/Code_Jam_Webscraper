#include<cstdio>
#include<set>
#include<queue>
#include<iostream>

#define FOR(I,A,B) for(int (I) = (A); (I) <= (B); (I)++)
#define FOREACH(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); ++a)
#define SIZE(X) ((int)X.size())

using namespace std;

static inline int digitsToNumber(deque<int> &A)
{
    int r = 0;
    FOREACH(i,A) 
    {
        r *= 10;   
        r += *i;
    }
    return r;
}

static inline int higherRotations(int n, int b)
{
    deque<int> A;
    set<int> R;
    int t = n;
    while(t != 0)
    {
        A.push_front(t%10);
        t /= 10;
    }
    FOR(i,2,SIZE(A))
    {
        A.push_back(A.front());
        A.pop_front();
        int q = digitsToNumber(A);
        if(n < q and q <= b) R.insert(q);
    }
    return SIZE(R);
}

void solve()
{
    int z;
    scanf("%d", &z);
    FOR(q,1,z) 
    {
        int a, b, r=0;
        scanf("%d%d", &a, &b);
        FOR(i,a,b) r += higherRotations(i,b);
        printf("Case #%d: %d\n", q, r);
    }
}

int main()
{
    solve();
    return 0;
}
