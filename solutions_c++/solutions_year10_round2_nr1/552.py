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
    I.open("D:\\Codings\\A-large.in");
    P.open("D:\\Codings\\test.out");
    int t;I>>t;
    for(int ca=1;ca<=t;ca++){
        int m,n;vector<string>dic;
        I>>m>>n;
        for(int i=0;i<m;i++){
            string s;
            I>>s;
            dic.push_back(s);
        }int temp=dic.size();
        for(int i=0;i<n;i++){
            string s,t;t='/';
            I>>s;
            for(int j=0;j<s.size();j++){
                if(isdigit(s[j])||isalpha(s[j]))t+=s[j];
                if((j==s.size()-1&&t.size()>1)||(s[j]=='/'&&t.size()>1)){
                    bool f=0;
                    for(int k=0;k<dic.size();k++){
                        if(dic[k]==t){f=1;break;}
                    }
                    if(!f)dic.push_back(t);
                    t+='/';
                }
            }
        }
        P<<"Case #"<<ca<<": "<<dic.size()-temp<<endl;
    }
    return 0;
}
