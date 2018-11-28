
#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <deque>
#include <list>
#include <vector>
#include <limits.h>
#include <string>

#define F(a) for(size_t i=0;i<a;++i)
#define FF(a) for(size_t j=0;j<a;++i)

using namespace std;

int main()	{
	ifstream in("fileAB.in");
	ofstream ou("fileAB.ou");
	size_t n,base,ind;
	unsigned __int64 uns;
	in>>n;
	for(size_t iii = 0;iii<n;iii++)	{
		string a;
		in>>a;
		map<char,int> cou;
		cou.clear();
		F(a.size())
			cou[a[i]] = -1;
		base=cou.size();
		cou[a[0]] = 1;
		if(a.find_first_not_of(a[0])<a.size())
			cou[a[a.find_first_not_of(a[0])]] = 0;
		if(base < 2)
			base = 2;
		if(base > 2)	{
			ind = 2;
			F(a.size())	{
				if(cou[a[i]] == -1)	{
					cou[a[i]] = (ind);
					ind++;
				}
			}
		}
		uns = 0;
		F(a.size())	{
			uns = uns*base + cou[a[i]];
		}
		ou<<"Case #"<<iii+1<<": "<<uns<<endl;
	}
	return 0;
}