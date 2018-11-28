#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define rei(i,a,b) for(int i=a;i<b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define pb(a,x) a.push_back(x)
#define all(a) a.begin(),a.end()
#define srt(a) sort(all(a))
#define rev(a) reverse(all(a))

int main(){
    int test;
    scanf("%d",&test);
    rei(i,0,test){
        map<string,string> combine;
        int totCombine=0;
        scanf("%d",&totCombine);
        rei(j,0,totCombine){
            string cmbn;
            cin>>cmbn;
            string pr=cmbn.substr(0,2);
            string form="";form+=cmbn[2];
            combine[pr]=form;rev(pr);
            combine[pr]=form;
        }
        int totOppose=0;
        bool oppose[255][255];
        mem(oppose,0);
        scanf("%d",&totOppose);
        rei(j,0,totOppose){
            string opps;
            cin>>opps;
            oppose[(int)opps[0]][(int)opps[1]]=true;
            oppose[(int)opps[1]][(int)opps[0]]=true;
        }
        int sz=0;
        scanf("%d",&sz);
        string input;
        cin>>input;
        string ret="";
        rei(j,0,sz){
            if(ret==""){
                ret+=input[j];
            }else{
                ret+=input[j];
                string sub=ret.substr(ret.size()-2,2);
                while(combine.count(sub)!=0){
                    sub=combine[sub];
                    ret=ret.substr(0,ret.size()-2);
                    ret+=sub;
                    if(ret.size()==1)
                        break;
                    sub=ret.substr(ret.size()-2,2);
                }
                rei(j,0,ret.size()){
                    if(oppose[(int)ret[j]][(int)ret[ret.size()-1]])
                        ret="";
                }
            }
        }
        printf("Case #%d: [",i+1);
        rei(j,0,ret.size()){
            if(j!=ret.size()-1){
                printf("%c, ",ret[j]);
            }else{
                printf("%c]\n",ret[j]);
            }
        }
        if(ret.size()==0) printf("]\n");
    }
    return 0;
}
