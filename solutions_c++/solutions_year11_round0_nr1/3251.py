//Parse the input

//for each command in sequence
// Determine who is to push button (pusher) and who is to wait (waiter)
// While pusher is not at the proper position
//   Advance pusher
//   Determine if waiter should move (by looking at the next cmd for waiter), if so
//   advance waiter
//   Timer++
// Timer++ (takes a time unit to push)

#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::pair;
using std::string;
using std::vector;

typedef pair<char,int> Command;
typedef vector<Command > Sequence;

vector<Sequence> ParseInput(const string& filename) {

    vector<Sequence> res;

    std::ifstream fin;
    fin.open(filename.c_str(), std::ifstream::in);
    if (fin.fail()) {
        cout << "Failed to open " << filename << endl;
        return res;
    }

    int num_sequences;
    fin >> num_sequences;
    for (int i = 0; i < num_sequences; ++i) {
        int num_commands;
        fin >> num_commands;
        Sequence this_sequence;
        for (int j = 0; j < num_commands; ++j) {
            char bot;
            int position;
            fin >> bot >> position;
            this_sequence.push_back(std::make_pair(bot, position));
        }
        res.push_back(this_sequence);
    }

    fin.close();

    return res;
}

int ShouldMove(const char& bot, const Sequence& input, const int& next_idx, std::map<char,int>& bot_positions) {

    // no more commands for this bot
    if (next_idx == -1 || input[next_idx].second - bot_positions[bot] == 0)
        return 0;

    int movement = (input[next_idx].second - bot_positions[bot]) > 0 ? 1 : -1;

    return movement;
}

int NextInstructionIdx(const char& bot, const Sequence& commands, const int& current_idx) {

    int num_commands = commands.size();
    for (int i = current_idx + 1; i < num_commands; ++i) {
        if (commands[i].first == bot)
            return i;
    }
    return -1;
}

int Simulation(Sequence input) {

    int num_commands = input.size();
    std::map<char, int> bot_positions;
    bot_positions['O'] = 1;
    bot_positions['B'] = 1;
    std::map<char, int> next_instruction_idx;
    int timer = 0;
    for (int i = 0; i < num_commands; ++i) {
        Command command = input[i];
        char pusher, waiter;
        if (command.first == 'O') {
            pusher = 'O';
            waiter = 'B';
        }
        else {
            pusher = 'B';
            waiter = 'O';
        }

        next_instruction_idx[pusher] = i;
        next_instruction_idx[waiter] = NextInstructionIdx(waiter, input, i);

        int button_pos = command.second;
        while (bot_positions[pusher] != button_pos) {
            if (bot_positions[pusher] > button_pos)
                bot_positions[pusher]--;
            else
                bot_positions[pusher]++;

            bot_positions[waiter] += ShouldMove(waiter, input, next_instruction_idx[waiter], bot_positions);
            timer++;

//            cout << "Time " << timer << ": "
//                 << pusher << " moved to " << bot_positions[pusher] << ", "
//                 << waiter << " moved to " << bot_positions[waiter] << endl;
        }

        // while the pusher is pushing the button, the waiter can still move
        bot_positions[waiter] += ShouldMove(waiter, input, next_instruction_idx[waiter], bot_positions);
        timer++;
//        cout << "Time " << timer << ": "
//             << pusher << " pushed buttom at " << bot_positions[pusher] << ", "
//             << waiter << " moved to " << bot_positions[waiter] << endl;
    }

    return timer;
}

int main(int argc, char** argv) {

    vector<Sequence> all_sequences = ParseInput(string(argv[1]));

    int num_sequences = all_sequences.size();
    vector<int> required_time(num_sequences, 0);
    std::ofstream fout;
    fout.open("output.txt",std::ofstream::out);
    if (fout.fail()) {
        cout << "Failed to open output.txt for writing." << endl;
        return 1;
    }
    for (int i = 0; i < num_sequences; ++i) {
        required_time[i] =  Simulation(all_sequences[i]);
        fout << "Case #" << i+1 << ": " << required_time[i] << endl;
    }

    fout.close();
    return 0;
}
