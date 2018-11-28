#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef  pair<int,int> A;

class f
{
public:
	bool operator()(const A &x,const A &y)
	{
		return x.first<y.first?true:false;
	}
};
int main(void)
{
	int T,N;
	int caseid;
	int i,j,k;
	vector<A>  v;
	int first,second;
	int sum;

	cin>>T;
	for(caseid=1;caseid<=T;caseid++)
	{
		cin>>N;
		
		for(i=0;i<N;i++)
		{
			cin>>first>>second;
			v.push_back(make_pair(first,second));
		}

		sort(v.begin(),v.end(),f());
		sum=0;
		for(i=0;i<N-1;i++)
		{
			for(k=0,j=i+1;j<N;j++)
				if(v[j].second<v[i].second)
					k++;
			sum+=k;
		}

		cout<<"Case #"<<caseid<<": "<<sum<<endl;
		v.clear();

	}
}
