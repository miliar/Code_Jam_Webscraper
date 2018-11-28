#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <stack>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
double EPS=1e-10;
double EQ(double a,double b){
    return abs(a-b)<EPS;
}
void fast_stream(){
  std::ios_base::sync_with_stdio(0);
}

//ifstream ifs("insmallA.txt");
//ofstream ofs("outsmallA.txt");
//#define cin ifs
//#define cout ofs

// ˆá‚¤Ží—Þ‚Ì•¶Žš‚ÍAŒÂ‚µ‚©‚È‚¢
// ‚»‚ê‚¼‚ê‚Ì•¶Žš‚ÌÅ“K‚©‚¢‚ðl‚¦‚Ä‚¨‚¢‚ÄA
// ‚»‚ê‚ðŒó•â‚É‚·‚é

int T;
double per[100001];
void solve(){
    cin>>T;
    for(int q=0;q<T;q++){
        int A,B;
        cin>>A>>B;
        for(int i=0;i<A;i++)cin>>per[i];
        double res=1000000000;
        // keep typing
        {
            double prvPer=1;
            double cost=0;
            for(int i=0;i<=A;i++){
                if(i==A)cost+=(B-A+1)*prvPer;
                else{
                    double p=prvPer*(1-per[i]);
                    cost+=(B-A+1+B+1)*p;
                    prvPer*=per[i];
                }
            }
            res=min(res,cost);
        }
        // right away
        res=min(res,2.0+B);
        // backspace
        {
            double prvPer=1;
            double sumPer=0;
            double cost=0;
            double cur=0;
            for(int i=0;i<A;i++){
                if(i==0){
                    res=min(res,(double)(A-i)+(B+1));
                    sumPer+=(1-per[i]);
                }
                else{
                    double p=prvPer*(1-per[i]);
                    double tmp=(A-i)+(1-sumPer)*(B-i+1)+(sumPer)*(B-i+1+B+1);
                    res=min(res,tmp);
                    sumPer+=p;
                }
                prvPer*=per[i];
            }
        }
        printf("Case #%d: %.10f\n",q+1,res);
    }
}
