#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#define FOR(i,a,b) for(int i=(int)a;i<(int)b;++i)
#define REP(i,n) FOR(i,0,n)
#define IT(c) __typeof((c).begin())
#define FORIT(i,c) for(IT(c) i=(c).begin();i != (c).end();++i)
#define ALL(c) (c).begin() , (c).end()
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define PB push_back
#define MP make_pair
#define TC int tt;scanf("%d",&tt);while(tt--)
using namespace std;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out","w",stdout);
    int count=1;
    TC
    {
    	int a,b;
    	cin >> a >> b;
    	char arr[a][b];
    	REP(i,a)
    	{
    	   REP(j,b)
    	     cin >> arr[i][j];
    	 } 
    	    int r[3] ={0,1,1};
    	    int c[3] ={1,0,1};
    	char sym[3] = { 92,92,47};
    	bool total=0;
    	bool present=1;
    	int flag=1;
  		REP(i,a)
  		{
  			REP(j,b)
  			{
  				flag=0;
  				if(arr[i][j]=='#')
  				{
  					present=0;
  					REP(k,3)
  					{
  						if( i+r[k]<a && j+c[k]<b)
  						{
  							//cout <<arr[i+r[k]][j+c[k]]<<" ";
  							if(arr[i+r[k]][j+c[k]] == '#' )
  							{
  							
  							   flag++;
  							}
  						}
  					}
  				//	  							cout <<"\n";
  				}
  				if(flag==3)
  				{
  			//		cout << i << " "<< j <<"\n\n\n";
  					arr[i][j]=47;
  					REP(l,3)
  					{
  						arr[i+r[l]][j+c[l]] = sym[l];
  					}
  					total=1;
  				}
  			}
  		}
  		int pre=0;
  			REP(i,a)
  			   REP(j,b)
  			     if(arr[i][j]=='#')
  			       pre++;
  			if((total||present)&&pre==0)
  			{
		    	cout <<"Case #"<<count <<": "<<"\n";
		    	REP(i,a)
		    	{
		    	 REP(j,b)
		    	 {
		    	 	printf("%c",arr[i][j]);
		    	  }
		    	 cout <<"\n";
		    	}
		    }
		    else 
		    {
		    	cout <<"Case #"<<count <<": "<<"\n"<<"Impossible"<<"\n";
		    }
		    count++; 	   	
    }
	return 0;
}























