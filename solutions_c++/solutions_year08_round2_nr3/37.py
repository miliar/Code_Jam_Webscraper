#include <iostream>
#include <map>
#include <queue>
#include <cstdio>
#include <vector>
#include <set>

#define pb push_back
#define mp make_pair

using namespace std;

void process(int t)
{
    int K;
    cin >> K;
    vector<int> pos;
    map<int,int> out;
    vector<int> result;
    vector<int> countess;

    int n;
    cin >> n;
    for(int i=0;i<n;i++)
    {
	int tmp;
	cin >> tmp;
	out[tmp-1] = i ;
    }

    result.resize(n);

    for(int i=0;i<K;i++)
	pos.pb(i);

    const int aa = 1048576;

    countess.resize(aa*2,0);

    for(int i=aa;i<aa+K;i++)
    {
	countess[i] = 1;
	int tmp = i/2;
	while(tmp>0)
	{
	    countess[tmp]++;
	    tmp/=2;
	}
    }
    int cur = 0;

    for(int i=1;i<=K;i++)
    {
	cur = (cur+i-1) % countess[1];
	
	int tmp = 1,tmp2 = cur+1;

	while(tmp < aa)
	{
	    if(countess[tmp*2] >= tmp2)
	    {
		tmp = tmp*2;
	    }
	    else
	    {
		tmp2 -= countess[tmp*2];
		tmp = tmp * 2 + 1;
	    }
	}

	if(out.count(tmp-aa))
	{
	    result[out[tmp-aa]] = i;
	}

	while(tmp > 0)
	{
	    countess[tmp]--;
	    tmp /= 2;
	}
    }
    
    int ret=0;

    cout << "Case #" << t << ":";
    for(int i=0;i<n;i++)
	cout << " " << result[i];
    cout << endl;
}

int main(void)
{
    int T;
    cin >> T;
    for(int i=1;i<=T;i++)
	process(i);
}
