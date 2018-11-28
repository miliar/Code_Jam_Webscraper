#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

#define pb push_back

using namespace std;

int t, n;
vector<int> o, b;
vector<char> order;

void init()
{
	int i, pos;
	char rob[2];

	o.clear();
	b.clear();
	order.clear();

	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%s %d", rob, &pos);
		order.pb(rob[0]);
		if (rob[0] == 'O')
			o.pb(pos);
		else
			b.pb(pos);
	}
}

int done()
{
	int cnt, o_pos, b_pos, o_ptr, b_ptr, ptr, tag;

	cnt = 0;
	o_pos = b_pos = 1;
	o_ptr = b_ptr = ptr = 0;

	while (ptr < order.size()) {
		tag = 0;
		cnt++;
		if (order[ptr] == 'O' && o_pos == o[o_ptr]) {
			o_ptr++;
			tag = 1;
		} else {
			if (o_pos < o[o_ptr])
				o_pos++;
			else if (o_pos > o[o_ptr])
				o_pos--;
		}
		if (order[ptr] == 'B' && b_pos == b[b_ptr]) {
			b_ptr++;
			tag = 1;
		} else {
			if (b_pos < b[b_ptr])
				b_pos++;
			else if (b_pos > b[b_ptr])
				b_pos--;
		}
		ptr += tag;
	}

	return (cnt);
}

int main()
{
	int i;

	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		init();
		printf("Case #%d: %d\n", i + 1, done());
	}
}


