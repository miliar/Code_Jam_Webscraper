// codejam.cpp : Defines the entry point for the console application.
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>


using namespace std;

typedef long long int64;
#define For(i,n) for (i=0;i<n;i++) 

int i,j,k,n,m,tests,t;

int main()
{
	ifstream inp("b-large.in");
	ofstream out("b-large.out");
	
	inp>>tests;
	For(t,tests)
	{
		out<<"Case #"<<t+1<<": ";
		string s,et_s;
		inp>>s;
		bool f = false;
		For(i,s.length()-1)
			if (s[i]<s[i+1])
				f = true;

		if (f)
		{
			//===
			//string z = s;
			//sort(z.begin(), z.end());
			//while (true)
			//{
			//	bool next = next_permutation(z.begin(), z.end());
			//	if (z==s){
			//		next_permutation(z.begin(), z.end());
			//		et_s = z;
			//		break;
			//	}

			//}

			//===
			//out<<et_s<<" ";
			string x="";
			for (i = s.length()-1; i>0; i--){
				x = x + s[i];
				if (s[i-1] < s[i]){
					sort(x.begin(), x.end());
					int pos = -1; 
					For(j,x.length())
						if (x[j]>s[i-1])
						{
							if (pos==-1)
								pos = j;
							else
								if (x[j]<x[pos])
									pos=j;
						}
						swap(x[pos],x[0]);
					x = x + s[i-1];
					sort(++x.begin(), x.end());
					
					For(j,i-1)
						out<<s[j];
					out<<x;
					
					break;
				}
			}

		}
		else {
			reverse(s.begin(), s.end());
			j=0;
			while (s[j]=='0') j++;
			swap(s[0],s[j]);
			out<<s[0]<<"0";
			For(i,s.length())
				if (i>0)
					out<<s[i];
		}


		out<<endl;
	}

	return 0;
}

