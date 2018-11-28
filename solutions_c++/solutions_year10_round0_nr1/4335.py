#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cctype>
#include <list>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;
static const double pi = 2 * acos(0.0);

template<typename T>
inline T sqr(T x)
{
    return x * x;
}


class Problem {
    string outstring;

protected:
    FILE* input;
    FILE* output;

    string& getline()
    {
        outstring.clear();

        char c = fgetc(input);
        while (c != '\n' && c != EOF)
        {
            outstring.push_back(c);
            c = fgetc(input);
        }

        return outstring;
    }

    char getchar()
    {
        return fgetc(input);
    }

    int getint()
    {
        int r;
        if (fscanf(input, "%d", &r))
            return r;
        return 0;
    }

    double getdouble()
    {
        double r;
        if (fscanf(input, "%lf", &r))
            return r;
        return 0;
    }

    string& getword()
    {
        outstring.clear();

        char c = fgetc(input);
        while (!isspace(c) && c != EOF) {
            outstring.push_back(c);
            c = fgetc(input);
        }

        return outstring;
    }

public:
    Problem(const char* fin="input.txt", const char* fout="output.txt")
    {
        input = fopen(fin, "r");
        output = fopen(fout, "w");
    }

    ~Problem()
    {
        fclose(input);
        fclose(output);
    }

    virtual void solve() = 0;
};


void printchar(char c)
{
    printf("%c", c);
}


class SnapperChain : public Problem {
    typedef bool Power;

    enum State {
        OFF,
        ON
    };

    struct Snapper {
        Power power;
        State state;

        Snapper(Power p=false, State s=OFF)
            : power(p), state(s)
        {

        }

        void toggle()
        {
            if (state == OFF)
                state = ON;
            else
                state = OFF;
        }
    };

    typedef vector<Snapper> Chain;
    Chain chain;

    void buildchain(int n)
    {
        chain.clear();
        chain.push_back(Snapper(true, OFF));
        for (int i = 1; i < n; ++i) {
            chain.push_back(Snapper(false, OFF));
        }
    }

    void snap()
    {
        typedef Chain::iterator Iter;

        chain[0].toggle();
        for (Iter i = chain.begin() + 1; i != chain.end(); ++i) {
            if (i->power) {
                i->toggle();
            }
        }

        for (Iter i = chain.begin() + 1; i != chain.end(); ++i) {
            if ((i - 1)->power && (i - 1)->state == ON) {
                i->power = true;
            } else {
                i->power = false;
            }
        }
    }


public:
    void solve()
    {
        int t = getint();

        for (int tc = 1; tc <= t; ++tc) {
            int n = getint();
            int k = getint();

            printf("%d %d\n", n, k);
            buildchain(n);
            for (int i = 0; i < k; ++i) {
                snap();
            }

            string out;
            if (chain[n - 1].state == ON && chain[n - 1].power == true) {
                out = string("ON");
            } else {
                out = string("OFF");
            }

            printf("Case #%d: %s\n", tc, out.c_str());
            fprintf(output, "Case #%d: %s\n", tc, out.c_str());
        }
    }

};


int main()
{
    SnapperChain problem;
    problem.solve();
	return 0;
}

