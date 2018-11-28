#include <iostream>
using namespace std;

int cases,i,n,s,p,j,t,wynik;



int main()
{
	ios_base::sync_with_stdio(0);
	cin>>cases;
	for(i=0;i<cases;++i)
	{
		wynik=0;
		cin>>n;
		cin>>s;
		cin>>p;
		for(j=0;j<n;++j)
		{
			cin>>t;
			if(t<2)
			{
				if(t>=p) {++wynik;}
			}
			else if(t>28)
			{
				if(10>=p) {++wynik;}
			}
			else if(t%3==0)
			{
				if(int(t/3)>=p) {++wynik;}
				else if(int(t/3)+1>=p) {if(s>0) {++wynik; --s;}}
			}
			else if(t%3==1)
			{
				if(int(t/3)+1>=p) {++wynik;}
			}
			else
			{
				if(int(t/3)+1>=p) {++wynik;}
				else if(int(t/3)+2>=p) {if(s>0) {++wynik; --s;}}
			}
		}
		cout<<"Case #"<<i+1<<": "<<wynik<<endl;
	}
	return 0;
}
