#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <sstream>
#include <ctype.h>
#include <queue>
#include <stack>
#include <fstream>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl;

template<class Item>
void display(vector<Item> v)
{
	for(int i=0; i<v.size(); i++)
		cout << v[i] << ' ';
	cout << '\n';
}

string out(__int64 n)
{
	string ret = "";
	string flag = n<0 ? "-" : "";
	n = n < 0 ? -n : n;
	do
	{	char c = (n%10) + '0';
		ret = c + ret;
		n /=10;
	}
	while(n);
	return flag + ret;
}
 
int main()
{

int G;
fstream In("a-large.in", ios::in);
fstream Out("a-large.out", ios::out);

In >> G;

for(int h=1; h<=G; h++)
{

int N;

In >> N;

int i, j;
vector<__int64> a(N), b(N);
int t;
for(i=0; i<N; i++)
{	In >> t; a[i]=t;
}

for(i=0; i<N; i++)
{	In >> t; b[i]=t;
}

sort(a.begin(), a.end() );
sort(b.begin(), b.end() );

__int64 ret = 0;

for(i=0; i<N; i++)
	ret += a[i]*b[N-1-i];

Out << "Case #" << h << ": " << out(ret) << endl;


}


In.close();
Out.close();
return 0;

}

