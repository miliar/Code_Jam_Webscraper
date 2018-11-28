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

bool prime[10001];
vector<long long> nums = vector<long long>(10001);

int main(){
    int t;

    cin >> t;

    CLEAR(prime,true);

    for(int i=2;i<sqrt(10000)+1;i++){
        if(prime[i])
            for(int j=i*i;j<=10000;j+=i)
                prime[j]=false;
    }

    FOR(t_n,t){

        long long tot = 1, l, h;
        int n;
        cin >> n >> l >> h;


        FOR(i,n)
            cin >> nums[i];

        bool good = false;

        long long x;
        for(x = l; x <= h; x++){
            good = true;
            FOR(i,n){
                if( nums[i]%x!=0 && x%nums[i]!=0 ){
                    good = false;
                    break;
                }
            }
            if(good){
                break;
            }
        }


        cout << "Case #"<<t_n+1<<": ";
        if(good){
            cout<<x<<endl;
        }
        else
            cout << "NO" << endl;
    }
    return 0;
}
