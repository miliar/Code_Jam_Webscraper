#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>

#define MAX 10010

using namespace std;

int main(void){
	int T, k = 0;
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("result.txt", "w", stdout);
	scanf("%d", &T);
	while(k++ < T){
		vector<int> position;
		vector<int> length;
		int n, d, l;
		map<int, int> climb;
		scanf("%d", &n);
		for(int i = 0; i < n; ++i){
			scanf("%d%d", &d, &l);
			position.push_back(d);
			length.push_back(l);
		}
		
		scanf("%d", &l);
		position.push_back(l);
		length.push_back(l);

		if(position[0] > length[0]){
			printf("Case #%d: NO\n", k);
			continue;
		}

		climb.insert(map<int, int>::value_type(position[0], position[0]));

		int current;
		bool ok = false;
		for(map<int, int>::iterator it = climb.begin(); it != climb.end(); ++it){
			int current = it->first;
			if(current == l){
				ok = true;
				break;
			}

			for(unsigned j = 0; j < position.size(); ++j){
				if(position[j] <= current)
					continue;
				int dist = position[j] - current;
				if(it->second < dist)
					break;
				int newlen = min(dist, length[j]);
				if(climb.find(position[j]) != climb.end())
					climb[position[j]] = max(climb[position[j]], newlen);
				else
					climb[position[j]] = newlen;
			}
		}
		
		if(ok)
			printf("Case #%d: YES\n", k);
		else
			printf("Case #%d: NO\n", k);
		
	}
	return 0;
}
