#include<iostream>
#include<sstream>
#include<map>
#include<ctime>
using namespace std;

stringstream ss;
string text, m_text;
map<string, bool> record;

multimap<long, long> dict;
multimap<long, long>::iterator it;
pair<multimap<long, long>::iterator, multimap<long, long>::iterator> ret;

int init_n(long n)
{
	if(n<=10) return 0;
	const long b = 2000000;
	
	long i, l, m;
	
	ss.clear();
	ss<<n;
	ss>>text;
	l=text.length();
	record.clear();
	for(i=1;i<l;i++)
	{
		m_text=text.substr(l-i, i)+text.substr(0, l-i);
		if(m_text[0]=='0') continue;
		ss.clear();
		ss<<m_text;
		ss>>m;
		if(m>n && m<=b)
		{
			if(record.find(m_text) != record.end()) continue;
			
			dict.insert(pair<long, long>(n, m));
			
			record[m_text] = 1;
		}
	}
	return record.size();
}

void init()
{
	long i;
	dict.clear();
	for(i = 1; i <= 2000000; i++)
		init_n(i);
}

int check_n(long n, long b)
{
	int i = 0;
	ret = dict.equal_range(n);
	for(it = ret.first; it != ret.second; it++)
		if((long)(*it).second <= b) i++;
	
	return i;
}

int main()
{
	//clock_t time_s = clock();
	int n, m;
	long a, b, i, j;
	
	init();
	
	cin >> n;
	for(m = 1; m <= n; m++)
	{
		cin >> a >> b;
		j = 0;
		for(i = a; i <= b; i++)
			j += check_n(i, b);
		cout << "Case #" << m << ": " << j << endl;
	}
	//cout << (clock()-time_s)/CLOCKS_PER_SEC/60 << endl;
}
