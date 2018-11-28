#include <iostream>
#include <cmath>
#include <vector>
#include <iterator>
#include <numeric>
#include <cstdio>
#include <string>
#include <algorithm>
#include <queue>

template <class T>
T tabs (T a)
{
    if (a<0)
        return -a;
    return a;
}

template <class T>
T tmin (T a, T b)
{
	if (a>b)
		return b;
	return a;
}

template <class T>
T tmax (T a, T b)
{
	if (a<b)
		return b;
	return a;
}

struct robot
{
	int a;
	bool b;
};


using namespace std;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tests, res,q=0;
	cin>>tests;
	while (tests--)
	{
		q++;
		res=0;
		int o=1,b=1;
		queue<pair<int,int> > orange, blue;
		int k;
		cin>>k;
		robot t;
		char ch;
		for (int i=0;i<k;++i)
		{	
			cin>>ch>>t.a;
			if(ch=='B')
				t.b=true;
			else 
				t.b=false;
			if (t.b)
				blue.push(make_pair(t.a,i));
			else
				orange.push(make_pair(t.a,i));
		}
		k=0;
		while(!blue.empty() && !orange.empty())
		{
			int l;
			bool go;
			if (blue.front().second==k)
			{
				l=tabs(blue.front().first-b)+1;
				b=blue.front().first;
				blue.pop();
				go=(o<orange.front().first);
				if (go)
					o=tmin(orange.front().first, o+l);
				else
					o=tmax(orange.front().first, o-l);
			}
			else 
			{
				l=tabs(orange.front().first-o)+1;
				o=orange.front().first;
				orange.pop();
				go=(b<blue.front().first);
				if (go)
					b=tmin(blue.front().first, b+l);
				else
					b=tmax(blue.front().first, b-l);
			}
			res+=l;
			k++;
		}
		while (!blue.empty())
		{
			res+=tabs(blue.front().first-b)+1;
			b=blue.front().first;
			blue.pop();
		}
		while (!orange.empty())
		{
			res+=tabs(orange.front().first-o)+1;
			o=orange.front().first;
			orange.pop();
		}
		cout<<"Case #"<<q<<": "<<res<<endl;
	}
}
