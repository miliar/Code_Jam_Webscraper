#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;
typedef unsigned long long ull;


int main()
{
    char map[] = "yhesocvxduiglbkrztnwjpfmaq";
    int cases;
    string s;  

    cin >> cases;
    getline(cin, s);
    int idx= 1;    
    while(cases--)
    {
        
        cout << "Case #"<<idx<<": ";
        getline(cin, s);
        int len = s.size();
        for(int i = 0 ; i < len; i++)
        { 
           if(s[i] != ' ')
                cout<< map[s[i] - 'a'];
            else
                cout << " ";
        }   
        cout << endl;
        idx++;
    }
    

    return 0;
}
