#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cctype>
using namespace std;
const int MAXN = 5010;
typedef vector<string> VS;
typedef vector<int> Tok;

Tok my_tokens[MAXN];
VS words;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int L,D,N;
    while(cin>>L>>D>>N) {
        words.clear();
        for(int i=0;i<N;i++) my_tokens[i].clear();
        for(int i=0;i<D;i++) {
            string str;
            cin>>str;
            words.push_back(str);
        }

        for(int i=0;i<N;i++) {


            string str;
            cin>>str;
            int isp=0,state=0;
            for(int j=0;j<str.size();j++) {
                char ch=str[j];
                if(isp) {
                    if(ch==')'){
                        my_tokens[i].push_back(state);
                        state=0;
                        isp=0;
                    }
                    else {
                        state|=(1<<(ch-'a'));
                    }
                }
                else {
                    if(ch=='(') isp=1;
                    else {
                        my_tokens[i].push_back(1<<(ch-'a'));
                    }
                }
            }


            Tok curToken = my_tokens[i];
            int ret=0;
            for(int j=0;j<D;j++) {
                int ok=0;
                for(int k=0;k<L;k++) {
                    if(curToken[k]&(1<<(words[j][k]-'a'))) {
                        ok++;
                    }

                }
                if(ok==L) ret++;
            }

            cout<<"Case #"<<i+1<<": "<<ret<<endl;
        }




    }
    return 0;
}


