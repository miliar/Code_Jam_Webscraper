#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string map = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    ifstream in("input.in");
    int n;
    in >> n;
    string a;
    for(int j = 0; j < n; ++j)
    {
        do
        {
            getline(in, a);
        }
        while(!a.size());
        cout << "Case #" << j + 1 << ": ";
        for(int i = 0; i < a.size(); ++i)
        {
            if(a[i] != ' ')
                cout << map[a[i] - 97];
            else
                cout << " ";
        }
        cout << "\n";
    }
    return 0;
}
