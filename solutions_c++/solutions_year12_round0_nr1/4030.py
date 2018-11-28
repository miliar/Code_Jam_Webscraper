#include <iostream>
#include <map>

using namespace std;



/*char mp[30] = {  
              'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','q','p',
                'd','r','j','g','t','h','a',
                'z'

              }; */

int main()
{
    
    
map<char , char> cmp;

cmp['y'] = 'a';
cmp['n'] = 'b';
cmp['f'] = 'c';
cmp['i'] = 'd';
cmp['c'] = 'e';
cmp['w'] = 'f';
cmp['l'] = 'g';
cmp['b'] = 'h';
cmp['k'] = 'i';
cmp['u'] = 'j';
cmp['o'] = 'k';
cmp['m'] = 'l';
cmp['x'] = 'm';
cmp['s'] = 'n';
cmp['e'] = 'o';
cmp['v'] = 'p';
cmp['q'] = 'z';
cmp['p'] = 'r';
cmp['d'] = 's';
cmp['r'] = 't';
cmp['j'] = 'u';
cmp['g'] = 'v';
cmp['t'] = 'w';
cmp['h'] = 'x';
cmp['a'] = 'y';
cmp['z'] = 'q';

map<char,char>::iterator chrT;


    int tetC;
    cin >> tetC;
    char name[105];
    cin.getline (name,150);
   
    for(int cnt = 1; cnt <= tetC; cnt++)
    {
            cin.getline(name,150);
            int clen = strlen(name);
            cout << "Case #" << cnt << ": ";
            for(int cCnt = 0; cCnt < clen; cCnt++)
            {
                    char curChr = name[cCnt];
                    if(curChr != ' ')
                    {
                              chrT=cmp.find(curChr);
                              curChr = chrT->second;
                    }
                    cout << curChr;
            }                 
            cout << endl; 
            
    }
    return 0;
}
