#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

ifstream fin("ctc");
#define cin fin

void stuff()
{
	int i,j;
	double X,S,R,T,N;
	double b,e,speed;
	double sum,time=0;
	vector<pair<double,double> > lengths;//speed,length
	vector<pair<double,double> >::iterator it;
	cin>>X>>S>>R>>T>>N;
	sum=0;
	for(i=0;i<N;i++)
	{
		cin>>b>>e>>speed;
		speed+=S;
		lengths.push_back(make_pair(speed,e-b));
		sum+=(e-b);
	}
	lengths.push_back(make_pair(S,X-sum));
	sort(lengths.begin(),lengths.end());
	it=lengths.begin();
	while(T>0 && it != lengths.end())
	{
		double a=(*it).second/((*it).first-S+R);
		if( a<T)
		{
			time+=a;
			T-=a;
		}
		else
		{
			time+=T;
			it->second-=T*((*it).first-S+R);
			T=0;
			break;
		}
		it++;
	}
	if(it==lengths.end())
	{
		cout<<time;
		return;
	}
	while(it !=lengths.end())
	{
		time+=((it->second)/(it->first));
		it++;
	}
	cout<<time;
	
}

int main(void)
{
	int T;
	cin>>T;
	cout.precision(10);
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		stuff();
		cout<<endl;
	}
}
