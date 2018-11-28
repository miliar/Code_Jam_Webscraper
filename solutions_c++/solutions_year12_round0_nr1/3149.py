#include <fstream>

using namespace std;

static char codex [] = {
    'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
    'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'
};

string translate (string text)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        if (text[i] == ' ')
        {
            result += ' ';
            continue;
        }
        result += codex[text[i] - 97];
    }
    return result;
}

int main()
{
    short T;
    string line;
    
    ifstream fin ("A_short_input.txt");
    ofstream fout ("A_short_output.txt");
    
    fin >> T;
    getline(fin, line);
    for (int i = 1; i <= T; i++)
    {
        getline(fin, line);
        fout << "Case #" << i << ": " << translate(line) << "\n";
    }
    
    fin.close();
    return 0;
}
