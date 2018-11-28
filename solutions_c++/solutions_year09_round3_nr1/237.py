#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;
typedef long long int64;

int main (int argc, char * const argv[]) {
    
	string WELC="welcome to code jam";
	
	fstream INP("input.txt",fstream::in);
	fstream OUT("output.txt",fstream::out);
		
	int T;
	INP>>T;
	
	for(int c=0;c<T;c++)
		{
		
		string s;
		INP>>s;
		
		int num=0;
		set<char> cont;
		for(int i=0;i<s.size();i++)
			cont.insert(s[i]);
		
		num=cont.size();
		
		vector<int64> m(s.size());
		
		map<char,int> corr;
		
		corr[s[0]]=1;
		int it=0;
		
		for(int i=0;i<s.size();i++)
			if(corr.find(s[i])!=corr.end())
				continue;
			else
				{
				corr[s[i]]=it;
				it++;
				if(it==1)
					it++;
				}
		
		for(int i=0;i<m.size();i++)
			m[i]=corr[s[i]];
		
		int64 risp=0;
		
		reverse(m.begin(),m.end());
		int64 k=1;
		
		if(num==1)
			num++;
		
		for(int i=0;i<m.size();i++)
			{
			risp+=k*m[i];
			k*=num;
			}
		
		OUT<<"Case #"<<c+1<<": "<<risp<<endl;
		
		}
		
		
	
	
    return 0;
}
