#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;
             
char g[30] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
    int n;
    scanf("%d\n", &n);
    for(int i = 1; i <= n; i++)
    {
        char s[105], ch;
		vector <string> res;
        gets(s);
//		scanf("%c", &ch);
        string a = s, b;
        istringstream cn(a);
        while(cn >> b)
        {
            for(int j = 0; j < b.size(); j++)
                b[j] = g[b[j] - 'a'];
            res.push_back(b);
        }
		printf("Case #%d:", i);
		for(int j = 0; j < res.size(); j++)
			cout << " " << res[j];
        printf("\n");
		res.clear();
    }
//	while(1);
    return 0;
}