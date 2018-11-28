#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <map>
using namespace std;

#define SORT(v) sort(v.begin(),v.end());
#define REVERSE(v) reverse(v.begin(),v.end());

int main(void)
{
    int I,J,K,T,C,D,N;
    char ch1,ch2,ch3;
    string str,input,tmpstr,tmpstr1,res;
    map<string,char> comb;
    vector<string> opp;

    freopen ("input.in","r",stdin);
    freopen ("output.out","w",stdout);

    cin>>T;
    for(I = 1; I <= T; I = I + 1)
    {
        opp.clear();
        comb.clear();
        res.clear();

        cin>>C;
        for(J = 1; J <= C; J = J + 1)
        {
            cin>>ch1>>ch2;
            str.clear();    str.push_back(ch1); str.push_back(ch2);
            cin>>ch3;
            comb[str]=ch3;
            str.clear();    str.push_back(ch2); str.push_back(ch1);
            comb[str]=ch3;
        }

        cin>>D;
        for(J = 1; J <= D; J = J + 1)
        {
            cin>>ch1>>ch2;
            str.clear();    str.push_back(ch1); str.push_back(ch2);
            opp.push_back(str);
            str.clear();    str.push_back(ch2); str.push_back(ch1);
            opp.push_back(str);
        }

        cin>>N>>input;
        for(J = 0; J < input.size(); J = J + 1)
        {
            tmpstr.clear();
            tmpstr.push_back(input[J]);
            tmpstr.push_back(input[J+1]);

            if(comb[tmpstr]!=NULL)
            {
                res.push_back(comb[tmpstr]);
                J = J + 1;
            }
            else
            {
                int flag = 0;
                for(K = J + 1; K < input.size(); K = K + 1)
                {
                    tmpstr.clear();
                    tmpstr.push_back(input[J]);
                    tmpstr.push_back(input[K]);
                    tmpstr1.clear();
                    tmpstr1.push_back(input[K - 1]);
                    tmpstr1.push_back(input[K]);

                    if(find(opp.begin(),opp.end(),tmpstr)!=opp.end() && comb[tmpstr1]==NULL)
                    {
                        J = K;
                        flag = 1;
                        res.clear();
                        break;
                    }
                }
                if(flag == 0)
                    res.push_back(input[J]);
            }
        }

        cout<<"Case #"<<I<<": [";
        if(res.size() > 0)
        {
            for(J = 0; J < res.size()-1; J = J + 1)
                cout<<res[J]<<", ";
        }
        if(res.size() > 0)
            cout<<res[res.size() - 1];
        cout<<"]"<<endl;
    }

    return 0;
}