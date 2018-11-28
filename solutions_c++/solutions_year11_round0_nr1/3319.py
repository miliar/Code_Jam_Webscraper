#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
  
using namespace std; 
  
typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long LL; 
typedef pair<int,int> PII; 
typedef pair<string,string> PSS; 
 
#define pb push_back 
#define all(a) a.begin(), a.end() 
 
#define ss stringstream 
 
#define F(a,b,i) for(int i=a; i<b; ++i)   
#define FE(it,s) for (__typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)  
#define R(a,b,i) for(int i=b-1; i>=a; --i) 
  
/*  debug  */ 
#define D(x) cout << #x << " = "<< x <<endl; 
#define PV(label,x) cout<<label<<"=[ "; FE(it,x) cout<<*it<<" "; cout<<"]"<<endl; 
#define PM(label,x) cout<<label<<endl; FE(it,x){cout<<label<<"["<<it->first<<"]="<<it->second<<endl;} 

int main()
{
    int t,n,p;
    char r;
    cin>>t;
    F(0,t,nc){
        cin>>n;
        int res=0;
        int pa=1,pb=1;
        int ac=0;
        char ra='A';
        F(0,n,i){
            cin>>r>>p;
            int d;
            if(r=='O'){
                d=abs(p-pa);
            }
            else{
                d=abs(p-pb);
            }
            //printf("d=%d ra=%c ac=%d res=%d\n",d, ra, ac,res);
            if(ra!=r){
                if(d>ac){
                    res+=(d-ac)+1;
                    ac=(d-ac)+1;
                }
                else{
                    res++;
                    ac=1;
                }
                //ac=d+1;
            }
            else{
                ac+=(d+1);
                res+=(d+1);
            }
            if(r=='O'){
                pa=p;
            }
            else{
                pb=p;
            }
            
            ra=r;
        }
        cout<<"Case #"<<nc+1<<": "<<res<<endl;
    }
    return 0;
}
