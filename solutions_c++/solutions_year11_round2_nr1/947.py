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
#define eps 0.00000000000000001
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
	freopen("inputB.txt","rt",stdin);
	freopen("outputB.txt","wt",stdout);
	int cas,kas;
	cin>>kas;
	for(cas=0;cas<kas;cas++)
	{
	    int n;cin>>n;
	    string str[109];
	    for(int i=0;i<n;i++)
	    cin>>str[i];

	    double wp[109],wop[109],wwop[109],won[109],lost[109],total[109],final_res[109];


	    for(int i=0;i<109;i++)
	    wp[i]=wop[i]=wwop[i]=won[i]=lost[i]=total[i]=final_res[i]=0;


	    for(int i=0;i<n;i++)
	    {
	        double win=0,loss=0;
	        for(int j=0;j<n;j++)
	        {
	            if(str[i][j]=='1')win++;
	            if(str[i][j]=='0')loss++;
	        }
	        if(win+loss>0)
	        {
	            wp[i]=(win/(win+loss));
	        }
	        won[i]=win;
	        lost[i]=loss;
	        total[i]=win+loss;
	        final_res[i]=(0.25*wp[i]);
	    }


	    for(int i=0;i<n;i++)
	    {
	        double w=0,l=0,t=0,x=0;
	        double res=0;
	        for(int j=0;j<n;j++)
	        {
	            if(str[i][j]!='.')
	            {
	                if(str[i][j]=='1')
	                {
	                    w=won[j];
	                    t=total[j]-1;
	                }
	                else if(str[i][j]=='0')
	                {
	                    w=won[j]-1;
	                    t=total[j]-1;
	                }
	                res+=(w/t);
	                wop[i]=w/t;
	                x++;
	            }
	        }
	        wop[i]=res*(1.0000/x);
	        final_res[i]+=(.5*wop[i]);
	    }


	    for(int i=0;i<n;i++)
	    {
	        double c=0,x=0;
	        for(int j=0;j<n;j++)
	        {
	            if(str[i][j]!='.')
	            {
	                c++;
	                x+=(wop[j]);
	            }
	        }

	        wwop[i]=x/c;
	        final_res[i]+=(.25*wwop[i]);
	    }
	    cout<<"Case #"<<cas+1<<":"<<endl;
	    for(int i=0;i<n;i++)
	    {
	        printf("%.8lf\n",final_res[i]+eps);
	    }
	}

	return 0;
}
