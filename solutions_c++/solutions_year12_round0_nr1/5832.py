#include <iostream>
#include <map>


using namespace std;

void preliminary()
{
    map<char,char> m, rm;
    m['a'] = 'y';
    m['o'] = 'e';
    m['z'] = 'q';
    rm['z']= 'q';
    rm[' '] = ' ';
    bool found[100];
    string s[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string o[3] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
    for (int i = 0; i < 100; i++)
    {
        found[i] = false;
    }
    
    found['z'-'a'] = true;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < s[i].size(); j++)
        {
            m[s[i][j]] = o[i][j];
            found[s[i][j]-'a'] = true;
        }
        
    }
    char a= 'a';
    for (int i = 0; i <= 'z'-'a'; i++, ++a)
    {
        if (!found[i])
        {
            cout << "not found: " << a << endl;
        }
    }
    
    
    for (map<char,char>::const_iterator it = m.begin(); it != m.end() ; ++it)
    {
        rm[it->second] = it->first;
    }
    for (char i = 'a'; i <= 'z'; i++)
    {
        cout << i  << ":  " << rm[i] << endl;
    }
}
int main()
{
    //~ preliminary();
    
    map<char,char> m, rm;
    m[' '] = ' ';
    m['a'] = 'y';
    m['o'] = 'e';
    m['z'] = 'q';
    m['q'] = 'z';
    string s[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string o[3] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < s[i].size(); j++)
        {
            m[o[i][j]] = s[i][j];
        }
    }
    for (map<char,char>::const_iterator it = m.begin(); it != m.end() ; ++it)
    {
        rm[it->second] = it->first;
    }
    
    int T;
    cin >> T;
    cin.get();
    for (int i = 0; i < T; i++)
    {
        //~ string temp;
        //~ getline(cin, temp);
        //~ for (int j = 0; j < temp.size(); j++)
        //~ {
            //~ temp[j] = rm[temp[j]];
        //~ }
        cout << "Case #" << i+1 << ": " ;
        char temp = cin.get();
        while(temp != '\n')
        {
            //~ if (rm[temp]==0)
            //~ {
                //~ cout << "problema con " << temp << endl;
            //~ }
            
            cout << rm[temp];
            temp = cin.get();
        }
        cout << endl;
    }
     
}
