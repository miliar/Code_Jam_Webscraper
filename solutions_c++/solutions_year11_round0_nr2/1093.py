#include<cstdio>
#include <cctype>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include <deque>
#include <math.h>
#include<stdio.h>
#include<memory.h>
using namespace std;


typedef stringstream ss;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long int64;

#define PI 3.14159265
#define pb push_back
#define ALL(t) t.begin(),t.end()
#define FORnm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000
struct Opps
{
 	char one;
	char two;		 
};
struct Change
{
   string a;
	 char   b; 			 
};
int main()
{
//	freopen("B-small-attempt1.in", "r", stdin);
//	freopen("respuestaS.out", "w+", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("respuestaL.out", "w+", stdout);

	int i, j, tc,T,C,D,N;
	int cnt;
  string str,strtemp;
  deque<char> A;
  vector<Opps> Op;
  vector<Change> Vals;
  cin	>> T;
	FORnm(tc,1,T)
	{
		cin >> C;
		A.clear();
		Vals.clear();
		Op.clear();
		forn(i,C)
		{
		  cin >> str;
		  Change ctemp;
			ctemp.a=str.substr(0,2);
			ctemp.b=str[2];
			Vals.pb(ctemp);
			ctemp.a=str.substr(1,1)+str.substr(0,1);
			ctemp.b=str[2];
			Vals.pb(ctemp);

		}
		cin >> D;
		forn(i,D)
		{
		  cin >> str;
			Opps temp;
			temp.one=str[0]; 				 
			temp.two=str[1];
			Op.pb(temp);
		}
		cin >> N >> str;
		forn(i,N)
		{
	    A.pb(str[i]); 	
		 	if(A.size()>1)
		 	{
			 strtemp=A[A.size()-2];
			 strtemp+=A[A.size()-1];
			 forn(k,Vals.size())
			   if(Vals[k].a==strtemp)
				 		 {
						 	A[A.size()-2]=Vals[k].b;															
						 	A.pop_back();						 	
		          break;
							 }
				
				int amin=MAXIMO,amax=-MAXIMO;
				bool erase=false;
				
				  FORnm(ll,0,A.size()-1)
							{
				   				forn(r,D)
									 if( (Op[r].one==A[A.size()-1] && Op[r].two==A[ll] ) || (Op[r].two==A[A.size()-1] && Op[r].one==A[ll] )  ) 
									  { amin=ll;
						          amax=A.size()-1;
						          erase=true;
						          A.clear();
										 	break;
										}
						  }

		  }
		}
		
		// print cases
		if(A.size()>0)
		{
		 cout<<"Case #"<<tc<<": [";
		 forn(i,A.size()-1) cout<<A[i]<<", ";
		 cout<<A[A.size()-1];
		 cout<<"]"<<endl;
		 }
		 else
		  cout<<"Case #"<<tc<<": []"<<endl;
	}
	return 0;
}

