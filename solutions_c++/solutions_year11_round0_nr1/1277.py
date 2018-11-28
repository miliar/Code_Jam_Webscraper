#include <cstdio>

#include <vector>
using namespace std;

struct TCommand {
	int Robot;
	int Button;
	int Executed;

	TCommand()
		: Executed(1234567890)
	{
	}
};

struct TState {
	int Pos;
	int Command;

	TState()
		: Pos(1)
		, Command(0)
	{
	}
};

typedef vector<TCommand> TCommands;

void Do(int time, int index, TState& state, TCommands& commands) {
	while (state.Command < commands.size() && commands[state.Command].Robot != index)
		++state.Command;
	if (state.Command < commands.size()) {
		if (state.Pos == commands[state.Command].Button) {
			int j = 0;
			while ( (j < state.Command) && (commands[j].Executed < time) )
				++j;
			if (j == state.Command) {
				commands[state.Command].Executed = time;
				++state.Command;
			}
		}
		else if (commands[state.Command].Button < state.Pos)
			--state.Pos;
		else if (commands[state.Command].Button > state.Pos)
			++state.Pos;
	}
}

int main() {
	// freopen("A-small-attempt0.in", "r", stdin);
	// freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int iTest = 0; iTest < t; ++iTest) {
		int n;
		scanf("%d", &n);
		TCommands commands;
		for (int i = 0; i < n; ++i) {
			char ch;
			do {
				scanf("%c", &ch);
			}
			while ( (ch != 'O') && (ch != 'B') );
			TCommand c;
			c.Robot = (ch == 'B');
			scanf("%d", &c.Button);
			commands.push_back(c);
		}

		TState orange, blue;
		int time = 0;
		while ( (orange.Command < commands.size()) || (blue.Command < commands.size()) ) {
			++time;
			Do(time, 0, orange, commands);
			Do(time, 1, blue, commands);
		}
		printf("Case #%d: %d\n", iTest + 1, time);
	}

	return 0;
}