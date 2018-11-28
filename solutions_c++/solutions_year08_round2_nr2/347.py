#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef unsigned long long int_t;

struct DisSet {
        int_t base;
        int_t n;
        vector<int_t> set, height;

        DisSet(int_t a, int_t b) :
            base(a),
            n(b-a+1),
            set(n),
            height(n, 0)
        {
                for (int_t i=0; i<n; ++i)
                        set[i] = i;
        }

        int_t find(int_t xa)
        {
                int_t x = xa-base;
                int_t r = x;
                while (set[r] != r)
                        r = set[r];
                while (x!=r) {
                        int_t j = set[x];
                        set[x] = r;
                        x = j;
                }
                return r+base;
        }

        void merge(int_t a, int_t b)
        {
                a -= base;
                b -= base;
                if (height[a] == height[b]) {
                        ++height[a];
                        set[b] = a;
                } else
                        if (height[a]>height[b])
                                set[b] = a;
                        else
                                set[a] = b;
        }
};


int_t gcd(int_t a, int_t b)
{
        int_t t;
        while (b) {
                t = b;
                b = a % b;
                a = t;
        }
        return a;
}

int_t prime(int_t x)
{
    while ((x & 1) == 0)
        x >>=1;
    if (x == 1)
        return 2;
    for (int_t d=3; d*d<=x; d+=2) {
        while (x%d == 0)
            x/=d;
        if (x == 1)
            return d;
    }
    return x;
}

int main()
{
    int n;
    cin >> n;
    
    for (int i=0; i<n; ++i) {
        int_t a, b, p;
        cin >> a >> b >> p;
        
        DisSet ds(a, b);
        for (int_t x=a; x<=b; ++x) {
            for (int_t y=x+1; y<=b; ++y) {
                int_t d = gcd(x,y);
                if (d >= p && prime(d) >= p) {
                    //clog << "merging " << x << " : " << y << endl;
                    ds.merge(ds.find(x), ds.find(y));
                    /*for (int_t z=x+x; z<=b; z+=x)
                        ds.merge(x, z);
                    for (int_t z=y+y; z<=b; z+=y)
                        ds.merge(x, z);*/
                }
            }
        }
        set<int_t> roots;
        for (int_t x=a; x<=b; ++x) {
            int_t f = ds.find(x);
            //clog <<"f:" << f << endl;
            roots.insert(f);
        }
        
        cout << "Case #" << i+1 << ": " << roots.size() << endl;
    }
}
