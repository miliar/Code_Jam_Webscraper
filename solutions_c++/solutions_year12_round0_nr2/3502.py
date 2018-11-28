#include<iostream>

using namespace std;
int m1(int point)
{
	if(point%3==0)return point/3;
	//if(point%3==1)
	return point/3+1;
	//return point/3+1;
}
int m2(int point)
{
	if(point%3==2)return point/3+2;
	return point/3+1;
}
bool possible(int point)
{
	if(point < 2)return false;
	return true;
}
void solve(int num)
{
	int res = 0;
	int N, S, p;
	int pts[120], pos1[120],pos2[120];//pos1 czy bez wyjatkowego, pos2 czy z wyjatkowym
	cin>>N>>S>>p;
	for(int i=0;i<N;i++)
	{
		cin>>pts[i];
		if(m1(pts[i]) >= p)res++;
		else if(possible(pts[i]) && m2(pts[i]) >= p && S > 0)
		{
			res++;
			S--;
		}
	}
	cout<<"Case #"<<num<<": "<<res<<endl;
}
void brutesolve(int num)
{
	int mres = 0;
	int N, S, p;
	int pts[120], pos1[120],pos2[120];//pos1 czy bez wyjatkowego, pos2 czy z wyjatkowym
	cin>>N>>S>>p;
	for(int i=0;i<N;i++)
	{
		cin>>pts[i];
	}
	if(N==3)
	{
		if(S==2)
		{
			int res = 0;
			if(m2(pts[0])>=p)res++;
			if(m2(pts[1])>=p)res++;
			if(m1(pts[2])>=p)res++;
			if(!(possible(pts[0]) && possible(pts[1])))res = 0;
			mres = max(res,mres);
			res = 0;
			if(m2(pts[0])>=p)res++;
			if(m1(pts[1])>=p)res++;
			if(m2(pts[2])>=p)res++;
			if(!(possible(pts[0]) && possible(pts[2])))res = 0;
			mres = max(res,mres);
			res = 0;
			if(m1(pts[0])>=p)res++;
			if(m2(pts[1])>=p)res++;
			if(m2(pts[2])>=p)res++;
			if(!(possible(pts[2]) && possible(pts[1])))res = 0;
			mres = max(res,mres);
		}
		if(S==1)
		{
			int res = 0;
			if(m2(pts[0])>=p)res++;
			if(m1(pts[1])>=p)res++;
			if(m1(pts[2])>=p)res++;
			if(!(possible(pts[0])))res = 0;
			mres = max(res,mres);
			res = 0;
			if(m1(pts[0])>=p)res++;
			if(m2(pts[1])>=p)res++;
			if(m1(pts[2])>=p)res++;
			if(!(possible(pts[1])))res = 0;
			mres = max(res,mres);
			res = 0;
			if(m1(pts[0])>=p)res++;
			if(m1(pts[1])>=p)res++;
			if(m2(pts[2])>=p)res++;
			if(!(possible(pts[2])))res = 0;
			mres = max(res,mres);
		}
		if(S==0)
		{
			int res = 0;
			if(m1(pts[0])>=p)res++;
			if(m1(pts[1])>=p)res++;
			if(m1(pts[2])>=p)res++;
			mres = max(res,mres);
		}
		if(S==3)
		{
			int res = 0;
			if(m2(pts[0])>=p)res++;
			if(m2(pts[1])>=p)res++;
			if(m2(pts[2])>=p)res++;
			if(!(possible(pts[0]) &&possible(pts[2]) && possible(pts[1])))res = 0;
			mres = max(res,mres);
		}
	}
	if(N==2)
	{
		if(S==0)
		{
			int res = 0;
			if(m1(pts[0])>=p)res++;
			if(m1(pts[1])>=p)res++;
// 			if(m1(pts[2])>=p)res++;
			mres = max(res,mres);
		}
		if(S==1)
		{
			int res = 0;
			if(m2(pts[0])>=p)res++;
			if(m1(pts[1])>=p)res++;
			if(!(possible(pts[0])))res = 0;
			mres = max(res,mres);
			res = 0;
			if(m1(pts[0])>=p)res++;
			if(m2(pts[1])>=p)res++;
			if(!(possible(pts[1])))res = 0;
// 			if(m1(pts[2])>=p)res++;
			mres = max(res,mres);
		}
		if(S==2)
		{
			int res = 0;
			if(m2(pts[0])>=p)res++;
			if(m2(pts[1])>=p)res++;
			if(!(possible(pts[0]) && possible(pts[1])))res = 0;
			mres = max(res,mres);
		}
	}
	if(N==1)
	{
		if(S==0)
		{
			int res = 0;
			if(m1(pts[0])>=p)res++;
			mres = max(res,mres);
		}
		if(S==1)
		{
			int res = 0;
			if(m2(pts[0])>=p)res++;
			if(!(possible(pts[0])))res = 0;
			mres = max(res,mres);
		}
	}
	cout<<"Case #"<<num<<": "<<mres<<endl;

}
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		solve(i+1);
	}
}