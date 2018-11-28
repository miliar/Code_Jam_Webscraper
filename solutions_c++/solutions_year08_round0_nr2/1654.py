#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
using namespace std;
bool v1[110],v2[110],v11[110],v22[110];
bool v[110][110];
int n,na,nb,t;
class node
{
public:
	int f1,s1,f2,s2;
	node(int f1_,int f2_,int s1_,int s2_)
	{
		f1=f1_;f2=f2_;
		s1=s1_;s2=s2_;
	}
	bool operator < (node& n2)
	{
		if(f1!=n2.f1)return (f1<n2.f1);else
		if(f2!=n2.f2)return (f2<n2.f2);else
		if(s1!=n2.s1)return (s1<n2.s1);else
		if(s2!=n2.s2)return (s2<n2.s2);else
		return false;
	}
};
vector<node> va,vb;
bool s1(node n1,node n2)
{
	if(n1.f1!=n2.f1)return (n1.f1<n2.f1);else
	if(n1.f2!=n2.f2)return (n1.f2<n2.f2);else
	if(n1.s1!=n2.s1)return (n1.s1<n2.s1);else
	if(n1.s2!=n2.s2)return (n1.s2<n2.s2);else
	return false;
}
/*
bool s2(node n1,node n2)
{
	return (n1.f1!=n2.f1?n1.f1<n2.f1:n1.f2<=n2.f2);
}


void f()
{
	sort(va.begin(),va.end(),s1);
	sort(vb.begin(),vb.end(),s2);
	for(int i=0;i<va.size();i++)
	{
		for(int j=0;j<vb.size();j++)
		{
			bool fl = (va[i].s1!=vb[j].f1?va[i].s1<vb[j].f1:va[i].s2<=va[j].f2) ;
			if(fl)
			{
				//cout<<va[i].s1<<" "<<va[i].s2<<" "<<vb[j].f1<<" "<<vb[j].f2<<endl;
				va.erase(va.begin()+i);
				break;
			}
		}
	}
	sort(vb.begin(),vb.end(),s1);
	sort(va.begin(),va.end(),s2);
	for(int i=0;i<vb.size();i++)
	{
		for(int j=0;j<va.size();j++)
		{
			bool f = (vb[i].s1!=va[j].f1?vb[i].s1<va[j].f1:vb[i].s2<=va[j].f2);
			if(f)
			{
				vb.erase(vb.begin()+i);
				break;
			}
		}
	}
}
*/
bool can(node n1,node n2)
{
	return ((n1.s1!=n2.f1?n1.s1<n2.f1:n1.s2<=n2.f2));
}
bool equal(node n1,node n2)
{
	return (n1.f1==n2.f1&&n1.f2==n2.f2&&n1.s1==n2.s1&&n1.s2==n2.s2);
}
bool ff(int i,int j,bool f)
{
	if(i>=va.size()||j>=vb.size())return true;
	if(f)
	{
		if((!v2[j])&&(!v11[i])&&can(va[i],vb[j]))
		{
			v2[j]=1;
			v11[i]=1;
			ff(i+1,j,false);
			return true;
		}
	}
	else
	{
		if((!v1[i])&&(!v22[j])&&can(vb[j],va[i]))
		{
			v1[i]=1;
			v22[j]=1;
			ff(i,j+1,true);
			return true;
		}
	}
	return false;
}

void f1(int i, int j)
{
}

void f2(int i, int j)
{
}


int main()
{
	freopen("B-large.in","r",stdin);	
	freopen("B-small.out","w",stdout);
	cin>>n;
	for(int i=0;i<n;i++)
	{
		va.clear();
		vb.clear();
		memset(v,0,sizeof(v));
		memset(v1,0,sizeof(v1));
		memset(v2,0,sizeof(v2));
		memset(v11,0,sizeof(v11));
		memset(v22,0,sizeof(v22));
		cin>>t>>na>>nb;
		cin.get();
		for(int j=0;j<na;j++)
		{
			string s;
			getline(cin,s);
			stringstream ss(s);
			int x1,x2,y1,y2;
			ss>>x1;
			ss.get();
			ss>>x2;
			ss.get();
			ss>>y1;
			ss.get();
			ss>>y2;
			y2+=t;
			if(y2>=60){y2%=60;y1++;}
			va.push_back(node(x1,x2,y1,y2));
		}
		for(int j=0;j<nb;j++)
		{
			string s;
			getline(cin,s);
			stringstream ss(s);
			int x1,x2,y1,y2;
			ss>>x1;
			ss.get();
			ss>>x2;
			ss.get();
			ss>>y1;
			ss.get();
			ss>>y2;
			y2+=t;
			if(y2>=60){y2%=60;y1++;}
			vb.push_back(node(x1,x2,y1,y2));
		}
		//f();
		int x=0,y=0;
		sort(va.begin(),va.end());
		sort(vb.begin(),vb.end());
		for(int k=0;k<va.size();k++)
			for(int j=0;j<vb.size();j++)
			{
				ff(k,j,false);
				ff(k,j,true);
			}
		for(int j=0;j<va.size();j++)
			if(!v1[j])x++;
		for(int j=0;j<vb.size();j++)
			if(!v2[j])y++;
		cout<<"Case #"<<i+1<<": "<<x<<" "<<y<<endl;
	}
	return 0;
}