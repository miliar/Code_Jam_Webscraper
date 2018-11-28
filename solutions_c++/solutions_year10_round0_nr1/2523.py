#include<vector>
#include<iostream>
#include<map>
#include<queue>
#include<iterator>
#include<algorithm>
#include<iomanip>
#include<set>
#include<thread>
#include<mutex>
#include<condition_variable>
#include<iomanip>
#include<memory>
#include<utility>
#include<tuple>
using namespace std;
typedef vector<int> VI;
typedef vector<vector<int>> VII;typedef long long LL;
typedef long long LL;

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
		LL K,N;
		cin>>N>>K;
		cout << "Case #" << t << ": ";
		if((K+1)%(1<<N) == 0) cout << "ON";
		else cout << "OFF";
		cout << endl;
	}
}

