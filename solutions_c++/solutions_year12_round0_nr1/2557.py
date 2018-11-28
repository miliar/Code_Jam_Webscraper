//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <utility>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#define pi 2.0*acos(0.0)
#define pb push_back
#define MAX 2147483647
#define MIN -2147483647
#define rep(i,n) for(int i(0),_n(n);i<_n;i++)
#define reps(i,s,n) for(int i(s),_n(n);i<_n;i++)
#define mp make_pair


typedef long long ll;
typedef vector<int> VI;
typedef set<int>SI;
typedef pair<int,int>PAR;
typedef vector<PAR>VP;
typedef map<string,int>MSI;



int main()
{
#ifndef ONLINE_JUDGE
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif
    string master="ynficwlbkuomxsevzpdrjgthaq";
    int kas;
    char inps[1009];
    cin>>kas;
    gets(inps);
    rep(cas,kas){
        printf("Case #%d: ",cas+1);
        string str="",inp;
        gets(inps);
        inp=inps;
        rep(i,inp.size()){
            if(isalpha(inp[i])){
                rep(j,master.size()){
                    if(master[j]==inp[i])
                    cout<<(char)(j+'a');
                }
            }
            else cout<<inp[i];
        }
        puts("");

        //cout<<str<<endl;
    }

return 0;
}
