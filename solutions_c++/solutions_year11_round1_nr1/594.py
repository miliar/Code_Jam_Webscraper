#include <iostream>

using namespace std;

long long t,n,pd,pg;

long long gcd(long long a,long long b)
{
	return (a%b==0)?b:gcd(b,a%b);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large-out.out","w",stdout);
    cin>>t;
    for(int cnt=1;cnt<=t;cnt++)
    {
        cin>>n>>pd>>pg;
        cout<<"Case #"<<cnt<<": ";
		if((pd==100 && pg==100) || (pd==0 && pg==0))
			cout<<"Possible"<<endl;
		else if((pd<100 && pg==100) || (pd>0 && pg==0))
			cout<<"Broken"<<endl;
		else
		{
			if(n>=100/gcd(100,pd))
				cout<<"Possible"<<endl;
			else
				cout<<"Broken"<<endl;
		}
    }
    return 0;
}
