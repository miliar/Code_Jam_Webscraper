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

    unsigned int getuint()
        {
            unsigned int r;
            if (fscanf(input, "%u", &r))
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


class RollerCoaster : public Problem {
    unsigned int N;
    unsigned int k;
    unsigned int R;

    struct Group {
        unsigned int size;
        unsigned int nextgroup;

        Group(unsigned int s=0, unsigned int n=0)
            : size(s), nextgroup(n)
        {

        }
    };

    struct Begin {
        unsigned long money;
        unsigned int count;

        Begin (unsigned long m=0, unsigned int c=0)
            : money(m), count(c)
        {

        }
    };

    Group queue[1000];
    int queuesize;

    Group makegroup(unsigned int* tab, int index)
    {
        unsigned int sum = 0;
        unsigned int n = 0;
        for (int i = index; ; i = (i + 1) % N) {
            if (n < N) {
                if (sum + tab[i] > k) {
                    return Group(sum, i);
                } else {
                    sum += tab[i];
                }
            } else {
                return Group(sum, i);
            }
            ++n;
        }
    }

    void makequeue()
    {
        unsigned int tab[N];
        unsigned int* ptab = tab;
        for (unsigned int i = 0; i < N; ++i) {
            *ptab = getuint();
            ++ptab;
        }

        Group* p = queue;
        unsigned int i;
        for (i = 0; i < N; ++i) {
            *p = makegroup(tab, i);
            ++p;
        }
        queuesize = i;
    }

    unsigned long solvequeue()
    {
        typedef pair<unsigned int, Begin> BeginPair;
        typedef map<unsigned int, Begin>::iterator Iter;
        map<unsigned int, Begin> begins;
        unsigned long money = 0;
        unsigned int count = 0;


        int i = 0;
        Iter iter;
        unsigned long cyclicmoney = 0;
        unsigned int cycliccount = 0;
        while (R) {
            if ((iter = begins.find(i)) != begins.end()) {
                cyclicmoney = money - iter->second.money;
                cycliccount = iter->second.count - R;
                break;
            }

            begins.insert(BeginPair(i, Begin(money, R)));

            money += queue[i].size;
            i = queue[i].nextgroup;
            --R;
        }


        if (R && cyclicmoney) {
            money += (R / cycliccount) * cyclicmoney;
            R %= cycliccount;
        }

        while (R) {
            money += queue[i].size;
            i = queue[i].nextgroup;
            --R;
        }

        return money;
    }

public:
    void solve()
    {
        int T = getint();

        for (int tc = 1; tc <= T; ++tc) {
            R = getuint();
            k = getuint();
            N = getuint();

            makequeue();
            fprintf(output, "Case #%d: %lu\n", tc, solvequeue());
        }
    }

};


int main()
{
    RollerCoaster problem;
    problem.solve();
	return 0;
}

