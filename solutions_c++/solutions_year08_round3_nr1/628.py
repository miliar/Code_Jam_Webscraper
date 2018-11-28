#include<iostream>
#include<string>
#include<list>
using namespace std;

struct a
{
	int num;

};

list<a> num;

bool operator < (a &x, a &y)
{
 return (x.num > y.num);
}

int main()
{
	int N,N2,p,k,l,i,times,keys,sum,imp;
	a temp;
	cin>>N;
	N2 = N;
	while(N--)
	{
		cin>>p>>k>>l;
		num.clear();
		for(i=0; i<l; i++)
		{
			cin>>temp.num;
			num.push_back(temp);
		}
		times = 1;
		keys = 0;
		sum = 0;
		imp = 0;
		num.sort();
		list<a>::iterator j;
		for(j=num.begin(); j!=num.end(); j++)
		{
			sum+= times*(*j).num;
			keys++;
			if(keys == k)
			{
				keys=0;
				times++;
			}
			if(times > p)
			{
				imp = 1;
				j++;
				break;
			}
		}	
		if(imp==0 || j==num.end())
			cout<<"Case #"<<-(N-N2)<<": "<<sum;
		else
			cout<<"Case #"<<-(N-N2)<<": Impossible";
		if(N) cout<<endl;
	}
}
