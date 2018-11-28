#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>

using namespace std;


long long int n,l,h; 

bool check(long long int val,vector<long long int> &v)
{
	for(long long int i=0;i<v.size()-1;i++)
	{
		if(v[i]%val==0 || val%v[i]==0)continue;
		return false;
	}
	return true;
}
bool range(long long int x)
{
	if(x>=l && x<=h)return true;
	return false;
}
bool solve()
{
	
	long long int i,x;
	vector<long long int> v,vv;
	
	cin>>n>>l>>h;

	for(i=1;i<=n;i++){cin>>x;v.push_back(x);}

	
	for(i=1;i*i<=x;i++)
	{
		if(x%i==0 && range(i))
			vv.push_back(i);
		if(x%(x/i)==0 && range(x/i))
			vv.push_back(x/i);
	}
	for(i=l/x;i<=h/x;i++)
		if(range(i*x))vv.push_back(i*x);

	sort(vv.begin(),vv.end());

	//cout<<"~~~~~";
	//for(i=0;i<vv.size();i++)	
	//	cout<<vv[i]<<" ";
	//cout<<endl;

	for(i=0;i<vv.size();i++)
		if(check(vv[i],v)){cout<<vv[i]<<endl;return false;}		
	return true;
}

int main()
{
	long long int i,t;
	for(cin>>t,i=1;i<=t;i++)
	{
		printf("Case #%lld: ",i);
		if(solve())cout<<"NO\n";
	}
	return 0;
}
