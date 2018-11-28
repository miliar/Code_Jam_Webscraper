#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

struct SNode
{
	int minchange;
	int oper;
	int value;
	int change;
}node[10005];
int n;
int dv;

const int INF = 1000000;

int min(int a, int b)
{
	if (a > b) return b;
	else return a;
}



void calvalue(int now)
{
	if (now*2+1 >= n)
		return;

	calvalue(now*2+1);
	calvalue(now*2+2);

	if (node[now].oper == 0) {
		node[now].value = (node[now*2+1].value || node[now*2+2].value);
	}
	else {
		node[now].value = (node[now*2+1].value && node[now*2+2].value);
	}
}

void calminchange(int now)
{
	if (now*2+1 >= n) {
		node[now].minchange = INF;
		return;
	}

	calminchange(now*2+1);
	calminchange(now*2+2);

	if (node[now].oper == 0) {
		if (node[now*2+1].value != node[now*2+2].value) {
			if (node[now].change == 1) {
				node[now].minchange = 1;
			}
			else {
				if (node[now*2+1].value == 1) {
					node[now].minchange = node[now*2+1].minchange;
				}
				else {
					node[now].minchange = node[now*2+2].minchange;
				}
			}
		}
		else if (node[now*2+1].value == 1) {
			node[now].minchange = node[now*2+1].minchange + node[now*2+2].minchange;
			if (node[now].change == 1) {
				node[now].minchange = min(node[now*2+1].minchange+1, node[now].minchange);
				node[now].minchange = min(node[now*2+2].minchange+1, node[now].minchange);
			}
		}
		else {
			node[now].minchange = min(node[now*2+1].minchange, node[now*2+2].minchange);
		}
	}
	else {
		if (node[now*2+1].value != node[now*2+2].value) {
			if (node[now].change == 1) {
				node[now].minchange = 1;
			}
			else {
				if (node[now*2+1].value == 0) {
					node[now].minchange = node[now*2+1].minchange;
				}
				else {
					node[now].minchange = node[now*2+2].minchange;
				}
			}
		}
		else if (node[now*2+1].value == 0) {
			node[now].minchange = node[now*2+1].minchange + node[now*2+2].minchange;
			if (node[now].change == 1) {
				node[now].minchange = min(node[now*2+1].minchange+1, node[now].minchange);
				node[now].minchange = min(node[now*2+2].minchange+1, node[now].minchange);
			}
		}
		else {
			node[now].minchange = min(node[now*2+1].minchange, node[now*2+2].minchange);
		}
	}

	node[now].minchange = min(node[now].minchange, INF);
}


int solve()
{
	calvalue(0);

	if (node[0].value == dv) return 0;

	calminchange(0);

	return node[0].minchange;
}


int main()
{
	int i, j, k;
	int t;
	int nowt;
	int temp;

	freopen("A-large.in.txt", "r", stdin);
//	freopen("A-large.out.txt", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t--) {
		nowt ++;

		scanf("%d%d", &n, &dv);
		for (i = 0; i < (n-1)/2; i ++) {
			scanf("%d%d", &node[i].oper, &node[i].change);
		}
		for (i = (n-1)/2; i < n; i ++) {
			scanf("%d", &node[i].value);
		}

		temp = solve();

		if (temp == INF)
			printf("Case #%d: IMPOSSIBLE\n", nowt);
		else
			printf("Case #%d: %d\n", nowt, temp);
	}

	return 0;
}
