#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
#define LET(x,a) typeof(a)x(a)
#define FOR(i,a,n) for(LET(i,a);i<n;++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define cs c_str()
#define GI ({int t; scanf("%d",&t); t;})
#define EACH(it,v) for(LET(it,v.begin()); it!=v.end(); ++it)
#define dbg(x) (cout << #x << ":" << (x) << "\t")
#define dbge(x) (dbg(x), cout << endl)

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
	//INPUT
	
  	clock_t start=clock();
	//ACTUAL PROGRAMMING STARTS HERE
	
	int kases; fin>>kases;
	REP(kase, kases)
	{
		string s = "";
		fin>>s;
		
		vector<int> v;
		REP(i, s.sz)v.pb(s[i]-'0');
	
		string str = s;
		if(next_permutation(v.begin(), v.end()))
		{
			REP(i,v.sz)str[i] = (char)(v[i]+'0');
		}
		else
		{
			sort(v.begin(), v.end());
			string zeros="0";
			str="";
			REP(i,v.sz)if(v[i]!=0)str+= (char)(v[i]+'0'); else zeros += "0";
			str = str.substr(0,1) + zeros + str.substr(1);
			
		}
		
		fout<<"Case #"<<(kase+1)<<": "<<str<<endl;
	}
	
	//END OF PROG
	clock_t end=clock();
	cout <<"Time: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
	
	return 0;
}
