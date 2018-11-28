#include <cstdio>
#include <vector>
#include <iostream>

#define REP(i,n) for(int i=0; i<(n); ++i)

using namespace std;

struct Node
{
	Node() { REP(i,26) child[i] = -1; }
	int child[26];
};

int l,d,n;
int last_index = 0;
vector<Node> nodes;

int new_node()
{
	nodes.push_back(Node());
	return last_index++;
}

void push()
{
	char buf[1024];
	scanf("%s",buf);
	int cur = 0;
	REP(i,l) {
//		cout << buf[i] << " : " << cur << endl;
		int next_index = nodes[cur].child[ buf[i]-'a' ];
		if(next_index == -1) next_index = new_node();
		nodes[cur].child[ buf[i]-'a' ] = cur = next_index;
	}
}

int go(vector< vector<int> > &line, int index, int cur)
{
//	cout << index << " " << cur << endl;

	int total = 0;
	if(index >= line.size()) return 1;
	Node &cur_node=nodes[cur];
	REP(j, line[index].size()) {
		int k = line[index][j];
		if(cur_node.child[k] != -1) {
			total += go(line, index+1, cur_node.child[k]);
		}
	}
	return total;
}

void check(int kase)
{
	vector< vector<int> > line;
	char buf[1024];
	int c=0;

	line.resize(l);
	scanf("%s",buf);

	REP(i,l) {
		if(buf[c] == '(') {
			++c;
			while(buf[c] != ')') {
				line[i].push_back((int) (buf[c]-'a') );
				++c;
			}
		}
		else {
			line[i].push_back((int) (buf[c]-'a') );
		}
		++c;
	}
	
	int ret = go(line, 0, 0);
	cout << "Case #" << kase << ": " << ret << endl;
}

int main()
{
	new_node();
	scanf("%d %d %d",&l,&d,&n);
	REP(i,d) {
		push();
	}
	REP(i,n) {
		check(i+1);
	};

	return 0;
}
