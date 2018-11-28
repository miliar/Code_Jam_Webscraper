#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ifstream ifs("A-large.in", ifstream::in);
    ofstream ofs("A-large.out", ifstream::out);
    string line;
    getline(ifs, line);
    int cases = 0;
    while (getline(ifs, line))
    {
        ++cases;
        int opos = 1, bpos = 1, onext = 0, bnext = 0;
        istringstream iss(line);
        char color;
        int button;
        int num;
        iss >> num;
        vector< pair <char,int> > buttons;
        vector<int> orange, blue;
        buttons.reserve(num);
        iss.ignore(1);
        while (iss.good())
        {
            iss >> color;
            iss >> button;
            buttons.push_back(make_pair(color, button));
            iss.ignore(1);
            switch (color)
            {
            case 'B' :
                blue.push_back(button);
                break;
            case 'O' :
                orange.push_back(button);
                break;
            default:
                cerr << "Error!!\n";
            }
        }
        orange.resize(1,1);
        blue.resize(1,1);
        int i = 0;
        int seconds = 0;
        while (i != buttons.size())
        {
            while ((buttons[i].first == 'B' ? bpos : opos) != buttons[i].second)
            {
                ++seconds;
                if (orange[onext] > opos)
                    ++opos;
                if (orange[onext] < opos)
                    --opos;
                if (blue[bnext] > bpos)
                    ++bpos;
                if (blue[bnext] < bpos)
                    --bpos;
                //cout << opos << " ; " << bpos << "\n";
            }

            //cout << buttons[i].first << buttons[i].second << "\n";
            if (buttons[i].first == 'B')
            {
                ++bnext;
                if (orange[onext] > opos)
                    ++opos;
                if (orange[onext] < opos)
                    --opos;
            }
            else
            {
                ++onext;
                if (blue[bnext] > bpos)
                    ++bpos;
                if (blue[bnext] < bpos)
                    --bpos;
            }
            ++seconds;
            ++i;
        }

        ofs << "Case #" << cases << ": " << seconds << "\n";
    }

    ifs.close();

    return 0;
}
