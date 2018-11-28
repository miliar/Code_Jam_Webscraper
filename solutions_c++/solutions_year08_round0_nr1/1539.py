#include <cstdio>
#include <list>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
using namespace std;
int main() {
	int N;
	scanf("%d", &N);
	for(int n=1; n<=N; n++) {
		int s, q;
		scanf("%d\n", &s);		
		map<string, list<int> > search_times;
		set<string> searchers;
		for (int i=0; i<s; i++) {
			char buffer[102];
			gets(buffer);
			searchers.insert(string(buffer));
		}
		scanf("%d\n", &q);
		vector<string> input(q);
		for (int i=0; i<q; i++) {
			char buffer[102];
			gets(buffer);
			input[i] = string(buffer);
			search_times[input[i]].push_back(i);			
		}
		for (set<string>::iterator i=searchers.begin(); i!=searchers.end(); i++)
			search_times[*i].push_back(q);
		priority_queue<pair<int, const string*>> next_occur;
		for (map<string, list<int> >::iterator i = search_times.begin(); i!= search_times.end(); i++) 
			next_occur.push(make_pair(i->second.front(), &(i->first)));					
		int cnt = 0;		
		const string* current = next_occur.top().second;

		if (search_times[*current].front() < q)
			for (int t=0; t<q; t++) {
				if (input[t] == *current) {
					cnt++;
					current = next_occur.top().second;
					if (next_occur.top().first == q)
						break;
				}
				search_times[input[t]].pop_front();
				next_occur.push(make_pair(search_times[input[t]].front(), &input[t]));
			}

		printf("Case #%d: %d\n", n, cnt);
	}
	return 0;
}