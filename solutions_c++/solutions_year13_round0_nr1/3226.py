#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

template <class T> std::string toString( const T &t ) { ostringstream oss; oss << t; return std::string (oss.str()); }


class Input
{
    public:
        string board[4];
};

class Output
{
    public:
        int state;
};

std::ostream& operator<<(std::ostream& o, const Output & output)
{
    switch (output.state)
    {
    case 0:
        o << "Draw";
        break;
    case 1:
        o << "X won";
        break;
    case 2:
        o << "O won";
        break;
    case 3:
        o << "Game has not completed";
    }
    return o;
}

class Parser
{
    public:
        void parse(string filename, vector<Input> & input);
};

class Solver
{
    public:
        void solve(Input & input, Output & output);
};

void Parser::parse(string filename, vector<Input> & inputs)
{
    ifstream fs(filename);
    int nbCase;
    fs >> nbCase;
    inputs.resize(nbCase);

    string line;
    getline(fs, line);
    for (int i = 0; i < nbCase; ++i)
    {
        Input & input = inputs[i];
        getline(fs, input.board[0]);
        getline(fs, input.board[1]);
        getline(fs, input.board[2]);
        getline(fs, input.board[3]);
        getline(fs, line);
    }
}

void Solver::solve(Input & input, Output & output)
{
    output.state = 0;

    int X;
    int O;
    for (unsigned int i = 0; i < 4; ++i)
    {
        X = 0;
        O = 0;
        for (unsigned int j = 0; j < 4; ++j)
        {
            if (input.board[i][j] == 'T' || input.board[i][j] == 'X')
                ++X;
            if (input.board[i][j] == 'T' || input.board[i][j] == 'O')
                ++O;
        }
        if (X == 4)
            output.state = 1;
        else if (O == 4)
            output.state = 2;
    }

    for (unsigned int i = 0; i < 4; ++i)
    {
        X = 0;
        O = 0;
        for (unsigned int j = 0; j < 4; ++j)
        {
            if (input.board[j][i] == 'T' || input.board[j][i] == 'X')
                ++X;
            if (input.board[j][i] == 'T' || input.board[j][i] == 'O')
                ++O;
        }
        if (X == 4)
            output.state = 1;
        else if (O == 4)
            output.state = 2;
    }

    X = 0;
    O = 0;
    for (unsigned int i = 0; i < 4; ++i)
    {
        if (input.board[i][i] == 'T' || input.board[i][i] == 'X')
            ++X;
        if (input.board[i][i] == 'T' || input.board[i][i] == 'O')
            ++O;
    }
    if (X == 4)
        output.state = 1;
    else if (O == 4)
        output.state = 2;

    X = 0;
    O = 0;
    for (unsigned int i = 0; i < 4; ++i)
    {
        if (input.board[3-i][i] == 'T' || input.board[3-i][i] == 'X')
            ++X;
        if (input.board[3-i][i] == 'T' || input.board[3-i][i] == 'O')
            ++O;
    }
    if (X == 4)
        output.state = 1;
    else if (O == 4)
        output.state = 2;

    if (output.state == 0)
        for (unsigned int i = 0; i < 4; ++i)
            for (unsigned int j = 0; j < 4; ++j)
                if (input.board[i][j] == '.')
                    output.state = 3;
}


int main(int argc, char * argv[])
{
    if (argc != 2)
    {
        std::cout << "no input!" << std::endl;
        return EXIT_FAILURE;
    }

    vector<Input> inputs;
    vector<Output> outputs;
    Parser p;
    Solver s;
    p.parse(argv[1], inputs);

    outputs.resize(inputs.size());
    for (unsigned int i = 0; i < inputs.size(); ++i)
        s.solve(inputs[i], outputs[i]);

    for (unsigned int c = 0; c < outputs.size(); ++c)
    {
        cout << "Case #" << c+1 << ": ";
        cout << outputs[c] << endl;
    }

    return EXIT_SUCCESS;
}
