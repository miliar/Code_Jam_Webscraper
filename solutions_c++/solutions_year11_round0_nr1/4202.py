
#include <iostream>
using namespace std;
int f(int a){
	return a>0?a:-a;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("largeret.out","w",stdout);
	int T,n,t,o,b,s,cases=1,fo,fb,zl;
	char c;
	cin >>T;
	while (T--)
	{
		cin >>n;
		s=0;
		fo=fb=0;
		o=b=1;
		for (int i=0;i<n;i++)
		{
			cin >>c>>t;
			if(c=='O'){
				zl=f(t-o);
				if(fo<=zl){
					s=s+zl-fo+1;					
					fb=fb+zl-fo+1;
					fo=0;
					o=t;
				}
				else {
					s++;
					fo=0;
					fb++;
					o=t;
				}
				
			}
			else{		
				zl=f(t-b);
				if(fb<=zl){
					s=s+zl-fb+1;					
					fo=fo+zl-fb+1;
					fb=0;
					b=t;
				}
				else{
					s++;
					fb=0;
					fo++;
					b=t;
				}
				
			}
		}
		cout <<"Case #"<<cases++<<": "<<s<<endl;
	}
	return 0;
}