#include <iostream>
#include <string>
#include <list>
//#include <algorithm>
#include <stdlib.h>

using namespace std;

inline int c2i(char c) { return c-'A'+1; }

int main()
{
    int T;
    cin>>T;
    for(int t=0; t<T; ++t)
    {
        int C;
        cin>>C;
        char cm[32][32]={};
        int om[32]={};

        for(int c=0;c<C;++c)
        {
            string s;
            cin>>s;
            cm[c2i(s[0])][c2i(s[1])]=s[2];
            cm[c2i(s[1])][c2i(s[0])]=s[2];
        }
        int D;
        cin>>D;
        for(int d=0;d<D;++d)
        {
            string s;
            cin>>s;
            om[c2i(s[0])] |=1<<c2i(s[1]);
            om[c2i(s[1])] |=1<<c2i(s[0]);
        }

        list<char> rl;
        int N;
        cin>>N;
        int o =0;
        
        for(int n=0;n<N;++n)
        {
            char b;
            cin>>b;
            if (!rl.empty())
            {
                int nb=cm[c2i(rl.back())][c2i(b)];
                if (nb!=0)
                {
                    rl.back()=nb;
                    continue;
                }
                o |= om[c2i(rl.back())];
                if (o & (1<<c2i(b)))
                {
                    o=0;
                    rl.clear();
                    continue;
                } 
                
            }  
            //
            rl.push_back(b);
        }


        cout<<"Case #"<<(t+1)<<": [";
        for(list<char>::iterator it=rl.begin(); it!=rl.end(); ++it)
        {
            if (it!=rl.begin()) cout<<", ";
            cout<<*it;    
        }
        cout<<"]"<<endl;
    }
    return 0;
}
