#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <math.h>
#include <cstdlib>
#include <ctime>

using namespace std;
vector<bool> v, g, c;

class BT
{
	public:
		int n;
		bool v, g, c, av;
		BT *lc, *rc;
			
		BT()
		{
			lc = rc = NULL;
			n = 0;
			v = false;
			g = false;
			c = false;
			av = false;
		}
		
		bool calc()
		{	
			if(!g)
				av = v;
			else
				if(v)
					av = lc -> calc() & rc -> calc();
				else
					av = lc -> calc() | rc -> calc();
			
			//cout<<n<<"  "<<av<<endl;
				
			return av;
		}
		
		int fix(bool x)
		{
			int best = 11000;
			
			if(av == x)
				return 0;
				
			if(!g)
				return -1;
					
			if(c)
				if(v)
				{
					if((lc -> av | rc -> av) == x)
						return 1;
				}
				else
				{
					if((lc -> av & rc -> av) == x)
						return 1;
				}
				
			if(v)
				if(x)
				{
					int a = lc -> fix(true);
					int b = rc -> fix(true);
					if(a==-1 || b==-1){ }
					else { if(best>a+b) best = a+b; }
				}
				else
				{
					int a = lc -> fix(false);
					int b = rc -> fix(false);
					
					if(a==-1 && b==-1) { }
					else if(a==-1) { if(best>b) best = b; }
					else if(b==-1) { if(best>a) best = a; }
					else if(a<b) { if(best>a) best = a; }
					else { if(best>b) best = b; }
				}
					
			if(!v)
				if(!x)
				{
					int a = lc -> fix(false);
					int b = rc -> fix(false);
					if(a==-1 || b==-1){ }
					else { if(best>a+b) best = a+b; }
				}
				else
				{
					int a = lc -> fix(true);
					int b = rc -> fix(true);
					
					if(a==-1 && b==-1) { }
					else if(a==-1) { if(best>b) best = b; }
					else if(b==-1) { if(best>a) best = a; }
					else if(a<b) { if(best>a) best = a; }
					else { if(best>b) best = b; }
				}
				
			if(c && !v)
				if(x)
				{
					int a = lc -> fix(true);
					int b = rc -> fix(true);
					if(a==-1 || b==-1){ }
					else { if(best>a+b) best = 1+a+b; }
				}
				else
				{
					int a = lc -> fix(false);
					int b = rc -> fix(false);
					
					if(a==-1 && b==-1) { }
					else if(a==-1) { if(best>b) best = 1+b; }
					else if(b==-1) { if(best>a) best = 1+a; }
					else if(a<b) { if(best>a) best = 1+a; }
					else { if(best>b) best = 1+b; }
				}
					
			if(c && v)
				if(!x)
				{
					int a = lc -> fix(false);
					int b = rc -> fix(false);
					if(a==-1 || b==-1){ }
					else { if(best>a+b) best = 1+a+b; }
				}
				else
				{
					int a = lc -> fix(true);
					int b = rc -> fix(true);
					
					if(a==-1 && b==-1) { }
					else if(a==-1) { if(best>b) best = 1+b; }
					else if(b==-1) { if(best>a) best = 1+a; }
					else if(a<b) { if(best>a) best = 1+a; }
					else { if(best>b) best = 1+b; }
				}
			
			if(best == 11000)
				return -1;
			return best;
		}
};

BT* form(int x, int n)
{
	BT *b = new BT;
	
	b -> n = x;
	b -> v = v[x];
	b -> g = g[x];
	b -> c = c[x];
	
	if(n >= 2*x)
	{
		b -> lc = form(2*x,n);
		b -> rc = form(2*x+1,n);
	}
	else
		b -> lc = b -> rc = NULL;
		
	return b;
}

int main()
{
    fstream in,out;
    in.open("A-large.in",ios::in);
    out.open("A-large.out",ios::out);
    
    /*problem specific code starts here*/
    
    long long N;
    in>>N;
    
    for(long long i=0;i<N;i++)
    {
		int M,V,j,res;
		in>>M>>V;
		
		v.clear();
		g.clear();
		c.clear();
		
		v.push_back(false);
		g.push_back(false);
		c.push_back(false);
				
		for(j=0;j<(M-1)/2;j++)
		{
			int x,y;
			in>>x>>y;
			
			v.push_back(x?true:false);
			g.push_back(true);
			c.push_back(y?true:false);
		}
		
		for(j;j<M;j++)
		{
			int x;
			in>>x;
			
			v.push_back(x?true:false);
			g.push_back(false);
			c.push_back(false);
		}
		
		BT *b = form(1,M);
		
		b -> calc();
		
		//cin>>res;
		
		res = b -> fix(V?true:false);
		
		out<<"Case #"<<i+1<<": ";
		if(res == -1)
			out<<"IMPOSSIBLE";
		else
			out<<res;
		out<<endl; 
	}
    
    /*problem specific code ends here*/
    
    in.close();
    out.close();
    
    return 0;
}
