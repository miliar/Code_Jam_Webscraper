#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <sstream>
#include <cmath>
#include <iostream>
#include <cstdlib>

//#define  INFILE  "B-small-attempt0.in"
//#define OUTFILE  "B-small-attempt0.out"

#define  INFILE  "B-large.in"
#define OUTFILE  "B-large.out"

using namespace std;


int to_m(string s)
{
	int m=0;
	m=((s[0]-'0')*10+(s[1]-'0'))*60+(s[3]-'0')*10+(s[4]-'0');
	return m;
}

template <typename T1, typename T2, typename T3>	
class tri
{
	template <typename Ty1, typename Ty2, typename Ty3>
	friend 	ostream& operator<<(ostream& os,const tri<Ty1,Ty2,Ty3>& t);
	public:
		T1 first;
		T2 second;
		T3 third;
	
};

template <typename Ty1, typename Ty2, typename Ty3>
ostream& operator<<(ostream& os,const tri<Ty1,Ty2,Ty3>& t)
{
	os<<"("<<t.first<<", "<<t.second<<", "<<t.third<<")";
	return os;	
}

class comp
{
	public:
		bool operator()(const tri<int,int, int> p1,const tri<int, int, int> p2)
		{
			if(p1.first<p2.first)
			{
				return true;
			}			
			else if(p1.first==p2.first&&p1.second<p2.second)
			{			
				return true;
			}
			else if(p1.first==p2.first&&p1.second==p2.second&&p1.third<p2.third)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
};



class T
{
	public:
		template<typename T> static void print(const string name, const T value)
		{
			cout << name<<": " <<value<<endl;
		}
		
		template<typename T> static void print(const string name, const vector<T> v)
		{
			cout<<name<<": ";
			for(int i=0;i<v.size();++i)
			{
				cout<<v[i]<<(i==v.size()-1 ? "\n":" ");
			}
		}
		
		template<typename T> static void 
		print(const string name, const vector<vector<T> > v)
		{
			cout<<name<<":"<<endl;
			for(int i=0;i<v.size();++i)
			{
				for(int j=0;j<v[i].size();++j)
				{
					cout<<v[i][j]<<(j==v[i].size()-1 ? "\n":" ");
				}
			}		
		}		
};

	
int main()
{
	ifstream fin(INFILE);
	ofstream fout(OUTFILE);
	if(!fin)cout << "can't open input file!"<<endl;
	if(!fout)cout<< "can't creat output file!"<<endl;
{
	int N;
	fin>>N;
	for(int i=1;i<=N;++i)
	{
		int T,NA,NB;
		fin>>T>>NA>>NB;
		vector<tri<int,int,int> > v(NA+NB);
		for(int j=0;j<NA;++j)
		{
			string s;
			fin>>s;
			v[j].first=to_m(s);
			fin>>s;
			v[j].second=to_m(s)+T;
			v[j].third=0;
		}

		for(int j=NA;j<NA+NB;++j)
		{
			string s;
			fin>>s;
			v[j].first=to_m(s);
			fin>>s;
			v[j].second=to_m(s)+T;
			v[j].third=1;
		}
		
		sort(v.begin(),v.end(),comp());
			
		vector<int> cnt(2);		
		while(v.size()!=0)
		{
//			T::print("v",v);
			tri<int,int,int> tmp;
			vector<tri<int,int,int> >::iterator it=v.begin();
			++cnt[it->third];
			tmp=*it;
			v.erase(it);
			for(it=v.begin();it!=v.end();)
			{
				if(it->third!=tmp.third&&tmp.second<=it->first)
				{
					tmp=*it;
					it=v.erase(it);
				}
				else
				{
					++it;
				}			
			}	
		}
		
		fout<<"Case #"<<i<<": "<<cnt[0]<<" "<<cnt[1]<<endl;	
	}	
	
}	
	fin.close();
	fout.close();
	system("pause");
	
	return 0;
}
