#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
class node
{
	public:
	int chick;
	vector<int> slow;
	node(int _c)
	{
		chick=_c;
	}
};
bool operator < (node a,node b)
{
	return a.slow.size() < b.slow.size();
}
//bool intersect(int x1,int v1,int x2,int v2,int T)
//{
	//1 is fast and 2 is slow
	
int f(int N,int K,int B,int T,vector<int> x,vector<int> v)
{
//cout<<"new\n";
	int i,j;
	vector<node> yes;
	for(i=0;i<N;++i)
		if(x[i]+v[i]*T>=B)
		{
			node* curr=new node(i);
			for(j=0;j<N;++j)
			{
				if(x[j]+v[j]*T<B)
				{
					if(x[j]>x[i])// intersect(x[i],v[i],x[j],v[j],T))
					{
						curr->slow.push_back(j);
					}
				}
			}
			yes.push_back(*curr);
		}
	sort(yes.begin(),yes.end());
	if(yes.size()<K)
		return -1;
	int ans=0;
	for(i=0;i<K;++i)
	{
//		cout<<yes[i].slow.size()<<endl;
		ans+=yes[i].slow.size();
	}
	return ans;
}
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int C;
	fin>>C;
	int c;
	for(c=1;c<=C;++c)
	{
		fout<<"Case #"<<c<<": ";
		int N,K,B,T;
		fin>>N>>K>>B>>T;
		int i;
		vector<int> x,v;
		int xi,vi;
		for(i=0;i<N;++i)
		{
			fin>>xi;
			x.push_back(xi);
		}
		for(i=0;i<N;++i)
		{
			fin>>vi;
			v.push_back(vi);
		}
		int ans=f(N,K,B,T,x,v);
		if(ans==-1)
			fout<<"IMPOSSIBLE"<<endl;
		else
			fout<<ans<<endl;
	}
	return 0;
}
