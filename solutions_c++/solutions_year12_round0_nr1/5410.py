#include <fstream>
#include <iostream>
#include <cstring>

#define MAXG 105

using namespace std;

char g[MAXG];
char g2e[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};


#ifdef DEBUG
ifstream in("input.txt");
ofstream out("output.txt");
#endif

void print_en(char* g, int len)
{
    for(int i=0; i < len; i++)
    {
        if(g[i]==' ')
            out << ' ';
        else
            out << g2e[g[i]-'a'];
    }
    out << endl;
}

int main()
{
    int n;
    in >> n;
    in.get();
    for(int i=0; i < n; i++)
    {
        in.getline(g, MAXG);
        out << "Case #" << (i+1) << ": ";
        print_en(g, strlen(g));
    }

    return 0;
}
