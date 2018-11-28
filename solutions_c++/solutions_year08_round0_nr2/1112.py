#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

void insert(int x, vector<int> &v)
{
	int i=v.size();
	v.push_back(x);
	while (i>0)
	{
		if (v[i]<v[i-1])
		{
			int t=v[i];
			v[i]=v[i-1];
			v[i-1]=t;
		}
		i--;
	}
}

void pop(vector<int> &v)
{
	for (int i=0; i<v.size()-1; i++)
		v[i]=v[i+1];
	v.pop_back();
}

int main()
{
	string s;
	int N;
	cin>>N;
	int a[105], A[105], b[105], B[105];
	int na,nb,t;
	int ca,cb,i,j,x;
	vector<int> sa, sb;
	for (int test=1; test<=N; test++)
	{
		sa.clear();
		sb.clear();
		ca=cb=0;
		cin>>t>>na>>nb;
		for (i=0; i<na; i++)
		{
			cin>>s;
			s[2]=' ';
			istringstream in(s);
			int h,m;
			in>>h>>m;
			a[i]=h*60+m;
			cin>>s;
			s[2]=' ';
			istringstream IN(s);
			IN>>h>>m;
			A[i]=h*60+m+t;
		}
		for (i=0; i<nb; i++)
		{
			cin>>s;
			s[2]=' ';
			istringstream in(s);
			int h,m;
			in>>h>>m;
			b[i]=h*60+m;
			cin>>s;
			s[2]=' ';
			istringstream IN(s);
			IN>>h>>m;
			B[i]=h*60+m+t;
		}
		for (i=0; i<na; i++)
			insert(A[i],sa);
		for (i=0; i<nb; i++)
			insert(B[i],sb);
		for (i=0; i<na-1; i++)
			for (j=i+1; j<na; j++)
				if (a[i]>a[j])
				{
					x=a[i];
					a[i]=a[j];
					a[j]=x;
				}
		for (i=0; i<nb-1; i++)
			for (j=i+1; j<nb; j++)
				if (b[i]>b[j])
				{
					x=b[i];
					b[i]=b[j];
					b[j]=x;
				}
		/*
		cout<<"   departures (A):";
		for (i=0; i<na; i++)
			cout<<a[i]<<' ';
		cout<<"\n   arrivals (A):";
		for (i=0; i<nb; i++)
			cout<<sb[i]<<' ';
		cout<<"\n   departures (B):";
		for (i=0; i<nb; i++)
			cout<<b[i]<<' ';
		cout<<"\n   arrivals (B):";
		for (i=0; i<na; i++)
			cout<<sa[i]<<' ';
		cout<<endl;
		*/
		for (i=0; i<na; i++)
		{
			if (sb.size()>0 && a[i]>=sb[0])
			{
				//cout<<"bus (A)"<<a[i]<<" used the one arrived at "<<sb[0]<<endl;
				pop(sb);
			}
			else
				ca++;
		}
		for (i=0; i<nb; i++)
		{
			if (sa.size()>0 && b[i]>=sa[0])
			{
				//cout<<"bus (B)"<<b[i]<<" used the one arrived at "<<sa[0]<<endl;
				pop(sa);
			}
			else
				cb++;
		}
		cout<<"Case #"<<test<<": "<<ca<<" "<<cb<<endl;
	}
	return 0;
}
