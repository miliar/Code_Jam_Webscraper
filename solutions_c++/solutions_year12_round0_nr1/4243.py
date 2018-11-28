#include<iostream>

using namespace std;

char a[30];
void init()
{
     a['a' - 'a'] = 'y';
     a['b' - 'a'] = 'h';
     a['c' - 'a'] = 'e';
     a['d' - 'a'] = 's';
     a['e' - 'a'] = 'o';
     a['f' - 'a'] = 'c';
     a['g' - 'a'] = 'v';
     a['h' - 'a'] = 'x';
     a['i' - 'a'] = 'd';
     a['j' - 'a'] = 'u';
     a['k' - 'a'] = 'i';
     a['l' - 'a'] = 'g';
     a['m' - 'a'] = 'l';
     a['n' - 'a'] = 'b';
     a['o' - 'a'] = 'k';
     a['p' - 'a'] = 'r';
     a['q' - 'a'] = 'z';//
     a['r' - 'a'] = 't';
     a['s' - 'a'] = 'n';
     a['t' - 'a'] = 'w';
     a['u' - 'a'] = 'j';//
     a['v' - 'a'] = 'p';
     a['w' - 'a'] = 'f';
     a['x' - 'a'] = 'm';
     a['y' - 'a'] = 'a';
     a['z' - 'a'] = 'q';//
}

int main()
{
    int t;
    init();
    char q[1<<10];
    cin>>t;
    gets(q);
    for (int i=1; i<=t;++i)
    {
          gets(q);
          //cout<<q<<endl;
          cout<<"Case #"<<i<<": ";
          for ( int j=0; q[j]; ++j)
          {
              //ut<<q[j];
              //continue;
              if(q[j] == ' ')
                      cout<<q[j];
              else
                      cout<<(a[int(q[j] - 'a')]);
          }
          cout<<endl;
    }
    return 0;
}
