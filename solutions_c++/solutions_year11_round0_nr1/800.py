#include <iostream>
#include <cmath>
using namespace std;

struct Node
{
	int r;
	int pos;
}a[150];

int pos[2];
int next[2];
	

void getNext(int index , int n)
{
	next[0] = -1;
	next[1] = -1;
	for (int i=index ; i<n ; i++) {
		if (a[i].r == 0) {
			next[0] = a[i].pos;
			break;
		}
	}

	for (int i=index ; i<n ; i++) {
		if (a[i].r == 1) {
			next[1] = a[i].pos;
			break;
		}
	}
}

void process(int id , int steps)
{
	if (next[id] == -1)
		return ;
	if (pos[id] < next[id]) {
		if (pos[id] + steps <= next[id])
			pos[id] += steps;
		else
			pos[id] = next[id];
	}
	else {
		if (pos[id] - steps >= next[id]) 
			pos[id] -= steps;
		else
			pos[id] = next[id];
	}
}

int getFirst(int index)
{
	return a[index].r;
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int t;
	int n;
	char s[2];
	int index;
	int firstRole;
	int steps;
	int ans;
	int cas = 0;

	scanf("%d" , &t);
	while (t--) {
		cas++;

		scanf("%d" , &n);
		for (int i=0 ; i<n ; i++) {
			scanf("%s %d" , s , &a[i].pos);
			if (s[0] == 'O')
				a[i].r = 0;
			else
				a[i].r = 1;
		}
		
		index = 0;	
		pos[0] = 1;
		pos[1] = 1;
		ans = 0;

		while (index < n) {
			getNext(index , n);
			firstRole = getFirst(index);
			steps = abs(pos[firstRole] - next[firstRole]);
			ans += steps;
			process(0 , steps);
			process(1 , steps);
			ans++;
			process(1 - firstRole , 1);
			index++;
		}
		
		printf("Case #%d: %d\n" , cas , ans);
	}

	return 0;
}