#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;
#define for0(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define sz size


int main()
{
    map<char, char> d;
    string a = "abcdefghijklmnopqrstuvwxyz";
    string b = "ynficwlbkuomxsevzpdrjgthaq";
    for0(i, b.sz())
    {
        d[b[i]] = a[i];
    }
    
    int T = 0;
    cin >> T;
    for0(t, T)
    {
        cout << "Case #" << t + 1 << ": ";
        cin >> ws;
        string s;
        getline(cin, s);
        for0(j, s.sz())
        {
            if(s[j] == ' ')
            {
                cout << " ";
                continue;
            }
            cout << d[s[j]];
        }
        cout << endl;
    }
    return 0;
}
                
        
        

/*
int main()
{
    map<char, char> d;
    string a;
    string b;
    
    for0(i, 3)
    {     
        cin >> ws;
        getline(cin, a);
        cin >> ws;
        getline(cin, b);
        
        for0(j, a.sz())
        {
            if(!isalpha(a[j]))
                continue;
            a[j] = tolower(a[j]);
            b[j] = tolower(b[j]);
            d[a[j]] = b[j];
        }
    }
              
          
    map<char, char>::iterator it;
    for(it = d.begin(); it != d.end(); ++it)
    {
        cout << (*it).first << "    " << (*it).second << endl;
    }
    
    return 0;
}
*/
/*
a   y
b   
c
d
e
f
g
h
i
j
k
l   m
m
n
o   e
p
q
r   p
s
t
u   j
v
w
x
y
z   q
*/
