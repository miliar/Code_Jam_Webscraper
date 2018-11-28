# include <iostream>
# include <fstream>
# include <cstdio>

using namespace std;

char subs[256]={0};

int main()
{
 freopen("A-small-attempt1.in", "r", stdin);   
 freopen("output.txt", "w", stdout);
 
 subs['a'] = 'y';
 subs['b'] = 'h';
 subs['c'] = 'e';
 subs['d'] = 's';
 subs['e'] = 'o';
 subs['f'] = 'c';
 subs['g'] = 'v';
 subs['h'] = 'x';
 subs['i'] = 'd';
 subs['j'] = 'u';
 subs['k'] = 'i';
 subs['l'] = 'g';
 subs['m'] = 'l';
 subs['n'] = 'b';
 subs['o'] = 'k';
 subs['p'] = 'r';
 subs['q'] = 'z';
 subs['r'] = 't';
 subs['s'] = 'n';
 subs['t'] = 'w';
 subs['u'] = 'j';
 subs['v'] = 'p';
 subs['w'] = 'f';
 subs['x'] = 'm';
 subs['y'] = 'a';
 subs['z'] = 'q';
 
 int T, cas = 0;
 string input;
 
 cin>>T;
 getline(cin, input);
 
 while(T--){
                   getline(cin, input);
                   
                   cout<<"Case #"<<++cas<<": ";
                   for(int i = 0; i < input.size(); ++i){
                           if (input[i] >= 'a' && input[i] <= 'z') {
                                        cout<<subs[input[i]];
                           }    
                           else{
                                cout<<input[i];
                                }
                   }
                   cout<<endl;
            }
 
    return 0;
}
