#include<iostream>
#include<fstream>
#include<algorithm>
#include<limits>
#include<sstream>
#include<vector>
#include<string>
#include<functional>
using namespace std;

vector<long> v1,v2;
long calc()
{
	long ret=0;
	sort(v1.begin(),v1.end(),greater<long>());
	sort(v2.begin(),v2.end());
	for(int i=0;i<v1.size();i++)
		ret+=(v1[i]*v2[i]);
	return ret;
}

int main()
{
	int i,j;
	char str[1000];
	long T,t;
	long n;
	stringstream ss;
	fstream f1,f2;
	f1.open("c:\\gcj1\\A-small-attempt0.in",ios::in);
	f2.open("c:\\gcj1\\A-small-attempt0.out",ios::out);
	f1.getline(str,1000);
	ss<<str;
	ss>>T;
	ss.clear();
	for(i=0;i<T;i++)
	{
	f1.getline(str,1000);
	ss<<str;
	ss>>n;
	ss.clear();
		f1.getline(str,1000);
		ss<<str;
		for(j=0;j<n;j++)
		{

			ss>>t;
			//cout<<t<<" ";
			v1.push_back(t);
		}
		//cout<<endl;
		ss.clear();
		f1.getline(str,1000);
		ss<<str;
		for(int j=0;j<n;j++)
		{
			ss>>t;
		//	cout<<t<<" ";
			v2.push_back(t);
		}
		//cout<<endl;
		ss.clear();
	//	d();
		f2<<"Case #"<<i+1<<": "<<calc()<<endl;
		v1.clear();
		v2.clear();
	}
	system("pause");
	}