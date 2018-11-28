#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

struct move_type
{
    int robot;
    int button;
};

#define ABS(x) ((x) > 0 ? (x) : (-1 * (x)))

vector<vector<move_type> > g_allcases;

bool read_input()
{
    ifstream fin;
    //fin.open("/home/gerald/Desktop/Codejam2011_A/inputA.txt");
    fin.open("/home/gerald/Desktop/Codejam2011_A/A-large.in");
    int n_inp;
    fin >> n_inp;
    g_allcases.clear();
            //cout <<"Here2:" << n_inp <<endl;
    for(int oi=0; oi < n_inp; oi++)
    {
        vector<move_type> v_moves;
        int n_e;
        fin >> n_e;
        for(int ii = 0; ii < n_e; ii++)
        {
            char r;
            int b;
            move_type m;
            fin >> r;
            fin >> b;
            m.robot = (r == 'O') ? 0 : 1;
            m.button = b;
            //cout <<"Here";
            v_moves.push_back(m);
        }
        g_allcases.push_back(v_moves);
    }
    return true;
}

int process(int idx)
{
    int ttime = 0;
    int pos0 = 1;
    int pos1 = 1;
    int buf0 = 0;
    int buf1 = 0;
    vector<move_type> vmoves = g_allcases[idx];
    for(int i = 0; i < vmoves.size(); i++)
    {
        move_type cm = vmoves[i];
        if(cm.robot == 0)
        {
            int t = ABS(cm.button - pos0);
            t -= buf0;
            if(t <= 0) t=1;
            else t++;
            if(t > 0)
            {
                buf1 += t;
                ttime += t;
            }
            buf0 = 0;
            pos0 = cm.button;
        }
        else
        {
            int t = ABS(cm.button - pos1);
            t -= buf1;
            if(t <= 0) t=1;
            else t++;
            if(t > 0)
            {
                buf0 += t;
                ttime += t;
            }
            buf1 = 0;
            pos1 = cm.button;
        }
        //cout << ttime << ":" << cm.robot << "," << cm.button << endl;
    }
    return ttime;
}

int main()
{
    if(!read_input())
        return -1;

    //cout << g_allcases.size() << endl;
    for(int i = 0; i < g_allcases.size(); i++)
        cout << "Case #" << (i+1) << ": " << process(i) << endl;
    return 0;
}
