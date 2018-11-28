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

int main()
{
    fstream in,out;
    in.open("A-large.in",ios::in);
    out.open("A-large.out",ios::out);
    
    /*problem specific code starts here*/
    
    long long N;
    in>>N;
    
    for(int i=0;i<N;i++)
    {
		long long P,K,L,t,res=0;
		vector<long long> F;
		in>>P>>K>>L;
		
		for(int j=0;j<L;j++)
		{
			in>>t;
			F.push_back(t);
		}
		
		sort(F.begin(),F.end());
		reverse(F.begin(),F.end());
		
		for(int j=0;j<F.size();j++)
		{
			long long x = j/K;
			res += (x+1)*F[j];
		}
		
		out<<"Case #"<<i+1<<": "<<res<<endl; 
	}
    
    /*problem specific code ends here*/
    
    in.close();
    out.close();
    
    return 0;
}
