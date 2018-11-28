/* {{{ */
#include<cstdio>
#include<climits>
#include<cmath>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
#include<list>
#include<sstream>
#include<set>
#include<queue>
#include<vector>
#include<string>
#include<fstream>
#include<istream>
#include<iostream>
#include<bitset>
using namespace std;
/* }}}  */

typedef long long ll;
typedef unsigned long long ull;
const int MAX=200;
char str[MAX];

int main(int argc,char **argv){

    int tc,no;
    scanf(" %d",&no);

    for(tc=1;tc<=no;tc++)
    {
            int C;
           scanf(" %d ",&C);
           set<pair<char,char> > SC;
           map< pair<char,char> , char> MC;
           int i;
           for(i=0;i<C;i++){
                char s[4];
                scanf(" %s",s);
                SC.insert((make_pair(s[0],s[1])) );
                SC.insert((make_pair(s[1],s[0])) );
                MC[make_pair(s[0],s[1])]=s[2];
                MC[make_pair(s[1],s[0])]=s[2];
           }
           int D;
           scanf(" %d",&D);
           set<pair<char,char> > SD;

           for(i=0;i<D;i++){
                char s[4];
                scanf(" %s",s);
                SD.insert(make_pair(s[0],s[1]));
                SD.insert(make_pair(s[1],s[0]));
           }
           int n;
           scanf(" %d",&n);
           scanf(" %s",str);
            string ans;
            for(i=0;i<n;i++)
            {
                 ans+=str[i];
doagain:
                 if(ans.size()>1)
                 {
                        int sz=ans.size();
                        char  ch1=ans[sz-1],ch2=ans[sz-2];
                        pair<char,char> p(ch1,ch2);
                        if(SC.count(p)){
                           ans.erase(sz-2,2);
                           char ch=MC[p];
                           ans+=ch;
                           goto doagain;
                        }
                        set<char> SANS(ans.begin(),ans.end());
                        bool doclear=false;
                        set<pair<char,char> >::iterator it;
                        for(it=SD.begin();it!=SD.end();it++){
                                char ch1=it->first;
                                char ch2=it->second;
                                if(SANS.count(ch1) and SANS.count(ch2)) { doclear=true;break; }

                        }

                        if(doclear){
                            ans.clear();
                        }
                        
                 }
            }
            
            printf("Case #%d: [",tc);
            for(i=0;i<ans.size();i++){
                if(i and i<ans.size()) printf(", ");
                printf("%c",ans[i]);
            }
            printf("]\n");



    }

    return 0;
}
