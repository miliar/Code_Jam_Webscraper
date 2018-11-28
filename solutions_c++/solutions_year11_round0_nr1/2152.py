#include<cstdio>
#include<queue>

using namespace std;

struct robot {
	int pos;
	int cur;
	int num;
	int buttons[101];

	inline void go(int t) {
		if( pos == buttons[cur] ) {
			return;
		} else if( abs(buttons[cur]-pos) <= t ) {
			pos = buttons[cur];
		} else if( buttons[cur] < pos ) {
			pos -= t;
		} else {
			pos += t;
		}
	}

	inline int doClick() {
		int dur = abs(buttons[cur]-pos) + 1;
		pos = buttons[cur];
		cur++;
		return dur;
	}

	inline void reset() {
		pos = 1;
		cur = 0;
		if( num > 0 )
			buttons[num] = buttons[num-1];
		else buttons[0] = 1;
	}
	
	inline void addNext(int p) {
		buttons[num] = p;
		num++;
	}
};

struct event{
	int pos;
	robot* obj;
	robot* other;
};

robot orange;
robot blue;
queue<event> evQueue;

int solve() {

	int rslt = 0;
	while( !evQueue.empty() ) {
		event e = evQueue.front();
		evQueue.pop();

		int t = e.obj->doClick();
		e.other->go(t);
		rslt += t;
	}

	return rslt;
}

int main() {
	int cases,numButtons;
	char c;
	scanf("%d", &cases);

	for( int i=1; i<=cases; i++ ) {
		orange.num = 0;
		blue.num = 0;
		scanf("%d", &numButtons);
		for( int k=0; k<numButtons; k++ ) {
			do {
				scanf("%c", &c);
			} while(c != 'O' && c != 'B' );
			event e;
			scanf("%d", &e.pos);
			if( c == 'O' ) {
				e.obj = &orange;
				e.other = &blue;
				orange.addNext(e.pos);
			} else {
				e.obj = &blue;
				e.other = &orange;
				blue.addNext(e.pos);
			}
			evQueue.push(e);
		}
		orange.reset();
		blue.reset();
		int seconds = solve();
		printf("Case #%d: %d\n", i, seconds);
	}

	return 0;
}
