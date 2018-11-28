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

class pswpro
{
public:

	void getstring()
	{
		int casenum;
		cin>>casenum;
		for(int ii=1;ii<=casenum;ii++)
		{
			double result=0;
			int A,B;
			cin>>A>>B;
			vector<double> cor;
		
			for(int j=1;j<=A;j++)
			{
				double t;
				cin>>t;
				cor.push_back(t);
			}
			double d1=1;//继续输入
			for(int j=0;j<=cor.size()-1;j++)
			{
				d1*=cor[j];
			}
			d1=d1*(B-A+1)+(1-d1)*(B+1+B-A+1);
			double d2=B+2;//直接按enter
			vector<double> p;//前n个全对的概率
			vector<double> back;
			double t=1;
			for(int i=0;i<=A-1;i++)
			{
				t*=cor[i];
				p.push_back(t);
			}
		  for(int i=1;i<=A-1;i++)
		  {
			  double t=0;
			  t+=p[A-i-1]*(B-A+i+i+1)+(1-p[A-i-1])*(B-A+i+i+B+1+1);
			  back.push_back(t);
		  }
		  sort(back.begin(),back.end());
		  if(d1>d2)
		  {
			  d1=d2;
		  }
		  if(back.size()>0 && back[0]<d1)
		  {
			  d1=back[0];
		  }
		  result=d1;
			cout<<"Case #"<<ii<<": "<<result<<endl;
		}

	}
};



int main()
{
	freopen("E:/in1.in","rt",stdin);
  freopen("E:/out.out","wt",stdout);
	pswpro p;
	p.getstring();
	int i;
	cin>>i;
	return 0;
}