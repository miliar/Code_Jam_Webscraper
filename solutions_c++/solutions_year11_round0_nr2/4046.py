#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int T,C,D,N;
    int i,j,kase=1;
    string com[50],op[50],es;
    map<pair<char,char>,char> cm;
    map<char,char> ds;

    freopen("B-small-attempt1.in","r",stdin);
    freopen("B_small_1.out","w",stdout);

    cin >> T;

    while(T--)
    {
        cin >> C;

        cm.clear();
        ds.clear();

        for(i=0;i<C;i++)
        {
            cin >> com[i];
            cm[make_pair((char)com[i][0],(char)com[i][1])]=(char)com[i][2];
            cm[make_pair((char)com[i][1],(char)com[i][0])]=(char)com[i][2];
        }

        cin >> D;

        for(i=0;i<D;i++)
        {
            cin >> op[i];
            ds[(char)op[i][0]]=(char)op[i][1];
            ds[(char)op[i][1]]=(char)op[i][0];
        }

        cin >> N;
        cin >> es;

        int b=0;
        for(i=1;i<N;i++)
        {
            if((i-1>=b) && (cm[make_pair((char)es[i],(char)es[i-1])]!='\0'))
            {
                es[i]=cm[make_pair((char)es[i],(char)es[i-1])];
                es[i-1]='\0';

                if(b==i-1) b++;
            }
            else
            {
                for(j=i-1;j>=b;j--)
                    if(es[j]!='\0' && ds[(char)es[i]]==(char)es[j])
                    {
                        b=i+1;
                        break;
                    }
            }
        }

        cout <<"Case #"<< kase++ <<": [";

        if(b<N) cout << es[b] ;
        for(i=b+1;i<N;i++)
            if(es[i]!='\0')
                cout <<", "<< es[i];

        cout <<"]"<< endl;
    }

    return 0;
}
