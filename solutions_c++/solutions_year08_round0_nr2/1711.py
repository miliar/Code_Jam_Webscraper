#include <stdio.h>
#include <stdlib.h>
#include <set>
#include <algorithm>

using namespace std;

char buffer[105];

struct s_node {
	bool operator<(const struct s_node &s1) const {
		if (fromTime != s1.fromTime) {
			return (fromTime < s1.fromTime);
		} else {
			return (toTime < s1.toTime);
		}
	}
	int fromTime;
	int toTime;
	set<int> adjNodes;
	int indegree;
	bool used;
};
typedef struct s_node node;

node fromNodes[105];
node toNodes[105];

int
convert(char *time)
{
	time[2] = '\0';
	return atoi(time) * 60 + atoi(time + 3);
}

int
compare(const void *p1, const void *p2)
{
	node *n1 = (node *) p1;
	node *n2 = (node *) p2;

	return n2->fromTime - n1->fromTime;
}

int
drive(node* a, node* b, int which)
{
	int res = 1;
	a[which].used = true;
	set<int>::iterator itAct = a[which].adjNodes.begin();
	set<int>::iterator itEnd = a[which].adjNodes.end();
	while (itAct != itEnd) {
		if (b[*itAct].used == false) {
			which = *itAct;
			itAct++;
			res += drive(b, a, which);
			break;
		}
		itAct++;
	}
	while (itAct != itEnd) {
		if (b[*itAct].used == false) {
			b[*itAct].indegree--;
		}
		itAct++;
	}
	return res;
}

int
main(int argc, char **argv)
{
	int numCases;
	scanf("%d", &numCases);

	for (int kases = 0; kases < numCases; kases++) {
		int turnTime;
		scanf("%d", &turnTime);

		int from, to;
		scanf("%d%d", &from, &to);
		for (int i = 0; i < from; i++) {
			scanf("%s", buffer);
			fromNodes[i].fromTime = convert(buffer);
			scanf("%s", buffer);
			fromNodes[i].toTime = convert(buffer);
			fromNodes[i].adjNodes.clear();
			fromNodes[i].indegree = 0;
			fromNodes[i].used = false;
		}
		for (int i = 0; i < to; i++) {
			scanf("%s", buffer);
			toNodes[i].fromTime = convert(buffer);
			scanf("%s", buffer);
			toNodes[i].toTime = convert(buffer);
			toNodes[i].adjNodes.clear();
			toNodes[i].indegree = 0;
			toNodes[i].used = false;
		}

		//qsort(fromNodes, from, sizeof(fromNodes[0]), compare);
		//qsort(toNodes, to, sizeof(toNodes[0]), compare);
		sort(fromNodes, fromNodes + from);
		sort(toNodes, toNodes + to);

		for (int i = 0; i < from; i++) {
			for (int j = 0; j < to; j++) {
				if (fromNodes[i].fromTime >= toNodes[j].toTime + turnTime) {
					toNodes[j].adjNodes.insert(i);
					fromNodes[i].indegree++;
				}
				if (toNodes[j].fromTime >= fromNodes[i].toTime + turnTime) {
					fromNodes[i].adjNodes.insert(j);
					toNodes[j].indegree++;
				}
			}
		}
		
		int totalA = 0;
		int totalB = 0;
		int fulfilled = 0;
		while (fulfilled < from + to) {
			for (int i = 0; i < from; i++) {
				if (fromNodes[i].used) {
					continue;
				}
				if (fromNodes[i].indegree == 0) {
					fulfilled += drive(fromNodes, toNodes, i);
					totalA++;
				}
			}
			for (int i = 0; i < to; i++) {
				if (toNodes[i].used) {
					continue;
				}
				if (toNodes[i].indegree == 0) {
					fulfilled += drive(toNodes, fromNodes, i);
					totalB++;
				}
			}
		}

		printf("Case #%d: %d %d\n", (kases + 1), totalA, totalB);
	}

	return 0;
}
