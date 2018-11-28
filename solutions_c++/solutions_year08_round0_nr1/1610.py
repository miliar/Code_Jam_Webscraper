//program framework generated with WishingBone's parser :)-
//common header
#ifdef WIN32
#	pragma warning(disable:4786)
#	define for if (0); else for
#endif
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

//64 bit integer definition
#ifdef WIN32
#define in_routine(type,spec) \
istream& operator>>(istream& s,type &d){char b[30];s>>b;sscanf(b,spec,&d);return s;}
#define out_routine(type,spec) \
ostream& operator<<(ostream& s,type d){char b[30];sprintf(b,spec,d);s<<b;return s;}
typedef signed __int64 i64; in_routine(i64,"%I64d") out_routine(i64,"%I64d")
typedef unsigned __int64 u64; in_routine(u64,"%I64u") out_routine(u64,"%I64u")
#define long long signed __int64;
#else
typedef signed long long i64;
typedef unsigned long long u64;
#endif

//common routines
#ifdef WIN32
#define min(a,b) _cpp_min(a,b)
#define max(a,b) _cpp_max(a,b)
#endif
#define abs(a) ((a)>0?(a):-(a))
#define s2d(s,d) istringstream(s)>>d
#define d2s(d,s) {ostringstream t;t<<d;s=t.str();}
int gcd(int a,int b){for(int c;b;c=a,a=b,b=c%b);return a;}
int lcm(int a,int b){return a/gcd(a,b)*b;}
template <class T>
void remove(vector<T>& v,const T&e){
	v.resize(remove(v.begin(),v.end(),e)-v.begin());
}

//output routine
ostream& operator<<(ostream& s,string d){
	s<<'\"'<<d.c_str()<<'\"';
	return s;
}
template <class T>
ostream& operator<<(ostream& s,vector<T> d){
	s<<"{";
	for (typename vector<T>::iterator i=d.begin();i!=d.end();i++)
		s<<(i!=d.begin()?",":"")<<*i;
	s<<"}";
	return s;
}

//parsing routine
template <class T>
vector<basic_string<T> > parse(const basic_string<T> &s,const basic_string<T> &delim){
	vector<basic_string<T> > ret(0);
	for (int b,e=0;;ret.push_back(s.substr(b,e-b)))
		if ((b=s.find_first_not_of(delim,e))==(e=s.find_first_of(delim,b)))
			return ret;
}
vector<int> intparse(const string &s,const string &delim=" \t\n"){
	vector<string> tmp=parse(s,delim);
	vector<int> ret(0);
	for (vector<string>::iterator i=tmp.begin();i!=tmp.end();i++)
		{int t;s2d(*i,t);ret.push_back(t);}
	return ret;
}

//name mapper
class mapper{
public:
	map<string,int> m;
	vector<string> v;
	void reset(){
		v.clear();
		m.clear();
	}
	int size(){
		return v.size();
	}
	int get(string str){
		if (m.find(str)==m.end()){
			m[str]=v.size();
			v.push_back(str);
		}
		return m[str];
	}
	string get(int i){
		return v[i];
	}
};


int main()
{
	ofstream out("xx.out",ios::binary);
	ifstream in("A-large.in",ios::binary);
	int test_cases,tc,i,j,k,state_num;
	int SeNum,QueryNum,SwNum;
	string str;
	in>>test_cases;
	vector<string> SearchEngin;
	vector<bool> SeState;
	for(tc=0;tc<test_cases;tc++)
	{
		SeState.clear();SearchEngin.clear();
		in>>SeNum;
		getline (in,str);
		for (i=0;i<SeNum;i++)
		{
			getline (in,str);
			SearchEngin.push_back(str);
			SeState.push_back(true);
		}
		for (i=0;i<SeNum;i++)
		{
	//		cout<<SearchEngin[i]<<endl;
		}
		state_num = 0;
		SwNum = 0;
		in>>QueryNum;
		getline (in,str);
		for (j=0;j<QueryNum;j++)
		{
			getline (in,str);
//			cout<<str<<endl;
			string tmp = str;
			for (i=0;i<SeNum;i++)
			{
				if (SeState[i]&&(tmp==SearchEngin[i]))
				{
	
					if (state_num==SeNum-1)
					{
						for (k=0;k<SeNum;k++)
							SeState[k]=true;
						state_num = 1;
						SwNum ++;
					}												
					else 
						state_num++;
					SeState[i]=false;
				}
			}
		}
		out<<"Case #"<<tc+1<<": "<<SwNum<<endl;
	}
	return 0;
}