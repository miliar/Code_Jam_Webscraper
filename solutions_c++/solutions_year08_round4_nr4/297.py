//CODEJAM - D

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	//vars
	ifstream f ("D.in");
	ofstream g ("D.out");
	int t,tt,k,l,a,b,best,cur;
	string s,s2;
	int p[10];
	//testcase loop
	f >> tt;
		for (t=1; t<=tt; t++)
		{
			//input
			f >> k;
			f >> s;
			l=s.length();
			//try all :S
			best=9999;
				for (a=0; a<k; a++)
					p[a]=a;
				do
				{
					s2="";
						for (a=0; a<l; a+=k)
							for (b=0; b<k; b++)
								s2+=s[a+p[b]];
					cur=0;
					s2+='.';
						for (a=0; a<l; a++)
							if (s2[a]!=s2[a+1])
								cur++;
						if (cur<best)
							best=cur;
				}
				while (next_permutation(p,p+k));
			//output
			cout << "Case #" << t << ": " << best << endl;
			g << "Case #" << t << ": " << best << endl;
		}
	return(0);
}