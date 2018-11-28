#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int mp[26];
int main()
{


    mp[0] = 'y';
    mp[1] = 'h';
    mp[2] = 'e';
    mp[3] = 's';
    mp[4] = 'o';
    mp[5] = 'c';
    mp[6] = 'v';
    mp[7] = 'x';
    mp[8] = 'd';
    mp[9] = 'u';
    mp[10] = 'i';
    mp[11] = 'g';
    mp[12] = 'l';
    mp[13] = 'b';
    mp[14] = 'k';
    mp['p'-'a'] = 'r';
    mp['q'-'a'] = 'z';
    mp['r'-'a'] = 't';
    mp['s'-'a'] = 'n';
    mp['t'-'a'] = 'w';
    mp['u'-'a'] = 'j';
    mp['v'-'a'] = 'p';
    mp['w'-'a'] = 'f';
    mp['x'-'a'] = 'm';
    mp['y'-'a'] = 'a';
    mp['z'-'a'] = 'q';
    int t;
    scanf("%d" , &t );
    char c;
    c = getchar();
    char input[110] , output[110];
    int i;
    int count = 0;
    while( t )
    {
           t--;
           count++;
           i = 0;
           fflush( stdin );


           while( ( input[i] = getchar() ) != '\n' )
           {
                  if( input[i] == ' ' )
                             c = input[i];
                  else {
                       c = input[i];
                       c = c - 'a';
                      c = mp[c];
                  }
                  output[i] = c;
                  i++;
           }
           output[i] = '\0';

           printf("Case #%d: %s\n" , count , output );
    }


    return 0;
}
