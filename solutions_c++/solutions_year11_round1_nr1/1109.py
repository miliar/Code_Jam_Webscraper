#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define clr(x) memset((x), 0, sizeof(x))

int T;
void fun(int p,int q,int& f1,int& f2)
{
	for(int i = p; i > 1; i--)
	{
		if(p%i == 0 && q%i == 0)
		{
			f1 = p/i;
			f2 = q/i;
			fun(f1,f2,f1,f2);
		}
	}
}
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt5.in","r",stdin);freopen("A-small-attempt5.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
//	freopen("test.txt","r",stdin);freopen("test.out","w",stdout);
//  for(i = 0; i < T; i++)
	int i,j;
	long long N;
	vi Nd;
	int PD,PG;
	double dd = 1e-8;
	int possible;
	int f1D,f2D;
	cin>>T;
	for(int caseID = 1; caseID <= T; caseID++)
	{
		cin>>N>>PD>>PG;
		
		Nd.clear();
		cout<<"Case #"<<caseID<<": ";
		possible = 0;
		if(PG == 100 || PG == 0)
		{
			if(PD == PG)
				cout<<"Possible"<<endl;
			else
				cout<<"Broken"<<endl;
			continue;

		}
		if(PD == 100 || PD == 0)
		{
			if(PD == PG)
				cout<<"Possible"<<endl;
			else
				cout<<"Broken"<<endl;
			continue;
		}

//		PD /= 100;
//		PG /= 100;
		f1D = PD;
		f2D = 100;
		fun(PD,100,f1D,f2D);
		if(f2D <= N)
			possible = 1;
		//for(int i = 1; f1D*i <= N; i++)
		//{
		//	possible = 1;
		//	/*if(i == 0)
		//	{
		//		if(PG < dd)
		//		{
		//			Nd.push_back(0);
		//			possible = 1;
		//		}

		//	}
		//	else if(i*PD - (int)(i*PD) < dd)
		//	{
		//		Nd.push_back(i);
		//		possible = 1;
		//	}*/
		//}
		//if(possible)
		//{
		//	double dtmp;
		//	possible = 0;
		//	for(int j = 0; j < Nd.size(); j++)
		//	{
		//		if(Nd.at(j) == 0)
		//		{
		//			if(PG < dd)
		//			{
		//				possible = 1;
		//				break;
		//			}
		//		}
		//		else
		//		{
		//			dtmp = ( Nd.at(j)*PG + (int)(Nd.at(j)*PD) )/(1-PG);
		//			if(dtmp - (int)dtmp < dd)
		//			{
		//				possible = 1;
		//				break;
		//			}
		//		}
		//	}	
		//}
		if(PG != 100)
		{
			if(possible)
				cout<<"Possible";
			else
				cout<<"Broken";
			cout<<endl;
		}
	}
	return 0;
}