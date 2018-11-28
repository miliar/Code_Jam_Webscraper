//Source Code
//Code compiled and run in Microsoft Visual C++ 6.0
//Standard Libraries Used
//Append any character at the end of input file, before running this programme.

#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<math.h>
#include <set>
#include <queue>

//#include<cstdio>
//#include <cstdlib>
//#include <sstream>
//#include<cstdio>
//#include<cmath>

using namespace std;

#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const double pi = atan(1.0)*4.0;

//const double eps = 1e-8;
//typedef pair<int,int> pii;
//typedef long long ll;
//#define SZ(x) (int)(x.size())
//const int inf = 1000000009;

int main()
{
	   ifstream finput;
	   finput.open("F:/C-small.IN"); 
	   ofstream foutput("F:/ASmallOut.txt");		
	   
	   int numTests;					
	   char ch;
	   	   
	   finput>>numTests;

	   finput.get(ch);
	   while(isspace(ch))finput.get(ch);
	   finput.putback(ch);
	   
	   cout<<"num = "<<numTests<<endl;    
	
	   if(!finput.is_open())
	   {
		   cout<<"ERROR in opening input file";
		   return 1;
	   }

	
	   __int64 modulator = 1000000007;

	   for(int test =1;test <= numTests; test++)
	   {
		
		__int64 ans = 0;
		int n, m;
		__int64 X, Y, Z;
		finput>>n>>m;
		
		char *inp = new char [40];
		
		finput.get(ch);
		while(isspace(ch)) finput.get(ch);
		finput.putback(ch);

		finput.get(inp,40,' ');
		X = atoi(inp);
		finput.get(ch);
		while(isspace(ch)) finput.get(ch);
		finput.putback(ch);
		
		finput.get(inp,40,' ');
		Y = atoi(inp);
		finput.get(ch);
		while(isspace(ch)) finput.get(ch);
		finput.putback(ch);
				

		finput.get(inp,40,'\n');
		Z = atoi(inp);
		finput.get(ch);
		while(isspace(ch)) finput.get(ch);
		finput.putback(ch);
		
		int * A = new int[m];
		vector <__int64> speeds;
		vector <__int64> subSeq;
		speeds.resize(n);
		subSeq.resize(n);
		

		int i;
		F0(i,m)finput>>A[i];
		
		F0(i,n)
		{ 
			speeds[i] = A[i%m];
			A[i%m] = (X * A[i%m] + Y * (i + 1)) % Z;
		}

		F0(i,n) subSeq[i] = 1;

		for(i= n-1; i>= 0; i--)
		{
			subSeq[i] %= modulator;
			for(int j = (i - 1); j >= 0; j--)
			{
				if(speeds[j] < speeds[i])
					subSeq[j] += subSeq[i];
				subSeq[j] %= modulator;
			}
		}
		
		F0(i,n){ ans += subSeq[i];
				ans %= modulator;}
		/*
		itoa(ans,inp,10);
		cout<<inp<<endl;
*/
		long int answer = ans;

//		cout<<answer<<endl;
		
	foutput<<"Case #"<<test<<": "<<answer<<endl;
	  }

finput.close();
foutput.close();
return 0;
}

