#include <iostream>
#include <string>
using namespace std;
char dict[26];

void dict_open()
{
    freopen("dict.txt","r",stdin);
    char a ,b;
    while(cin >> a >> b) dict[a] = b; 
}

int main()
{
    dict_open();
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    char str[100];
    gets(str);
    puts(str);
    int n;
    sscanf(str, "%d", &n);
    for(int _n=1; _n<=n; _n++)
    {
        gets(str);
        int len = strlen(str);
        cout << "Case #" << _n << ": ";
        for(int i=0; i<len; i++)
        {
            if(str[i] == ' ') putchar(' ');
            else cout << dict[str[i]];
        }
        puts("");
    }
}
