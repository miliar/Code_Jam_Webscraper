#include<iostream>
#include<string>
#include<map>
#include<queue>
#include<deque>
#include<stack>
#include<vector>
#include<set>
#include<algorithm>
#include<utility>
#include<bitset>
#include<sstream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cctype>

#define FOR(a,b) for(int a=0;a<b;a++)
#define FORR(a,b) for(int a=b-1;a>=0;a--)
#define INR(a,b) (0<=a && a<b)
#define CLEAR(a,b) memset(a,b,sizeof a)

#define PB push_back
#define LLI long long
#define PII pair<int,int>
#define MKP make_pair
#define VI vector<int>
#define VS vector<string>
#define VVI vector< vector<int> >
#define VVS vector< vector< string > >
#define IT iterator

#define MAX 101

using namespace std;

int main(){
    int t;
    cin >> t;
    FOR(t_n,t){
        
        vector< map<char,char> > comb(92,map<char,char>());
        vector< set<char> > opos(92,set<char>());

        int cn;
        cin >> cn;
        while(cn--){
            string str;
            cin >> str;
            comb[str[0]][str[1]]=str[2];
            comb[str[1]][str[0]]=str[2];
        }
        int on;
        cin >> on;
        while(on--){
            string str;
            cin >> str;
            opos[str[0]].insert(str[1]);
            opos[str[1]].insert(str[0]);
        }
    
        int n;
        cin >> n;
        string elems;
        cin >> elems;

        vector<char> list;

        for(int i=0;i<n;i++){
            char next = elems[i];

            if(list.size()==0){
                list.PB(next);
                continue;
            }
            char top = list[list.size()-1];

            if( comb[top].count(next) > 0 ){
                list[list.size()-1] = comb[top][next];
            }
            else if(opos[next].size()>0){
                bool cleared = false;
                FOR(j,list.size()){
                    if( opos[next].count(list[j]) > 0){
                        list.clear();
                        cleared = true;
                        break;
                    }
                }

                if(!cleared){
                    list.PB(next);
                }
            } else {
                list.PB(next);
            }
        }
        
        cout << "Case #" << t_n+1 << ": [";
        FOR(i,list.size()){
            if(i!=0)
                cout << ", ";
            
            cout << list[i];
        }
        cout << "]"<<endl;
    }
    return 0;
}
