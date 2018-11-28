#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int n = 0, s, it = 0;
    string str;
    getline(cin,str,'\n');
    while(str[it]!=0){n=(n*10)+str[it++]-'0';}
    
    F(wer,n){
        getline(cin,str,'\n');
        vector<pair<int,int> > v(str.S,pair<int,int>(-1,0));
        string wel = "welcome to code jam";
        F(i,wel.S){
            F(j,str.S){
                if(wel[i] == str[j]){
                    if(i == 0){
                        v[j] = make_pair(0,1);//posi, cuanto
                    }
                    else{
                        s = 0;
                        F(k,j){
                            if(v[k].first+1 == i){
                                s += v[k].second;
                            }
                        }
                        s = s%10000;
                        v[j] = make_pair(i,s);
                    }
                }
            }
        }
        s = 0;
        F(j,str.S){
            if(wel[v[j].first] == 'm'){
                s += v[j].second;
            }
            s = s%10000;
        }
        s = s%10000;
        printf("Case #%d: %04d\n",wer+1,s);
    }
    fclose(stdout);
    //system("pause");
    return 0;
}
