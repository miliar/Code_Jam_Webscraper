#include<iostream>
#include<math.h>
#include<string>
#include<list>
#include<utility>

using namespace std;

bool compare(pair<int,int> a,pair<int,int> b)
{
	if(a.first>b.first)
		return true;
	else if(a.first<b.first)
		return false;
	else if(a.second>=b.second)
		return true;
	else
		return false;
}


bool operator >=(pair<int,int> a,pair<int,int> b)
{
	if(a.first>b.first)
		return true;
	else if(a.first<b.first)
		return false;
	else if(a.second>=b.second)
		return true;
	else
		return false;
}

pair<int,int> operator +(pair<int,int> a,int b)
{
	a.second+=b;
	while(a.second>=60)
	{
		a.first++;
		a.second-=60;
	}
	if(a.first<24)
		return a;
	else
	{
		a.first=23;
		a.second=59;
		return a;
	}
}

pair<int,int> operator -(pair<int,int> a,int b)
{
	if(b<a.second)
	{
		a.second-=b;
		return a;
	}
	else
	{
		while(b>a.second)
		{
			b-=60;
			a.first-=1;
		}
		if(b==a.second)
			a.second==0;
		if(a.first<0)
		{
			a.first=0;
			a.second=0;
			return a;
		}
		else
			return a;
	}
}

int main()
{
	int ncases;
	cin>>ncases;
	int turn_time;
	int na,nb,ta,tb;
	int temp1,temp2;
	list< pair<int,int> > A_arrivs,B_arrivs,A_depts,B_depts;
	list< pair<int,int> >::iterator i,j;
	for(int itr=0;itr<ncases;itr++)
	{
		cin>>turn_time;
//		cout<<"turn_time"<<turn_time<<"\n";
		cin>>na>>nb;
		ta=na;
		tb=nb;
//		cout<<"na"<<na<<"nb"<<nb<<"\n";
		char token,token1;
		token=cin.get();
		for(int iint=0;iint<na;iint++)
		{
			token=cin.get();
			token1=cin.get();
			temp1=(token-48)*10+(token1-48);
			token=cin.get();
			token=cin.get();
			token1=cin.get();
			temp2=(token-48)*10+(token1-48);
			pair<int,int> newpair(temp1,temp2);
	//		cout<<"t1"<<temp1<<"t2"<<temp2<<"\n";
			A_depts.push_back(newpair);

			token=cin.get();

			token=cin.get();
			token1=cin.get();
			temp1=(token-48)*10+(token1-48);
			token=cin.get();
			token=cin.get();
			token1=cin.get();
			temp2=(token-48)*10+(token1-48);
			pair<int,int> newpair1(temp1,temp2);
			B_arrivs.push_back(newpair1);			
			
			token=cin.get();
		}
		for(int iint=0;iint<nb;iint++)
		{
			token=cin.get();
			token1=cin.get();
			temp1=(token-48)*10+(token1-48);
			token=cin.get();
			token=cin.get();
			token1=cin.get();
			temp2=(token-48)*10+(token1-48);
			pair<int,int> newpair(temp1,temp2);
			B_depts.push_back(newpair);

			token=cin.get();

			token=cin.get();
			token1=cin.get();
			temp1=(token-48)*10+(token1-48);
			token=cin.get();
			token=cin.get();
			token1=cin.get();
			temp2=(token-48)*10+(token1-48);
			pair<int,int> newpair1(temp1,temp2);
			A_arrivs.push_back(newpair1);			
			token=cin.get();
		}
//		cout<<na<<" "<<nb<<"\n";
		A_depts.sort(compare);A_depts.reverse();
		A_arrivs.sort(compare);A_arrivs.reverse();
		B_depts.sort(compare);B_depts.reverse();
		B_arrivs.sort(compare);B_arrivs.reverse();
		for(i=A_depts.begin();i!=A_depts.end();i++)
		{
	//		cout<<"adept"<<(*i).first<<":"<<(*i).second<<"\n";
			for(j=A_arrivs.begin();j!=A_arrivs.end();j++)
			{
	//			cout<<(*j+turn_time).first<<":"<<(*j+turn_time).second<<" ";
				if(*i >= (*j+turn_time))
				{
					ta--;
					A_arrivs.erase(j);
					break;
				}
			}
	//		cout<<"\n";
		}
		for(i=B_depts.begin();i!=B_depts.end();i++)
		{
	//		cout<<"bdept"<<(*i).first<<":"<<(*i).second<<"\n";
			for(j=B_arrivs.begin();j!=B_arrivs.end();j++)
			{
	//			cout<<(*j+turn_time).first<<":"<<(*j+turn_time).second<<" ";
				if(*i >= (*j+turn_time))
				{
					tb--;
					B_arrivs.erase(j);
					break;
				}
			}
	//		cout<<"\n";
		}
		cout<<"Case #"<<(itr+1)<<": "<<ta<<" "<<tb<<"\n";
		A_depts.clear();A_arrivs.clear();B_depts.clear();B_arrivs.clear();
	}
}
