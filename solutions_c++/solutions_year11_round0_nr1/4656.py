#include <fstream>
#include <vector>

using namespace std;


typedef struct {
    char robot;
    int button;
} command;


int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T, t;
    
    fin >> T;
    
    
    for (t = 1; t <= T; t++) {
        vector<command> commands;
        int cmd_orange, cmd_orange_next;
        int cmd_blue, cmd_blue_next;
        command temp;
        int orange, blue;
        int time = 0;
        int N;
        int i, j;
        
        orange = blue = 1;
        
        fin >> N;
        
        for (i = 0; i < N; i++) {
            fin >> temp.robot >> temp.button;
            commands.push_back(temp);
        }
        
        for (cmd_orange_next = 0; cmd_orange_next < N; cmd_orange_next++)
            if (commands[cmd_orange_next].robot == 'O')
                break;
        
        for (cmd_blue_next = 0; cmd_blue_next < N; cmd_blue_next++)
            if (commands[cmd_blue_next].robot == 'B')
                break;
        
        for (;;) {
            if (cmd_orange_next == N && cmd_blue_next == N)
                break;
            
            cmd_orange = cmd_orange_next;
            cmd_blue = cmd_blue_next;
            
            if (cmd_orange < N) {
                if (commands[cmd_orange].button == orange) {
                    if (cmd_orange < cmd_blue)
                        for (cmd_orange_next = cmd_orange + 1; cmd_orange_next < N; cmd_orange_next++)
                            if (commands[cmd_orange_next].robot == 'O')
                                break;
                }
                else if (commands[cmd_orange].button < orange)
                    orange--;
                else
                    orange++;
            }
            
            if (cmd_blue < N) {
                if (commands[cmd_blue].button == blue) {
                    if (cmd_blue < cmd_orange)
                        for (cmd_blue_next = cmd_blue + 1; cmd_blue_next < N; cmd_blue_next++)
                            if (commands[cmd_blue_next].robot == 'B')
                                break;
                }
                else if (commands[cmd_blue].button < blue)
                    blue--;
                else
                    blue++;
            }
            
            time++;
        }
        
        fout << "Case #" << t << ": " << time << endl;
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}
