#include <iostream>
#include <fstream>
using namespace std;

string map= "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    ifstream in("A-small-attempt1.in");
    cin.rdbuf(in.rdbuf());
    
    int n;
    cin >> n;
    string s;
    getline(cin,s);

    for (int T=0; T<n; ++T)
    {
        getline(cin, s);
        for (int i=0; i<s.length(); ++i)
            if (s[i] !=' ')
                s[i] = map[s[i]-'a'];
        cout << "Case #" << T+1 << ": " << s << endl;
    }

}

        
