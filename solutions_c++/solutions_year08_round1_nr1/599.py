#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <fstream>
#include <deque>

using namespace std;



int main()
{
	ifstream entrada("A-large.in");
	ofstream salida("salida.out");
	int T;
	entrada>>T;
	for(int _T=0;_T<T;++_T)
	{
		int n;
		entrada>>n;
		deque<int> xs,ys;
		int temp;
		for(int _n=0;_n<n;++_n)
		{
			entrada>>temp;
			xs.push_back(temp);
			push_heap(xs.begin(),xs.end());
		}
		sort_heap(xs.begin(),xs.end());
		
		for(int _n2=0;_n2<n;++_n2)
		{
			entrada>>temp;
			ys.push_back(temp);
			push_heap(ys.begin(),ys.end());
		}
		sort_heap(ys.begin(),ys.end());
		long long res=0;
		long long aux;
		int a=xs.size();
		for(int i=0;i<a;++i)
		{
			long long x,y;
			if(xs.front()<=ys.front())
			{
				x=xs.front();
				y=ys.back();
				xs.pop_front();
				ys.pop_back();
			}
			else
			{
				x=xs.back();
				y=ys.front();
				xs.pop_back();
				ys.pop_front();
			}
			aux=x*y;
			res+=aux;
		}
		salida<<"Case #"<<_T+1<<": "<<res<<endl;

	}

	return 0;
}
