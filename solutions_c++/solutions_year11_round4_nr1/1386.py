#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define max(a,b) (a)>(b)?(a):(b)
struct Node
{
	double B,E,W;
	Node(){}
	Node(double _B,double _E,double _W):B(_B),E(_E),W(_W){}
	bool operator< (const Node A) const
	{
		return W < A.W;
	}
};

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cases,N;
	double X,S,R,T;
	double B,E,W;
	cin>>cases;
	for(int cas=1;cas<=cases;cas++)
	{
		cin>>X>>S>>R>>T>>N;
		int start = 0;
		vector<Node>v;
		for(int i=0;i<N;i++)
		{
			cin>>B>>E>>W;
			if(start<B)
			{
				v.push_back(Node(start,B,0));
			}
			v.push_back(Node(B,E,W));
			start = E;
		}
		if(E < X)v.push_back(Node(E,X,0));

		sort(v.begin(),v.end());
		double sum = 0;
		for(int i=0;i<v.size();i++)
		{
			if(T > 0)
			{
				double tmp = (v[i].E - v[i].B)/(R + v[i].W);
				if(tmp < T)
				{
					T -= tmp;
					sum += tmp;
				}
				else
				{
					sum += (v[i].E - v[i].B - (R + v[i].W) * T)/(v[i].W + S) + T;
					T = 0;
				}
				
			}
			else
			{
				sum += (v[i].E - v[i].B)/(S + v[i].W);
			}
		}
		printf("Case #%d: %lf\n",cas,sum);
	}
}