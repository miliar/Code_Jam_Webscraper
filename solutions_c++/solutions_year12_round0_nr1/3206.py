#include <cstdio>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <sstream>
#include <vector>

using namespace std; 

main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	int i,t;
	char a;
	
	cin >> t;
	a=getchar();
	
	for (i=1;i<=t;++i)
	{
        printf("Case #%d: ",i);
        while (a=getchar())
        {
            if (a==' ') cout << ' ';
            if (a=='y') cout << 'a';
            if (a=='n') cout << 'b';
            if (a=='f') cout << 'c';
            if (a=='i') cout << 'd';
            if (a=='c') cout << 'e';
            if (a=='w') cout << 'f';
            if (a=='l') cout << 'g';
            if (a=='b') cout << 'h';
            if (a=='k') cout << 'i';
            if (a=='u') cout << 'j';
            if (a=='o') cout << 'k';
            if (a=='m') cout << 'l';
            if (a=='x') cout << 'm';
            if (a=='s') cout << 'n';
            if (a=='e') cout << 'o';
            if (a=='v') cout << 'p';
            if (a=='z') cout << 'q';
            if (a=='p') cout << 'r';
            if (a=='d') cout << 's';
            if (a=='r') cout << 't';
            if (a=='j') cout << 'u';
            if (a=='g') cout << 'v';
            if (a=='t') cout << 'w';
            if (a=='h') cout << 'x';
            if (a=='a') cout << 'y';
            if (a=='q') cout << 'z';
            if (a=='\n') 
            {
                cout << '\n';
                break;
            }
        }
    }
}
