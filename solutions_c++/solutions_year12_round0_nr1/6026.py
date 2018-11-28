# include <iostream>
# include <cstdio>
using namespace std;
 
int main()
{
        char m[1000],str[2000];
        int t,i,inc = 1;
        char ch;
        m[' '] = ' ';
        m['a'] = 'y';
        m['b'] = 'h';
        m['c'] = 'e';
        m['d'] = 's';
        m['e'] = 'o';
        m['f'] = 'c';
        m['g'] = 'v';
        m['h'] = 'x';
        m['i'] = 'd';
        m['j'] = 'u';
        m['k'] = 'i';
        m['l'] = 'g';
        m['m'] = 'l';
        m['n'] = 'b';
        m['o'] = 'k';
        m['p'] = 'r';
        m['q'] = 'z';
        m['r'] = 't';
        m['s'] = 'n';
        m['t'] = 'w';
        m['u'] = 'j';
        m['v'] = 'p';
        m['w'] = 'f';
        m['x'] = 'm';
        m['y'] = 'a';
        m['z'] = 'q';
        
        scanf("%d\n",&t);
        while(t--)
        {
                cin.getline(str, 1000, '\n');
                for(i = 0; str[i]; i++)
                {
                        ch = str[i];
                        str[i] = m[ch];
                }
                printf("Case #%d: %s\n", inc++, str);
        }
        return 0;
}
         