#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<list>
#include<stdio.h>
#include<sstream>
#include<set>
#include<deque>
#include<cmath>
#include<numeric>
#include<fstream>

using namespace std;

typedef long long LInt;
typedef vector<int> intvec;
typedef vector<intvec> intvec2;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define FOR(i,k,n) for (int i=(k); i<(int)(n); ++i)
#define DEC(i,k) for (int i=(k); i>=0; --i)
#define FORIT(i,c) for (decltype((c).begin())i=(c).begin();i!=(c).end();++i)

/////////////////////////
//#define fin cin
//#define fout cout
////////////////////////

int main()
{
	ifstream fin("E:\\Buid\\Algorithm\\GoogleJam\\2011Qualification\\B-large.in");
	ofstream fout("E:\\Buid\\Algorithm\\GoogleJam\\2011Qualification\\B-large.out");
	int T;
	int C,D,N;
	map<string,char> CList;
	set<string> DList;

	map<string,char>::iterator Citor;
	set<string>::iterator Ditor;

	string ans;

	fin>>T;

	REP(TEST,T)
	{
		ans.clear();
		CList.clear();
		DList.clear();
		
		fin>>C;
		REP(i,C)
		{
			char a,b,c;
			fin>>a>>b>>c;
			string temp = "";
			temp+=a;
			temp+=b;
			CList[temp]=c;
			temp="";
			temp+=b;
			temp+=a;
			CList[temp]=c;
		}

		fin>>D;
		REP(i,D)
		{
			char a,b;
			fin>>a>>b;
			string temp="";
			temp+=a;
			temp+=b;
			DList.insert(temp);
			temp="";
			temp+=b;
			temp+=a;
			DList.insert(temp);
		}

		fin>>N;
		REP(i,N)
		{
			string temp = "";
			char now;
			fin>>now;
here:			if(ans.size()==0)
			{
				ans.push_back(now);
			}
			else
			{
				temp+=now;
				temp+=ans[ans.size()-1];
				Citor = CList.find(temp);
				if(Citor!=CList.end())
				{
					ans.pop_back();
					now=(*Citor).second;
					goto here;
				}

				int j;
				bool nde = true;
				for(j = 0;j<ans.size();++j)
				{
					temp = "";
					temp+=now;
					temp+=ans[j];
					Ditor = DList.find(temp);
					if(Ditor!=DList.end())
					{
						ans.clear();
						nde = false;
						break;
					}
				}
				if(nde)
					ans.push_back(now);
			}
		}

		fout<<"Case #"<<TEST+1<<": [";
		REP(i,ans.size()-1)
		{
			fout<<ans[i]<<", ";
		}
		if(ans.size()>0)
			fout<<ans[ans.size()-1]<<"]"<<endl;
		else
			fout<<"]"<<endl;
	}
	
	system("pause");
	return 0;
}