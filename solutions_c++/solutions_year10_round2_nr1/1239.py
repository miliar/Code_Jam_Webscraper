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
map<string,int> M;

vector<string> dict,path;

void parse(string &s,int idx,vector<string> &VS){
     if(s.size()<=0) return;
     if(idx>=s.size()) return;
     if(s[idx]=='/') { parse(s,idx+1,VS); return; }
     size_t found=s.find("/",idx);
     if(found==string::npos) {  VS.push_back(s.substr(idx)); return; }
     else VS.push_back(s.substr(idx,found-idx)),parse(s,found,VS);
 }

 int get(string &x){
        int i,j;
        int c=0;
        for(i=0;i<x.size();i++) if(x[i]=='/') c++;
        int ans=c;
        for(i=0;i<dict.size();i++){
            string &t=dict[i];
            for(j=0;j<t.size() and j<x.size();j++){
                    if(x[j]!=t[j]) break;
            }
            int no=1;
            if(j==t.size() and j==x.size()){
                no=0;
                return 0;
            }
            if(j==x.size()){
                if(j<t.size() and t[j]=='/') no=0;
            }
            if(j==t.size() ){
                    if(j<x.size() and x[j]=='/') no=0;
            }
            for(;j<x.size();j++) if(x[j]=='/') no++;
            ans=min(ans,no);
        }
        return ans;
 }
                
int main(int argc,char **argv){
    int tc,NC,ans=0;
    cin >> NC;
        for(tc=1;tc<=NC;tc++){
            ans=0;
            M.clear();
            dict.clear(),path.clear();
            int N,K;
            cin >> N>>K;
            int i;
            for(i=0;i< N;i++){
                    string x;
                    cin >> x;
                    if(x=="/") continue;
                    dict.push_back(x);
            }
            for(i=0;i<K;i++){
                    string x;
                    cin >> x;
                    if(x=="/") continue;
                    path.push_back(x);
                    int k=get(x);
                    ans+=k;
  //                  printf("%d,",k);
                    dict.push_back(x);
            }


            /*

        vector<vector<string> > D;
        vector<vector<string> > Q;
            int j,val=1;
            for(i=0;i<N;i++){
                    string s=dict[i];
                    vector<string> VS;
                    parse(s,0,VS);
                    D.push_back(VS);
                    for(j=0;j<VS.size();j++)
                        if(M.count(VS[j])==0) M[VS[j]]=val++;

            }
            for(i=0;i<K;i++){
                    string s=path[i];
                    vector<string> VS;
                    parse(s,0,VS);
                    Q.push_back(VS);
                    for(j=0;j<VS.size();j++)
                        if(M.count(VS[j])==0) M[VS[j]]=val++;
            }
            */


            
         
            printf("Case #%d: %d\n",tc,ans);
        }
    return 0;
}
