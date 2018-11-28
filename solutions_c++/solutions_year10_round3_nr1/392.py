#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	int T;
	cin >> T;
	vector<int> a;
	vector<int> b;
	int N;
	for(int counter=0;counter<T; counter++)
	{
		cin >> N;
		for(int i=0; i<N; i++)
		{
			int tmp1, tmp2;
			cin >> tmp1 >> tmp2;
			a.push_back(tmp1);
			b.push_back(tmp2);
		}
		
		int tot=0;
		for(int i=0 ;i<a.size(); i++)
		{
			for(int j=i+1; j<a.size(); j++)
			{
				if(a[i] > a[j] && b[i] < b[j])
					tot++;
				else if(a[i] < a[j] && b[i] > b[j])
					tot ++;
			}
			
			
		}
		
		cout << "Case #" << counter+1 << ": " << tot << endl;
		a.clear();
		b.clear();
		
		
	}


	return 0;
}