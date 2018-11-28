#include<iostream>
#include<string>
#include<map>

using namespace std;

int main()
{
    map<char,char> dict;
    
    dict.insert( pair<char,char>(' ',' '));
    dict.insert( pair<char,char>('a','y'));
    dict.insert( pair<char,char>('b','h'));
    dict.insert( pair<char,char>('c','e'));
    dict.insert( pair<char,char>('d','s'));
    dict.insert( pair<char,char>('e','o'));
    dict.insert( pair<char,char>('f','c'));
    dict.insert( pair<char,char>('g','v'));
    dict.insert( pair<char,char>('h','x'));
    dict.insert( pair<char,char>('i','d'));
    dict.insert( pair<char,char>('j','u'));
    dict.insert( pair<char,char>('k','i'));
    dict.insert( pair<char,char>('l','g'));
    dict.insert( pair<char,char>('m','l'));
    dict.insert( pair<char,char>('n','b'));
    dict.insert( pair<char,char>('o','k'));
    dict.insert( pair<char,char>('p','r'));
    dict.insert( pair<char,char>('q','z'));
    dict.insert( pair<char,char>('r','t'));
    dict.insert( pair<char,char>('s','n'));
    dict.insert( pair<char,char>('t','w'));
    dict.insert( pair<char,char>('u','j'));
    dict.insert( pair<char,char>('v','p'));
    dict.insert( pair<char,char>('w','f'));
    dict.insert( pair<char,char>('x','m'));
    dict.insert( pair<char,char>('y','a'));
    dict.insert( pair<char,char>('z','q'));
    
	int T;
    cin >>T;
    
    string S;
    getline(cin, S);
    
    for (int t=0; t<T; ++t)
    {
        getline(cin, S);
        
        string G;
        for (int i=0; i<S.size(); ++i)
            G += dict[S[i]];
        
        cout << "Case #" << t+1 << ": " << G << endl;
    }
}