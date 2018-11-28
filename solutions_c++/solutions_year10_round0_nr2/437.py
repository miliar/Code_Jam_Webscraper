#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>


using namespace std;

template<typename T> 
T gcd(T a,T b)
{
	if(b==0)
		return a;
	return gcd(b,a%b);
}

int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout); 
	int C,N;
	int t[3];
	cin>>C;
	
	int round=1;
	while (round<=C)
	{
		cin>>N;
		for (int i=0;i<N;i++)
			cin>>t[i];
		sort(t,t+N);
		int yueshu=t[1]-t[0];
		if(N==3)
			yueshu=gcd(yueshu,t[2]-t[1]);
		int res=0;
		if (t[0]%yueshu != 0)
			res=yueshu-t[0]%yueshu;
		cout<<"Case #"<<round<<": "<<res<<endl;
		round++;
	}
	return 0;
}
