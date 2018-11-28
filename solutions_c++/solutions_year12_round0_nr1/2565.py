#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main (int argc, char * const argv[]) 
{
	
	freopen("input2012_1.txt", "rt", stdin);
	freopen("output2012_1.txt", "wt", stdout);
	
//	string src = "abcdefghijklmnopqrstuvwxyz";
//	string tgt = "ynficwlbkuomxsevzpdrjgthaq";
    string tgth= "yhesocvxduiglbkrztnwjpfmaq";
    
    int T; 
	cin >> T;
	
	for(int i = 0; i <= T; i++) {
		string s;
		//cin >> s;
        getline(cin, s);
		
        if (i == 0)
            continue;
        
        cout << "Case #" << i << ": ";
        for (int j = 0; j < s.length(); j++)
        {
            if (s[j] >= 'a' && s[j] <= 'z')
            {
                cout << tgth[s[j]-'a'];
            }
            else
                cout << s[j];
            //cout << tgt[s[j] - 'a'];
        }
        cout << endl;
	}
    
	return 0;
}

