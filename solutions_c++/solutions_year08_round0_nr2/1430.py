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

vector<string> split(string a,char d){int i; vector<string> s;string s1;for(i=0;i<a.size();i++)if(a[i]!=d)s1.push_back(a[i]);else{s.push_back(s1);s1.clear();}s.push_back(s1);return s;}
long long tonum(string a){int i; long long b=0;for(i=0;i<a.size();i++)b=b*10+a[i]-48;return b;}
int st;

struct timer
{
	int sh, sm, eh, em, st, t;
};
		
vector<timer> vt;

int diffA(timer A, timer B)
{
	return (A.sh*60+A.sm) - (B.sh*60+B.sm);
}

int diffB(timer A, timer B)
{
	return (B.sh*60+B.sm) - (A.eh*60+A.em);
}

vector<timer> sortit(vector<timer> vt)
{
	timer t;
	for(int i=0;i<vt.size()-1;i++)
		for(int j=i;j<vt.size();j++)
			if(diffA(vt[i],vt[j]) > 0)
			{
				t = vt[i];
				vt[i] = vt[j];
				vt[j] = t;
			}
			
	return vt;
}

timer setit(string s, string e, int st)
{
	timer t;
	
	vector<string> vs = split(s,':');
	t.sh = tonum(vs[0]);
	t.sm = tonum(vs[1]);
	
	vs = split(e,':');
	t.eh = tonum(vs[0]);
	t.em = tonum(vs[1]);
	
	t.st = st;
	t.t = -1;
	
	return t;
}

bool assignt(int T)
{
	int done = true;
	int sst = -1;
	timer t;
	
	for(int i=0;i<vt.size();i++)
	{
		if(vt[i].t == -1)
			if(sst == -1)
			{
				sst = vt[i].st;
				st = vt[i].st;
				t = vt[i];
				vt[i].t = 1;
			}
			else if(sst != vt[i].st && diffB(t,vt[i])>=T)
			{
				sst = vt[i].st;
				t = vt[i];
				vt[i].t = 1;
			}
		
		if(vt[i].t == -1)
			done = false;
	}
	
	return done;
}

int main()
{
    fstream in,out;
    in.open("largeinputB.txt",ios::in);
    out.open("largeoutputB.txt",ios::out);
    
    /*problem specific code starts here*/
    
    int N;
    in>>N;
    
    for(int i=0;i<N;i++)
    {
		int T, A, B, resa=0, resb=0;
		string a, b;
		
		in>>T;
		in>>A;
		in>>B;
		
		timer t;
		vt.clear();
		
		for(int j=0;j<A;j++)
		{
			in>>a>>b;
			vt.push_back(setit(a,b,1));
		}
		
		for(int j=0;j<B;j++)
		{
			in>>a>>b;
			vt.push_back(setit(a,b,2));
		}
		
		vt = sortit(vt);
		
		while(!assignt(T))
		{
			if(st==1)
				resa++;
			else
				resb++;
		}
		
		if(st==1)
			resa++;
		else
			resb++;
		
		out<<"Case #"<<i+1<<": "<<resa<<" "<<resb<<endl;
	}
    
    /*problem specific code ends here*/
    
    in.close();
    out.close();
    
    return 0;
}
