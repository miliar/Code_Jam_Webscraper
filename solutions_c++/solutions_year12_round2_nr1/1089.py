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

class KRush
{
public:

	void getstring()
	{
		int casenum;
		cin>>casenum;
		for(int ii=1;ii<=casenum;ii++)
		{
			double result=0;
			int N;
			cin>>N;
			vector<int> one,two,complete;
			int star=0;
			for(int i=1;i<=N;i++)
			{
				int t;
				cin>>t;
				one.push_back(t);
				cin>>t;
				two.push_back(t);
				complete.push_back(0);
			}
		   //初始化完成
			while(true)
			{
				bool flag=false;
				for(int i=0;i<=N-1;i++)
				{
					int t=two[i];
					if(t<=star && complete[i]==0)
					{
						
						star+=2;
						complete[i]=2;
						result++;
						flag=true;
						break;
					}
				}
				if(flag)
				{
					continue;
				}
				for(int i=0;i<=N-1;i++)
				{
					int t=two[i];
					if(t<=star && complete[i]==1)
					{
						
						star+=1;
						complete[i]=2;
						result++;
						flag=true;
						break;
					}
				}
				if(flag)
				{
					continue;
				}
				int maxtwo=-1;
				int pos=-1;
				for(int i=0;i<=N-1;i++)
				{
					int t=one[i];
					if(t<=star && complete[i]==0 && two[i]>maxtwo)
					{
						pos=i;
						maxtwo=two[i];
					}
				}
				if(maxtwo!=-1)
				{
					complete[pos]=1;
					star++;
					result++;
					flag=true;
				}
				if(flag==false)
				{
					break;
				}
			}
			bool flag=true;
			for(int i=0;i<=N-1;i++)
			{
				if(complete[i]!=2)
				{
					cout<<"Case #"<<ii<<": "<<"Too Bad"<<endl;
					flag=false;
					break;
				}
			}
			if(flag)
			{
			cout<<"Case #"<<ii<<": "<<result<<endl;
			}
		}

	}
};


class SIN
{
public:
	void getstring()
	{
		int casenum;
		cin>>casenum;
		for(int ii=1;ii<=casenum;ii++)
		{
			vector<double> result;
			int num;
			cin>>num;
			vector<long> score;
			long X=0;
			for(int i=1;i<=num;i++)
			{
				int j;
				cin>>j;
				score.push_back(j);
				X+=j;
				result.push_back(-1);
			}
			/*for(int i=0;i<=num-1;i++)
			{
				long m=getmin(score,i);

				result.push_back((double)(X+m-score[i])/(double)(2*X));
			}*/
			double mean=(double)((double)2*X/(double)num);
			for(int i=0;i<=num-1;i++)
			{
				
				if(score[i]>mean)
				result[i]=0;
			}
			mean=0;
			int sum=0;
			for(int i=0;i<=num-1;i++)
			{
				if(result[i]!=0)
				{
					sum++;
					mean+=score[i];
				}
			}
			mean=(mean+X)/sum;
			for(int i=0;i<=num-1;i++)
			{
				if(result[i]!=0)
				{
					result[i]=(double)(mean-score[i])/X;
				}
			}
			cout<<"Case #"<<ii<<": ";
			for(int i=0;i<=num-1;i++)
			{
				cout<<result[i]*100<<" ";
			}
			cout<<endl;
		}

	}
	long getmin(vector<long> score,int pos)
	{
		long m=999999999;
		
		for(int i=0;i<=score.size()-1;i++)
		{
			if(i!=pos && score[i]<m)
			{
				m=score[i];
			}
		}
		return m;
	}

};

int main()
{
	freopen("E:/in2.in","rt",stdin);
    freopen("E:/out.out","wt",stdout);
	SIN p;
	p.getstring();
	int i;
	cin>>i;
	return 0;
}