#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cmath>
#include<map>
#include<sstream>
#include<cstring>
#include<numeric>
#include<stack>
#include<queue>
#include<cstdlib>
#include<ctype.h>
#include<algorithm>
using namespace std;
#define min(a,b) a>b?b:a
#define max(a,b) a>b?a:b
#define PI 2*acos(0.0)
#define INF 1<<30
#define PB(a,b) a.push_back(b)
#define ALL(a) (a.begin(),a.end())
#define clear(a) a.erase(a.begin(),a.end())
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long LL;

int main(){
    ifstream I;
    ofstream P;
    I.open("D:\\Codings\\B-large.in");
    P.open("D:\\Codings\\test.out");
    int C;I>>C;
    for(int ca=1;ca<=C;ca++){
        int n,k,b,t;
        I>>n>>k>>b>>t;
        vector<int>x(n),v(n);
        for(int i=0;i<n;i++)I>>x[i];
        for(int i=0;i<n;i++)I>>v[i];
        int fix=0,start=n-1,s=0;bool possible=1;
        while(fix<k){
            bool flag=0;int end;
            for(int i=start;i>=0;i--){
                LL time;time=t*v[i]+x[i];
                if(time>=b){end=i;flag=1;break;}
            }
            if(flag){
                vector<int>t1,t2;
                for(int j=0;j<end;j++){t1.push_back(x[j]);t2.push_back(v[j]);}
                for(int j=end+1;j<=start;j++){s++;t1.push_back(x[j]);t2.push_back(v[j]);}
                t1.push_back(x[end]);t2.push_back(v[end]);
                for(int j=start+1;j<n;j++){t1.push_back(x[j]);t2.push_back(v[j]);}
                x=t1;v=t2;
                start--;fix++;
            }
            else {possible =0;break;}
        }
        P<<"Case #"<<ca<<": ";
        if(possible)P<<s<<endl;
        else P<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}

