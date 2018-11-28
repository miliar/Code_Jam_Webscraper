#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int mp[26];
int main()
{


    mp['a'-'a'] = 'y';
    mp['b'-'a'] = 'h';
    mp['c'-'a'] = 'e';
    mp['d'-'a'] = 's';
    mp['e'-'a'] = 'o';
    mp['f'-'a'] = 'c';
    mp['g'-'a'] = 'v';
    mp['h'-'a'] = 'x';
    mp['i'-'a'] = 'd';
    mp['j'-'a'] = 'u';
    mp['k'-'a'] = 'i';
    mp['l'-'a'] = 'g';
    mp['m'-'a'] = 'l';
    mp['n'-'a'] = 'b';
    mp['o'-'a'] = 'k';
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
    char input[110] , output[110];
    int i;
    char c;
    int count = 0;
	c = getchar();
    while( t )
    {
           t--;
           count++;
           i = 0;

	
		

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

