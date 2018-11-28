#include <fstream>
#include <string>
using namespace std;

char repl[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

ifstream inf("Input.txt");
ofstream outf("Output.txt");

int main() {
    int n; inf >> n;
    string G; getline(inf, G);
    for (int i = 0; i < n; i++) {
        getline(inf, G);
        outf << "Case #" << i+1 << ": ";
        for (int j = 0; j < (int)G.length(); j++)
            if (G[j] == ' ') outf << ' ';
            else outf << repl[G[j]-'a'];
        outf << "\n";
    }
}
