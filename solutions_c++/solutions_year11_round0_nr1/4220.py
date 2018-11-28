#include <cstdio>
#include <climits>

#define MAX_PUSHES 101

struct press {
	int button;
	int turn;
};

struct bot {
	press buttons[MAX_PUSHES];
	press *current;
	int pos;
};

int main() {
	int cases;
	scanf("%i", &cases);

	bot orange;
	bot blue;

	for(int c = 0; c < cases; ++c) {
		orange.current = orange.buttons;
		blue.current = blue.buttons;

		orange.pos = 1;
		blue.pos = 1;

		for(int i = 0; i < MAX_PUSHES; ++i) {
			orange.buttons[i].turn = INT_MAX;
			blue.buttons[i].turn = INT_MAX;
		}

		int buttons;
		scanf("%i", &buttons);
		
		for(int b = 0; b < buttons; ++b) {
			char bot[8];
			int button;
			scanf("%s %i", bot, &button);

			if(bot[0] == 'O') {
				orange.current->button = button;
				orange.current->turn = b;
				++orange.current;
			} else if(bot[0] == 'B') {
				blue.current->button = button;
				blue.current->turn = b;
				++blue.current;
			}
		}
		
		orange.current = orange.buttons;
		blue.current = blue.buttons;
		
		int pushes = 0;
		int seconds = 0;

		while(pushes < buttons) {
			bot *active;
			bot *other;

			if(orange.current->turn < blue.current->turn) {
				active = &orange;
				other = &blue;				
			} else {
				active = &blue;
				other = &orange;
			}

			if(active->pos == active->current->button) {
				++active->current;
				++pushes;
			} else if(active->pos > active->current->button)
				--active->pos;
			else
				++active->pos;

			if(other->pos > other->current->button)
				--other->pos;
			else if(other->pos < other->current->button)
				++other->pos;
				
			++seconds;
		}

		printf("Case #%i: %i\n", c + 1, seconds);
	}

	return 0;
}
