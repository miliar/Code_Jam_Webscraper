#include<iostream>

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>



using namespace std;



class dwtg
{
public:

	void getstring()
	{
		int casenum;
		cin>>casenum;
		for(int ii=1;ii<=casenum;ii++)
		{
			string str;
			int N,S,P;
			vector<int> ti;
			cin>>N>>S>>P;
			for(int i=1;i<=N;i++)
			{
				int t;
				cin>>t;
				ti.push_back(t);
			}
			int result=0;
			for(int i=0;i<=N-1;i++)
			{
				int t=ti[i];
				if(t%3==1 )
				{
					if(t/3+1>=P)
					{
						result++;
					}
				}
				else if(t%3==0)
				{
					if(t/3>=P)
					{
						result++;
					}
					else if(t/3+1>=P && S>0 )
					{
						result++;
						S--;
					}
					
				}
				else
				{
					if(t/3+1>=P)
					{
						result++;
					}
					else if(t/3+2>=P && S>0 )
					{
						result++;
						S--;
					}
					
				}
			}
			cout<<"Case #"<<ii<<": "<<result<<endl;
		}

	}
};

class RecycledNumbers
{
public:
	string int2str(int a)
	{
		stringstream ss;
		ss<<a;
		string r;
		ss>>r;
		return r;
	}
	int str2int(string s)
	{
		stringstream ss;
		ss<<s;
		int a;
		ss>>a;
		return a;
	}
	string weiyi(string str,int a)
	{
		string re(str.c_str(),a,str.length()-a);
		string re1(str.c_str(),0,a);
		re.append(re1);
		return re;
	}
	void getstring()
	{
		int casenum;
		cin>>casenum;
		for(int ii=1;ii<=casenum;ii++)
		{
			int A,B;
			cin>>A>>B;
			int result=0;
			int len=int2str(A).length();
			if(len>1)
			{
				for(int i=A;i<=B;i++)
				{
					for(int j=1;j<=len-1;j++)
					{
						string str=weiyi(int2str(i),j);
						int n=str2int(str);
						if(n>i && n<=B)
						{
							result++;
						//	cout<<i<<" "<<n<<endl;;
						}
					}
				}
			}
			cout<<"Case #"<<ii<<": "<<result<<endl;
		}

	}
};

int main()
{
	freopen("E:/in.in","rt",stdin);
//	freopen("E:/out.out","wt",stdout);
	 RecycledNumbers *s=new  RecycledNumbers();
	s->getstring();
	return 0;
}