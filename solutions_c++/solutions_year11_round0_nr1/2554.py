#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    int T, N, const_T;
    int P_i;
    char R_i;
    int seconds = 0;
    vector<char> steps;
    vector<int> orange, blue;
    int cur_orange_pos, cur_blue_pos, orange_step, blue_step;
    
    in >> T;
    const_T = T;
    while (T) {
        in >> N;
        steps.clear();
        orange.clear();
        blue.clear();
        cur_orange_pos = cur_blue_pos = 1;
        for (int i = 0; i < N; ++i) {
            in >> R_i >> P_i; 
            steps.push_back(R_i);
            if (R_i == 'O')
                orange.push_back(P_i);
            else
                blue.push_back(P_i);     
        }
        seconds = 0;
        while (!steps.empty()) {
            if (!orange.empty())
                orange_step = (cur_orange_pos > orange[0])? (-1): 1;
            if (!blue.empty())
                blue_step = (cur_blue_pos > blue[0])? (-1): 1;
                
            if (steps.front() == 'O') {
                if (orange.front() == cur_orange_pos) {
                    orange.erase(orange.begin());      
                    steps.erase(steps.begin());
                }        
                else
                    cur_orange_pos += orange_step;  
                if (!blue.empty() && cur_blue_pos != blue.front())
                    cur_blue_pos += blue_step;
            }
            else {
                if (blue.front() == cur_blue_pos) {
                    blue.erase(blue.begin());      
                    steps.erase(steps.begin());
                }        
                else
                    cur_blue_pos += blue_step;     
                if (!orange.empty() && cur_orange_pos != orange.front())
                    cur_orange_pos += orange_step;     
            } 
            seconds++;     
        }
        out << "Case #" << (const_T - T + 1) << ": ";
        out << seconds << endl;
        T--;      
    }
    
    return 0;    
}
