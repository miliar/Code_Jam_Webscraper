//Bismillahir Rahmanir Rahim

#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <functional>
#include <stack>
#include <queue>
#include <deque>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>

#define si  100000
#define pb push_back
#define popb pop_back
#define pf push_front
#define popf pop_front
#define mp make_pair
#define fo(i,n) for(int i=0;i<(n);i++)
#define sorta(a) sort(a.begin(),a.end())
#define sortab(a,n) sort(a,a+n)
#define sz size()
#define eps 0.000000000001
#define pi 2.0*acos(0.0)

using namespace std;

typedef long long ll;
typedef vector<int>VI;
typedef vector<string>VS;
typedef set<int>SI;
typedef pair<int,int>par;
typedef vector<par>VP;

bool eq(double a,double b)
{return !(fabs(a-b)>eps);}



int main()
{
	freopen("inputBF.txt","rt",stdin);
	freopen("outputBF.txt","wt",stdout);
	int kas,cas;cin>>kas;
	for(cas=0;cas<kas;cas++)
	{
	    double D,C,P[109],V[109];
	    double cur=0.0;
	    cin>>C>>D;
	    double res=10000000;
	    for(int i=0;i<C;i++)
	    {
	        double a,b;
	        cin>>a>>b;
	        P[i]=a;
	        V[i]=b;

	    }


	        double hi = 1000000,low=0;
double prev = 10000000;
	        while(low<hi)
	        {

	            double mid= (hi+low)/2.0;
	            if(fabs(prev-mid)<(10e-8))break;
	            double cur=P[0]-mid+eps;
	            int f=0;
	            for(int i=0;i<C;i++)
	            {
	                int t;
	                if(i==0)
	                t=1;


	                if(i!=0){
	                    if(P[i]-mid>cur+D || eq(P[i]-mid,cur+D)){
	                        cur=P[i]-mid+eps;
	                        t=1;
	                    }
	                    else t=0;
	                }

	                for(int j=t;j<V[i];j++)
	                {
	                    cur+=D;
	                    cur+=eps;
	                    if(fabs(cur-P[i])+eps>mid+eps){
	                        f=1;
	                        break;
	                    }
	                }
	                if(f)break;
	            }

	            if(!f){
	                res=min(mid+eps,res+eps);
	                hi=mid+eps;
	            }
	            else{
	                low=mid+eps;
	            }
	            prev=mid+eps;
	        }

	    cout<<"Case #"<<cas+1<<": ";
	    printf("%.9lf\n",res+eps);

	}

	return 0;
}
