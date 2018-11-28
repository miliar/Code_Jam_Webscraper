#include <iostream>

using namespace std;
#define BUFFER_SIZE 4000

char buffer[BUFFER_SIZE];
/*
 W e have come up with* the best possible language here at Google, called Googlerese. 
 To translate text into Googlerese, we take any message and replace each English letter
 with another English letter. This mapping is one-to-one and onto, which means that the 
 same input letter always gets replaced with the same output letter, and different input
 letters always get replaced with different output letters. A letter may be replaced 
 by itself. Spaces are left as-is.
 
 For example (and here is a hint!), our awesome translation algorithm includes the 
 following three mappings: 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'. This means that "a zoo"
 will become "y qee".
 
 Googlerese is based on the best possible replacement mapping, and we will never change 
 it. It will always be the same. In every test case. We will not tell you the rest of our 
 mapping because that would make the problem too easy, but there are a few examples below 
 that may help.
 
 Given some text in Googlerese, can you translate it to back to normal text?
 Solving this problem
*/

/**!
 * 3
 * ejp mysljylc kd kxveddknmc re jsicpdrysi
 * rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
 * de kr kd eoya kw aej tysr re ujdr lkgc jv
 * 
 * 
 Output
 * Case #1: our language is impossible to understand
 * Case #2: there are twenty six factorial possibilities
 * Case #3: so it is okay if you want to just give up
 * 
 */

static char mapping[255];

static void initMapping()
{
    mapping['a'] = 'y';
    mapping['b'] = 'h';
    mapping['c'] = 'e';
    mapping['d'] = 's';
    mapping['e'] = 'o';
    mapping['f'] = 'c';
    mapping['g'] = 'v';
    mapping['h'] = 'x';
    mapping['i'] = 'd';
    mapping['j'] = 'u';
    mapping['k'] = 'i';
    mapping['l'] = 'g';
    mapping['m'] = 'l';
    mapping['n'] = 'b';
    mapping['o'] = 'k';
    mapping['p'] = 'r';
    mapping['q'] = 'z';
    mapping['r'] = 't';
    mapping['s'] = 'n';
    mapping['t'] = 'w';
    mapping['u'] = 'j';
    mapping['v'] = 'p';
    mapping['w'] = 'f';
    mapping['x'] = 'm';
    mapping['y'] = 'a';
    mapping['z'] = 'q';
    mapping[' '] = ' ';
    mapping['\t'] = '\t';
    mapping['\n'] = '\n';
    mapping['_'] = '_';
    mapping['-'] = '-';
    mapping['.'] = '.';
}


int main()
{
    int n;
    
    initMapping();
    
    cin >> n;
    
    int msgLength;
    
    cin.getline(buffer, BUFFER_SIZE);
    
    for (int i = 1; i <= n; ++i) {
        cin.getline(buffer, BUFFER_SIZE);
        cout << "Case #" << i << ": ";
        for (int j = 0; buffer[j] != '\0'; ++j ) {
            cout << mapping[buffer[j]];
        }
        cout << endl;
    }
    return 0;
}