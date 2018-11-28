#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	int T,C,D,N;
	char c;
	ifstream in("input.txt");
	ofstream out("output.txt");	
	in>>T;
	for(int k=0; k<T; k++)
	{
		in>>C;
		vector<string> vc(C);
		for(int i=0; i<C; i++)
			in>>vc[i];

		in>>D;
		vector<string> vo(D);
		for(int i=0; i<D; i++)
			in>>vo[i];

		vector<int> va(26,0);

		string s="";
		in>>N;
		for(int i=0; i<N; i++)
		{
			in>>c;
			if (s.size()>0)
			{
				char _c=s[s.size()-1];
				bool flag=true;
				for(int j=0; flag && (j<C); j++)
				{
					if ((vc[j][0]==c)&&(vc[j][1]==_c)||(vc[j][0]==_c)&&(vc[j][1]==c))
					{
						flag=false;
						s[s.size()-1]=vc[j][2];
						va[_c-'A']=max(va[_c-'A']-1,0);
					}
				}
				if (flag)
				{
					s+=c;
					va[c-'A']++;
					for(int j=0; flag && (j<D); j++)
					{
						if ((va[vo[j][0]-'A']>0)&&(va[vo[j][1]-'A']>0))
						{
							flag=false;
							s="";
							fill(va.begin(),va.end(),0);
						}
					}
				}
			}
			else
			{
				s+=c;
				va[c-'A']++;
			}
		}
		
		string res="[";
		for(int i=0; i<(int)s.size()-1; i++)
		{
			res+=s[i];
			res+=", ";
		}
		if (s.size())
			res+=s[s.size()-1];
		res+="]";
		out<<"Case #"<<(k+1)<<": "<<res<<endl;
		
	}
	return 0;
}



