

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

#define mp make_pair
#define pb push_back

template<class T> T gcd(T a,T b){return a==0?b:gcd(b%a,a);}
template<class T> string tostring(T a){ostringstream os;os<<a;return os.str();}
int toint(string a){istringstream is(a);int p;is>>p;return p;}
long long toll(string a){istringstream is(a);long long p;is>>p;return p;}

void printcase(int i)
{
	cout<<"Case #"<<i<<": ";
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	long long T;
	cin>>T;
	long long n,pd,pg;
for(long long i=1;i<=T;i++)
{
	cin>>n>>pd>>pg;
	long long dct;
	for(dct=1;dct<=100;dct++)
	{
		if(dct*pd%100==0)break;
	}
	long long dw=dct*pd/100;
	printcase(i);
	if(dct>n||(pg==0&&pd!=0)||(pg==100&&pd!=100))
	{
		cout<<"Broken"<<endl;
	}
	else
	{
		cout<<"Possible"<<endl;
	}

}
	//system("pause");
}