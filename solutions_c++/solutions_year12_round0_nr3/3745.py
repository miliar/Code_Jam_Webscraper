#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 110
#define datat int
#define ansdatat int

int n;

map<int,int> mp;

void init_deal(){
}

int len(int num){
	int res = 0;
	while(num>0){
		res++;
		num/=10;
	}
	return res;
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		printf("Case #%d: ",ttt);
		int a, b;
		scanf("%d%d", &a, &b);

		int l = len(a); 
		double pp = pow(10.0,l-1);
		int p10 = int(pp);

		mp.clear();

		int ans = 0;
		for (int i = a; i<=b; i++)
			if(mp.find(i) == mp.end()){
				vector<int> v;
				v.resize(0);
				v.push_back(i);

				int now = i;
				for (int k = 1; k<l; k++)
				{
					now = (now%p10)*10+now/p10;					
					if(now>=a && now!=i&& now<=b && 
						find(v.begin(), v.end(), now) == v.end()){
						v.push_back(now);
					}
				}
				sort(v.begin(), v.end());
				for(int j = 0;j<v.size();j++){
					mp[v[j]] = j;
					//cout<<v[j]<<" ";
				}
				//cout<<endl;
			}
			else{
				ans+=mp[i];
			}

		printf("%d\n", ans);

	}
	

	return 0;
};

