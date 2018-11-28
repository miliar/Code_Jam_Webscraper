#include<iostream>
#include<vector>
#include<map>
#include<fstream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>



using namespace std;
stringstream ss;

int LCM(__int64 a,__int64 b)
{
	__int64 i;
	if(a<b) {i=a;a=b;b=i;}
	i=b;
	while(i>0)
	{
		i=a%b;
		a=b;
		b=i;
	}
	return a;
}

int main()
{
	freopen("a3.in","r",stdin);
	freopen("a3.out","w",stdout);
	__int64 t,i,lcm;
	__int64 n,d,g;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n>>d>>g;
		if(d!=0) lcm=LCM(100,d);
		else lcm=999999;
		if( 100/lcm>n || (d<100 && g==100) || (d>0 && g==0))
		{
			cout<<"Case #"<<i<<": Broken"<<endl;
			
		}
		else
		{
			cout<<"Case #"<<i<<": Possible"<<endl;
			
		}
	}
 return 0;
}
