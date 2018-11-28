#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct Command
{
	char bot;
	int button;
};

int main() {
	fstream file("a.in");
	if (!file.is_open()) {
		cout<<"nofile";
		return 0;
	}
	int numcases = 0;
	file >> numcases;
	for (int i = 0; i < numcases; ++i) {
		vector<Command> commands;
		int numCommands = 0;
		int result = 0;
		int bPos = 1;
		int oPos = 1;
		file >> numCommands;
		for (int x = 0; x < numCommands; ++x) {
			Command cmd;
			file >> cmd.bot >> cmd.button;
			commands.push_back(cmd);
		}
		bool remove = false;
		while (!commands.empty()) {
			Command &cmd = commands[0];
			if (cmd.bot == 'O') {
				if (cmd.button == oPos) {
					remove = true;
				} else {
					oPos += oPos < cmd.button ? 1 : -1;
				}
				for (int y = 0; y < commands.size(); ++y) {
					if (commands[y].bot == 'B') {
						if (bPos != commands[y].button)
							bPos += bPos < commands[y].button ? 1 : -1;
						break;
					}
				}
			} else {
				if (cmd.button == bPos) {
					remove = true;
				} else {
					bPos += bPos < cmd.button ? 1 : -1;
				}
				for (int y = 0; y < commands.size(); ++y) {
					if (commands[y].bot == 'O') {
						if (oPos != commands[y].button)
							oPos += oPos < commands[y].button ? 1 : -1;
						break;
					}
				}
			}
			//cout << "o: " << oPos << " b: " << bPos << endl;
			++result;
			if (remove)
				commands.erase(commands.begin());
			remove = false;
		}
		cout << "Case #"<<i+1<<": " << result << endl;
	}
}