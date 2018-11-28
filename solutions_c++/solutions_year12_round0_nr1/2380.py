#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int main() {
	map <char, char> table;
    
    table.insert(make_pair('a', 'y'));
    table.insert(make_pair('b', 'h'));
    table.insert(make_pair('c', 'e'));
    table.insert(make_pair('d', 's'));
    table.insert(make_pair('e', 'o'));
    table.insert(make_pair('f', 'c'));
    table.insert(make_pair('g', 'v'));
    table.insert(make_pair('h', 'x'));
    table.insert(make_pair('i', 'd'));
    table.insert(make_pair('j', 'u'));
    table.insert(make_pair('k', 'i'));
    table.insert(make_pair('l', 'g'));
    table.insert(make_pair('m', 'l'));
    table.insert(make_pair('n', 'b'));
    table.insert(make_pair('o', 'k'));
    table.insert(make_pair('p', 'r'));
    table.insert(make_pair('q', 'z'));
    table.insert(make_pair('r', 't'));
    table.insert(make_pair('s', 'n'));
    table.insert(make_pair('t', 'w'));
    table.insert(make_pair('u', 'j'));
    table.insert(make_pair('v', 'p'));
    table.insert(make_pair('w', 'f'));
    table.insert(make_pair('x', 'm'));
    table.insert(make_pair('y', 'a'));
    table.insert(make_pair('z', 'q'));
    table.insert(make_pair(' ', ' '));
	
    int t, T = 1;
    char line[1000];
    
    scanf("%d ", &t);
    while (t--) {
        printf("Case #%d: ", T++);
        scanf("%[^\n] ", line);
        for (int i=0; line[i]; ++i) {
            if (table.find(line[i]) == table.end()) {
                printf("*");
            }
            else {
                putchar(table[line[i]]);
            }
        }
        puts("");
    }
    
	return 0;
}
