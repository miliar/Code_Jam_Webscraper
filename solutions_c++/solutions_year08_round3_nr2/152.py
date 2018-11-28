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

vector<int> vi;
string s;
long long ugly;

long long calc()
{
	long long res = 0;
	long long temp = s[0]-'0';
	long long old = 1;
	for(long long i=0;i<s.size()-1;i++)
		if(vi[i] == 0)
			temp = temp*10 + (s[i+1]-'0');
		else
		{
			if(old == 1)
				res = res + temp;
			else
				res = res - temp;
				
			temp = s[i+1]-'0';
			old = vi[i];
		}
		
	if(old == 1)
		res = res + temp;
	else
		res = res - temp;
	
	return res;
}

bool isugly(long long n)
{
	if(n%2==0 || n%3==0 || n%5==0 || n%7==0)
		return true;
	return false; 
}

void go(int x)
{
	if(x == s.size()-1)
	{
		long long v = calc();
		
		if(isugly(v))
			ugly++;
		return;
	}
	
	vi.push_back(0);
	go(x+1);
	vi.pop_back();
	
	vi.push_back(1);
	go(x+1);
	vi.pop_back();
	
	vi.push_back(2);
	go(x+1);
	vi.pop_back();
}

int main()
{
    fstream in,out;
    in.open("B.in",ios::in);
    out.open("B.out",ios::out);
    
    /*problem specific code starts here*/
    
    long long N;
    in>>N;
    
    for(long long i=0;i<N;i++)
    {
		vi.clear();
		ugly = 0;
		s = "";
		
		in>>s;
		
		go(0);
		
		out<<"Case #"<<i+1<<": "<<ugly<<endl; 
	}
    
    
    /*problem specific code ends here*/
    
    in.close();
    out.close();
    
    return 0;
}
