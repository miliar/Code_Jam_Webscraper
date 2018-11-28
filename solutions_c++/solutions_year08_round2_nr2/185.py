#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

using namespace std;

#ifndef DEB
#define DEBUG(out)
#else
#define DEBUG(out) cerr << __LINE__ << ":\t" << out << endl
#endif

bool isp[1001];

int graph[1001];

int ro(int i){
	if(graph[i] == i)
		return i;
	return ro(graph[i]);
}

int main(){
	int tcs;
	scanf("%d", &tcs);
	for(int i=0; i<=1000; ++i)
		isp[i] = true;
	isp[0] = isp[1] = false;
	for(int i=2; i<=32; ++i){
		if(isp[i]){
			for(int j=i; j*i <= 1000; ++j){
				isp[j*i] = false;
			}
		}
	}
	for(int tc=0; tc<tcs; ++tc){
		int a, b, p;
		for(int i=0; i<=1000; ++i)
			graph[i] = i;
		scanf("%d %d %d", &a, &b, &p);
		for(int i=a; i<=b; ++i){
			for(int j=i+1; j<=b; ++j){
				for(int t=p; t<=b; ++t){
					if(!isp[t])
						continue;
					if(i%t)
						continue;
					if(j%t)
						continue;
					DEBUG(i << " " << j);
					graph[ro(graph[i])] = graph[ro(graph[j])];
				}
			}
		}
		set<int> r;
		for(int i=a; i<=b; ++i){
			r.insert(ro(i));
		}
		printf("Case #%d: %d\n", tc+1, (int)r.size());
	}
}
