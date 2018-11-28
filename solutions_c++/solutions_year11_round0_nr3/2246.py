#include <iostream>
#include <vector>
#include <cassert>
#include <numeric>
#include <algorithm>
using namespace std;

uint64_t add(uint64_t a,uint64_t b)
{
    return a ^ b;
}

bool check(const vector<uint64_t> &v)
{
    assert(v.size() >= 2);
    uint64_t r = v[0];
    for(size_t i=1;i<v.size();++i)
	r = add(r,v[i]);
    return r == 0;
}

void solve(int case_num)
{
    int n;cin >> n;
    vector<uint64_t> v;
    for(int i=0;i<n;++i)
    {
	uint64_t e;cin >> e;
	v.push_back(e);
    }
    sort(v.begin(),v.end(),less<uint64_t>());
    if(check(v))
    {
	uint64_t result = accumulate(v.begin(),v.end(),0) - v[0];
	printf("Case #%d: %llu\n",case_num,result);
    }
    else
	printf("Case #%d: NO\n",case_num);
}

int main()
{
    int n;cin >> n;
    for(int i=1;i<=n;++i)
	solve(i);
    return 0;
}
