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
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 



using namespace std; 

template<class T> T gcd(T a,T b){return a==0?b:gcd(b%a,a);}
FILE *f;
int main()
{
	int t;
	int a;
	int b;
	int r;
	
	freopen("do.txt","r",stdin);
	freopen("fian.txt","w",stdout);
    cin>>t;
	for(int i=0;i<t;i++)
	{
		r=0;
		cin>>a;
		for(int j=0;j<a;j++)
		{
			cin>>b;
			if(b!=j+1)r++;
		}
		cout<<"Case #"<<i+1<<":"<<" "<<r<<endl;
	}
	return 0;	
}