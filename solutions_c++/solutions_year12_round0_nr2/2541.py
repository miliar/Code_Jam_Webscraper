
#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))
#define ABS(a) ((a)>(0))?(a):(a)


class CSolver
{
public:
	bool  virtual ReadData()
	{
		return false;
		//reading data
	};
	void  virtual Solve()
	{
		if (!ReadData())
			printf("error");
		
		printf("%f ","something");

	};
	
};

class AA
{
public:
	 AA()
	{
		mtran[0]='y';//a
		mtran[1]='h';//b
		mtran[2]='e';//c
		mtran[3]='s';//d
		mtran[4]='o';//e
		mtran[5]='c';//f
		mtran[6]='v';//g
		mtran[7]='x';//h
		mtran[8]='d';//i
		mtran[9]='u';//j
		mtran[10]='i';//k
		mtran[11]='g';//l
		mtran[12]='l';//m
		mtran[13]='b';//n
		mtran[14]='k';//o
		mtran[15]='r';//p
		mtran[16]='z';//q
		mtran[17]='t';//r
		mtran[18]='n';//s
		mtran[19]='w';//t
		mtran[20]='j';//u
		mtran[21]='p';//v
		mtran[22]='f';//w
		mtran[23]='m';//x
		mtran[24]='a';//y
		mtran[25]='q';//z
	};
	bool  virtual ReadData()
	{
		return false;
		//reading data
	};
	void   Solve()
	{
		char ch;
		do 
		{
			scanf("%c", &ch);
			if (ch==char(10))
			{
				  printf("\n");
				break;
			}
			if (ch==32)
				  printf(" ");
			if ((ch>=97) && (ch<=122))
				  printf("%c", mtran[ch-97]);

		}while(true);
		
	};
	
	char mtran[26];
	
};


class BB
{
public:
	bool  virtual ReadData()
	{
		scanf("%d", &A);
		scanf("%d", &B);
		return false;
		//reading data
	};
	void   Solve()
	{
		ReadData();
		 pairs=0;
		for (int n=A;n<B;n++)
		{
			pairs=pairs+HowManyRecycled(n,B);
		}
		  printf("%d", pairs);

	}
	int GetDigits(int n)
	{
		int idig=0;
		while(n>=1)
		{
			idig++;
			n=n/10;
		}
		return idig;
	}
	int HowManyRecycled(int n,int B)
	{
		int rec=0;
		int newn=n;
		int idig=GetDigits(n);
		for (int i=0;i<idig;i++)
			foundparis[i]=-1;
		for (int i=0;i<idig;i++)
		{
			int temp ;
			temp=pow(10.,idig-1);
			temp=temp*(newn%10);
			temp=temp+newn/10;
			newn=temp;
			if ((newn>n) && (newn<=B))
			{
				bool found=false;
				int j=0;
				while((found==false) && (foundparis[j]!=-1))
				{
					if (foundparis[j]==newn)
						{
							found=true;
							break;
						}
					j++;
				}
				if (found==false)
				{
					foundparis[j]=newn;
					rec++;
				//printf("%d- %d|%d\n ",pairs+rec, n,newn);
				}
			}
		}
		return rec;
	}
	int A,B;
	int pairs;
	int foundparis[10];

};
		
class CC
{
public:
	int googlers;
	int suprising;
	int P;
	int PNotSuprising;
	int PMaybeSuprising;
	bool  virtual ReadData()
	{
	
		return false;
		//reading data
	};
	void   Solve()
	{
		PNotSuprising=0;
		PMaybeSuprising=0;
		scanf("%d", &googlers);
		scanf("%d", &suprising);
		scanf("%d", &P);
		int ti;
		rep (i, googlers) {
			scanf("%d", &ti);
			if(ti<=0)
			{
				if (P==0)
					PNotSuprising++;
			}
			else
			{
				switch (ti%3)
				{	case 0:
					{
						if ((ti/3)>=P)
							PNotSuprising++;
						if ((ti/3)==(P-1))
							PMaybeSuprising++;
						break;
					}
					case 1:
					{
						if ((ti/3)>=(P-1))
							PNotSuprising++;
					
						break;
					}
					case 2:
					{
						if ((ti/3)>=(P-1))
							PNotSuprising++;
						if ((ti/3)==(P-2))
							PMaybeSuprising++;

						break;
					}
				}
			}
		}
		
			int temp=min(PMaybeSuprising,suprising);
			printf("%d", PNotSuprising+temp);

	}
	
};
int main(int argc, char ** argv) {
   int t;
    char c;
	CC solver;
   char endofline;
   scanf("%d", &t);
   scanf("%c", &endofline);
   rep (i, t) {
       printf("Case #%d: ", i+1);
	 
	   
	    solver.Solve();
		scanf("%c", &endofline);
       printf("\n");
   }
   return 0;
}