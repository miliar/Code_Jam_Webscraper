#include <cstdio>
#include <map>
#include <cassert>

void test() {
	int n;
	std::map<int, int> lines;
	int d;
	scanf("%d", &n );
	while( n --> 0 ) {
		int a, b;
		scanf("%d %d", &a, &b );
		assert( lines.find(a) == lines.end() );

		lines[a] = b;
	}
	scanf("%d", &d);
	int reach = lines.begin()->first;
	assert( lines.find(0) == lines.end() );
	lines[0] = reach;
	
	std::map<int, int>::iterator from, to;
	from = lines.begin();
	to = lines.begin(); to++;
	while( from != to ) {
		if( from->first+from->second >= d ) {
			puts("YES");
			return;
		}
		
		while( to != lines.end() and from->first+from->second >= to->first ) {
				if( to->second > to->first-from->first )
					to->second = to->first-from->first;
				to++;
		}

		from++;
	}		

	puts("NO");
}

int main() {
	int T;
	scanf("%d", &T);
	for( int no = 1; no <= T; no++ ) {
		printf("Case #%d: ", no );
		test();
	}
	return 0;
}
