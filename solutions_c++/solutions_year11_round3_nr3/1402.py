#include <iostream>
#include <cstdint>
#include <vector>
#include <algorithm>
#include <boost/math/common_factor.hpp>
#include <cstring>
using namespace std;

int N;
uint64_t L,H;
vector<uint64_t> v;
int memo[10*10*10*10];

void read_input()
{
    memset(memo,0,sizeof memo);
    v.clear();

    cin >> N >> L >> H;
    
    for(int i=0;i<N;++i)
    {
	uint64_t note;cin >> note;
	v.push_back(note);
    }
    sort(v.begin(),v.end());
}

void calc()
{
    read_input();

    for(int n=L;n<=H;++n)
    {
	int i;
	for(i=0;i<N;++i)
	{
	    if(v[i] % n == 0 || n % v[i] == 0)continue;
	    else goto NEXT;
	}
    NEXT:
	if(i == N)
	{
	    cout << n << endl;
	    goto END;
	}
    }
    cout << "NO" << endl;
END:;
}

int main()
{
    int n;cin >> n;
    for(int i=1;i<=n;++i)
    {
	printf("Case #%d: ",i);
	calc();
    }
    return 0;
}

