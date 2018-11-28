// Codejam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <map>
#include <stack>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <algorithm>
using namespace std;

static int T;

static void calculate(int start_pos, const vector<int>& orange, const vector<int>& blue)
{
}

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream infile("A-large-practice.in");
    ofstream outfile("A-large-practice.out");

    if(!infile || !outfile)
        exit(1);

    infile >> T;

    for(int testcase = 1; testcase <= T; ++testcase)
    {
        int N;
        infile >> N;

        int last_blue = 0, last_orange = 0;
        char prev_color = 0;
        vector<vector<pair<int, int> > > graph(N + 2);
        vector<int> position(N + 2);
        vector<int> longest_path(N + 2, 0);

        position[0] = 1;
        for(int i = 0; i < N; ++i)
        {
            char color;
            int pos;

            infile >> color >> pos;

            if(color == 'O')
            {
                graph[last_orange].push_back(make_pair(i + 1, abs(pos - position[last_orange]) + 1));
                last_orange = i + 1;
            }
            else
            {
                graph[last_blue].push_back(make_pair(i + 1, abs(pos - position[last_blue]) + 1));
                last_blue = i + 1;
            }

            if(prev_color && prev_color != color)
                graph[i].push_back(make_pair(i + 1, 1));
            prev_color = color;

            position[i + 1] = pos;
        }

        graph[last_orange].push_back(make_pair(N + 1, 0));
        graph[last_blue].push_back(make_pair(N + 1, 0));

        // calculate the longest path in DAG
        for(int j = 0; j < graph.size(); ++j)
        {
            for(int k = 0; k < graph[j].size(); ++k)
            {
                int id = graph[j][k].first;

                longest_path[id] = max(longest_path[id], longest_path[j] + graph[j][k].second);
            }
        }

        // output
        outfile << "Case #" << testcase << ": ";
        outfile << longest_path[N + 1] << endl;
    }
    
    infile.close();
    outfile.close();
    return 0;
}

