#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    char *s[] ={
         "ejp mysljylc kd kxveddknmc re jsicpdrysi",
         "our language is impossible to understand",
         "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
         "there are twenty six factorial possibilities",
         "de kr kd eoya kw aej tysr re ujdr lkgc jv",
         "so it is okay if you want to just give up"
         };
    
    int mapping[27] = {0};
    
    for(int i=0;i<3;i++)
    {
        char *s1 = s[2*i], *s2 = s[2*i+1];        
        for(int j=0;j<strlen(s1);j++)
        {            
            if(s1[j] == ' ') continue;
            mapping[s1[j]-'a'] = s2[j]-'a';
        }
    }
    
    mapping['q'-'a'] = 'z'-'a';
    mapping['z'-'a'] = 'q'-'a';
    
    #if 0
    for(int i=0;i<26;i++)
        //cout << (char) ('a' + mapping[i]);
        cout << i << " " << (char) ('a'+i) << " <- " << (char) ('a' + mapping[i]) << endl;
    
    system("PAUSE");    
    return 0;
    #endif
    
    char *fname;
    int T;
    char S[110];
    
    if(argc > 1) fname = argv[1];
    else fname = "A-small-attempt1.in";
        
    ifstream in(fname);
    
    in.getline(S, 110);
    T = atoi(S);    
    
    for(int i=1;i<=T;i++)
    {
       in.getline(S, 110);
       for(char *t=S;*t;t++)
           *t = (*t == ' ') ? ' ' : (mapping[*t-'a'] + 'a');
       cout << "Case #" << i << ": ";
       cout << S << endl;
    }
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
