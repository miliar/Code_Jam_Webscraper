#include <cstdio>
#include <list>

using namespace std;

class Robot
{
public:
	void init(const list<int> & b) {
		btns = b;
		pushed = false;
		canpush = false;
		current_pos = 1;
		set_next_target();
	}

	bool isPushed() {
		return pushed;
	}

	void go() {
		canpush = true;
		pushed = false;
	}

	void wait() {
		canpush = false;
		pushed = false;
	}

	void process() {
		if (current_pos == target_pos) {
			if (canpush) {
				pushed = true;
				set_next_target();
			} else {
				/* wait */
			}
		} else if (current_pos < target_pos) {
			current_pos++;
		} else {
			current_pos--;
		}
	}
private:
	void set_next_target() {
		if (!btns.empty()) {
			target_pos = btns.front();
			btns.pop_front();
		}
	}

	bool pushed;
	bool canpush;
	int current_pos;
	int target_pos;
	list<int> btns;
};

Robot blue;
Robot orange;
list<int> schedule;

void printv(const list<int> &v)
{
	list<int>::const_iterator it = v.begin();
	while (it != v.end()) {
		printf("%d ", *it);
		++it;
	}
	printf("\n");
}

void
make_positions(list<int> &blue, list<int> &orange)
{
	int n = 0;
	scanf("%d ", &n);
	for (int i = 0; i < n; ++i) {
		char type;
		int btn;
		scanf("%c ", &type);
		if (i+1 == n) {
			scanf("%d", &btn);
		} else {
			scanf("%d ", &btn);
		}
		if (type == 'B') {
			blue.push_back(btn);
		} else {
			orange.push_back(btn);
		}
		schedule.push_back(type);
	}
} 

bool
scheduling()
{
	if (!schedule.empty()) {
		int s = schedule.front();
		schedule.pop_front();
		if (s == 'B') {
			blue.go();
			orange.wait();
		} else {
			orange.go();
			blue.wait();
		}
		return true;
	} else {
		return false;
	}
}

int run()
{
	bool done = false;
	int tick = 0;
	scheduling();
	while (true) {
		blue.process();
		orange.process();
		tick++;

		if (blue.isPushed() || orange.isPushed()) {
			if (!scheduling()) {
				break;
			}
		}
	}
	return tick;
}

int main(int argc, char **argv)
{
	int numcase = 0;
	scanf("%d", &numcase);
	for (int i = 0; i < numcase; ++i) {
		list<int> blue_positions;
		list<int> orange_positions;
	
		//blue_positions.push_back(1);
		//orange_positions.push_back(1);
		make_positions(blue_positions, orange_positions);

		blue.init(blue_positions);
		orange.init(orange_positions);

		printf("Case #%d: %d\n", i+1, run());
	}
	return 0;
}
