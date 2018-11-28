#include<iostream>
#include<fstream>
using namespace std;


long long int Gcd(long long int a,long long  int b)
{
	if(b==0)
		return a;
	return Gcd(b,a%b);
}

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-ll.out");
    long long int n,pd,pg,t,k=0,base;
    cin>>t;
    while(t--)
    {
    	cin>>n>>pd>>pg;
		
    	base = Gcd(100,pd);
    	base = 100/base;
		
    	if(base>n)
    	{
    		cout<<"Case #"<<++k<<": Broken"<<endl;
    	}
    	else if(pg==100 && pd<100)
    	{
    		cout<<"Case #"<<++k<<": Broken"<<endl;
    	}
		else if(pg == 0 && pd>0)
		{
			cout<<"Case #"<<++k<<": Broken"<<endl;
    	}
		else cout<<"Case #"<<++k<<": Possible"<<endl;
    }

    return 0;
}
