#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

class tTime
{
public:
	int d;
	int e;
	int s;
	void input(int h,int m)
	{
		d=h*60+m;
	}
	void input(string str)
	{
		int h,m;
		sscanf(str.c_str(),"%d:%d",&h,&m);
		input(h,m);
	}
	tTime(){};

	tTime(string str)
	{
		this->input(str);
	}
	tTime(int h,int m)
	{
		this->input(h,m);
	}
	tTime(int min)
	{
		d=min;
	}
	tTime operator + (int t)
	{
		tTime tt(t+this->d);
		return tt;
	}
	int operator - (tTime t)
	{
		return (this->d - t.d);
	}
	bool operator > (tTime t)
	{
		return this->d > t.d;
	}
	bool operator < (tTime t)
	{
		return this->d < t.d;
	}

};
bool cmp(tTime a,tTime b)
{
	if(a.d!=b.d)
		return (b.d)>(a.d);
	else
		if(a.e==1) return true;		
		else return false;
}
int qcmp(const void *x,const void *y)
{
	if(cmp(*(tTime*)x,*(tTime*)y)) return -1;
	else return 1;
}
int main()
{
	int T;
	int Ti=0;
	int turnaround;
	//	freopen("A-large.in","r",stdin);
	//	freopen("A-large.out","w",stdout);
	//freopen("C:\\Users\\SCat\\Documents\\Visual Studio 2005\\Projects\\pojcontest\\debug\\B-small.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d",&T);
	while(T--)
	{
		Ti++;
		int na,nb;
		tTime q[600];
		int c=0;
		scanf("%d",&turnaround);
		scanf("%d%d",&na,&nb);
		for(int i=0;i<na;i++)
		{
			string tstr1,tstr2;
			char tc[100];
			scanf("%s",tc);
			tstr1=tc;
			scanf("%s",tc);
			tstr2=tc;

			tTime tt;
			tt.input(tstr1);
			tt.e=-1;
			tt.s=0;
			q[c++]=tt;

			tt.input(tstr2);
			tt=tt+turnaround;
			tt.e=1;
			tt.s=1;
			q[c++]=tt;		
		}

		for(int i=0;i<nb;i++)
		{
			string tstr1,tstr2;
			char tc[100];
			scanf("%s",tc);
			tstr1=tc;
			scanf("%s",tc);
			tstr2=tc;

			tTime tt;
			
			tt.input(tstr1);
			tt.e=-1;
			tt.s=1;
			q[c++]=tt;


			tt.input(tstr2);
			tt=tt+turnaround;
			tt.e=1;
			tt.s=0;
			q[c++]=tt;
		}

		//sort(q,q+c,cmp);
		qsort(q,c,sizeof(q[0]),qcmp);

		int maxa=0,maxb=0;
		int train[2]={0};
		for(int i=0;i<c;i++)
		{
			train[q[i].s]+=q[i].e;
			maxa=max(maxa,-train[0]);
			maxb=max(maxb,-train[1]);			
		}
		printf("Case #%d: %d %d\n",Ti,maxa,maxb);
	}

	return 0;
}