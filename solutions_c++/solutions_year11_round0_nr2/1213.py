#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector <char> d;
vector <pair<char, char> > op;

char e[30][30];
int in_elem[30];


void opposed(){
	d.clear();
	d.push_back('[');
	d.push_back('[');
	fill(in_elem, in_elem + 30, 0);
}

int main(){
	int t, c, D, n;
	char data[111], tmp;
	
	scanf("%d", &t);
	for (int q = 1; q <= t; q++){
		fill(&e[0][0], &e[29][29], '.');
		op.clear();
		opposed();
		
		scanf("%d", &c);
		for (int i = 0; i < c; i++){
			scanf(" %s", data);
			e[data[0] - 'A'][data[1] - 'A'] = data[2];
			e[data[1] - 'A'][data[0] - 'A'] = data[2];
		}
		scanf("%d", &D);
		for (int i = 0; i < D; i++){
			scanf(" %s", data);
			op.push_back(make_pair(data[0], data[1]));
		}
		scanf("%d %s", &n, data);
		
		for (int i = 0; i < n; i++){
			d.push_back(data[i]);
			in_elem[data[i] - 'A']++;
			
			if (e[d[d.size() - 1] - 'A'][d[d.size() - 2] - 'A'] != '.'){
				in_elem[d[d.size() - 1] - 'A']--;
				in_elem[d[d.size() - 2] - 'A']--;
				tmp = e[d[d.size() - 1] - 'A'][d[d.size() - 2] - 'A'];
				in_elem[tmp - 'A']++;
				d.pop_back(), d.pop_back();
				d.push_back(tmp);
			}
			
			for (int j = 0; j < D; j++)
				if (in_elem[op[j].first - 'A'] > 0 && in_elem[op[j].second - 'A'] > 0)
					opposed();
		}
		
		printf("Case #%d: [", q);
		for (int i = 2; i < (int)d.size(); i++)
			if (i == 2)
				printf("%c", d[i]);
			else
				printf(", %c", d[i]);
		printf("]\n");
	}
}
