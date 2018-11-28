
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<numeric>
#include<cmath>
#include<fstream>

using namespace std;

typedef _int64 i64;

i64 B(vector<i64> d,i64 t,i64 l)
{
	i64 time=0;
	i64 i,first;
	vector<i64> v;

	for(first=1;first<=d.size();)
	{
		if(time+d[first-1]*2>=t)
			break;
		else
			time+=d[first-1]*2,++first;
	}

	if(first==d.size()+1)
		return time;

	--first;

	for(i=first+2;i<=d.size();++i)
		v.push_back(d[i-1]);

	v.push_back(d[first]-(t-time)/2);
	time=t;

	sort(v.begin(),v.end());

	if(v.size()<=l)
		for(i=0;i<v.size();++i)
			time+=v[i];
	else
	{
		for(i=1;i<=l;++i)
			time+=v[v.size()-i];
		for(i=0;i<=v.size()-l-1;++i)
			time+=v[i]*2;
	}
	
	return time;
}

i64 atoi64(string s)
{
	i64 ret=0,i,j,k;

	for(i=s.size();i>=1;--i)
	{
		for(j=1,k=1;j<=i-1;++j)
			k*=10;
		ret+=(s[s.size()-i]-'0')*k;
	}

	return ret;
}

string i64toa(i64 n)
{
	string s;

	while(n)
	{
		s.insert(s.begin(),n%10+'0'),n/=10;
	}

	return s;
}

void main()
{
	int num,i,j;
 	i64 n,l,c;
	i64 t;
	i64 k;
	string s;
	ifstream fin("C:\\Users\\dark\\Desktop\\gcj2011\\B-small\\B-large.in");
	ofstream fout("C:\\Users\\dark\\Desktop\\gcj2011\\B-small\\B-small.txt");
	vector<i64> v,temp;
	
	fin>>num;

	for(i=1;i<=num;++i)
	{
		v.clear();
		temp.clear();

		fin>>s;

		l=atoi64(s);

		fin>>s;

		t=atoi64(s);

		fin>>s;

		n=atoi64(s);

		fin>>s;

		c=atoi64(s);
		

		for(j=1;j<=c;++j)
		{
			fin>>s;
			k=atoi64(s);
			temp.push_back(k);
		}

		for(j=1;j<=n;++j)
		{
			v.push_back(temp[(j-1)%c]);
		}

		fout<<"Case #"<<i<<": ";
		s=i64toa(B(v,t,l));
		fout<<s<<endl;
	}

/*	i64 l=2;
	i64 t=271610 ;
	i64 a[]={6592 ,189 ,2166,9187 ,4145, 6722 ,6723, 6908 ,7708 ,2150, 4699 ,1990 ,8875 ,8889 ,2792 ,8926 ,6079 ,7511 ,5631 ,556 ,9342 ,3253 ,6356, 2570 ,9820 ,6454, 9140, 2038 ,6950 ,4360, 4053 ,6825 ,1834,4149 ,1649, 7955, 1203, 1372, 546, 4195 ,1351, 974 ,7201 ,4848, 624 ,1157 ,1948, 6440 ,7208 ,9370 ,1713 ,8697 ,2863 ,2878, 6634, 7111,9804, 9234 ,5046 ,2977,7779 ,8338 ,3227};
	vector<i64> d(a,a+63);

	i64 time=B(d,t,l);
	cout<<time<<endl;*/
}
