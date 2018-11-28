#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <fstream>
#include <sstream>
using namespace std;

/*bool check( int n, int base )
{
	vector<int> vc;
	int temp, m;
	m = n;
	while( m )
	{
		temp = m%base;
		vc.push_back(temp);
		m /= base;
	}
	
	int i,j, pp = 0;
	for( i = 0 ; i < vc.size(); i++)
	{
		pp
	}
} */
bool ty(int n, int base)
{
	int i, j, temp;
	int pp = 0;
	vector<int> vc;
	vector<int> path;
	while( n )
	{
		temp = n%base;
		vc.push_back(temp);
		n /= base;
	}
	for(i=0; i<vc.size(); i++)
		pp+=vc[i]*vc[i];
	while(pp!=1)
	{
		for( j = 0; j<path.size(); j++)
			if( pp == path[j] )
				return false;
		path.push_back( pp );

//		cout<<pp<<endl;
		vector<int> next;
		while( pp )
		{
			temp = pp%base;
			next.push_back(temp);
			pp /= base;
		}
		pp = 0;
		for(i=0; i<next.size(); i++)
			pp+= next[i]*next[i];
	}
	return true;
	
}
int main()
{
//	fstream in("try.txt");
//	int a[] = { 8, 3};
//	vector<int> vc(a, a+2);
/*	int n = 143;
	int base = 7;
	if( ty(n, base) )
		cout<<"yes"<<endl;
	else 
		cout<<"no"<<endl; */

	fstream in("try1.in");
	ofstream out("o1.txt");
	int T;
	
	int i;
	int bs;
//	scanf("%d", &T);
	string str;
	in>>T;
	stringstream ss;
	getline(in,str);

	
	for(i=0;i<T; i++)
	{
		out<<"Case #"<<i+1<<": ";
		getline(in, str);
		ss.clear();
		ss.str("");
		ss<<str;
		vector<int> base;
		while(ss>>bs)
		{
//			cout<<bs<<endl;
			base.push_back(bs);
		}
		int res = 2;
		bool flag;
		while(1)
		{
			flag = true;
//			cout<<"bs size: "<<base.size()<<endl;
			for(int k =0;k<base.size();k++)
			{
				if(!ty(res,base[k]))
				{
//					cout<<"o1"<<endl;
					flag = false;
					break;
				}
			}
			if(flag)
			{
//				cout<<"result: "<<res<<endl;
		//		return res;
				out<<res<<endl;
				break;
			}
			else
				res++;

		}
		
	}
	
}