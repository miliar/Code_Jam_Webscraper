#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    int n;
    char mapping[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");

    fin >> n;
    string input;
    getline(fin, input);

    for (int i = 0; i != n; ++i) {
        fout << "Case #" << (i + 1) << ": ";
        getline(fin, input);
        for (size_t j = 0; j != input.size(); ++j) {
            fout << ((input[j] == ' ') ? ' ' : mapping[input[j] - 'a']);
        }
        fout << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
