#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

const unsigned long  exp[10] = {1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000};
int N;
vector<string> Str;

string PreciseAdd(string a,string b)
{
	string::size_type len = a.size() > b.size()? a.size():b.size();
	string c(len,'0');
	string::size_type asize,bsize,csize;
	asize = a.size();
	bsize = b.size();
	for(string::size_type i = 0; i < asize / 2; i++)
	{
		swap(a[i],a[asize-1-i]);
	}
	for(string::size_type i = 0; i < bsize / 2; i++)
	{
		swap(b[i],b[bsize-1-i]);
	}
	if(len == a.size())
	{
		for(string::size_type i = 0; i < len - bsize; i++)
			b.push_back('0');
	}
	else
	{
		for(string::size_type i = 0; i < len - asize; i++)  // push_back会改变a.size()
			a.push_back('0');
	}
	char e = 0;//进位
	for(string::size_type i = 0; i < len; i++)
	{
		c[i] += a[i] + b[i] + e - 2 * '0';
		e = ( c[i] - '0' ) / 10;
		c[i] -= e * 10;
	}
	if(e > 0)
	{
		c.push_back(e+'0');
	}
	csize = c.size();
	for(string::size_type i = 0; i < csize / 2; i++)
	{
		swap(c[i],c[csize-1-i]);
	}
	return c;
}


string PreciseSub(string a,string b)  // 保证a>b
{
	string::size_type len = a.size();
	string::size_type e = 0;
	string c(len,'0');
	string::size_type asize, bsize, csize;
	asize = a.size();
	bsize = b.size();
	for(string::size_type i = 0; i < asize /2; i++)
	{
		swap(a[i],a[asize-1-i]);
	}
	for(string::size_type i = 0; i < bsize / 2; i++)
	{
		swap(b[i],b[bsize-1-i]);
	}
	for(string::size_type i = bsize; i < asize; i++)
	{
		b.push_back('0');
	}
	for(string::size_type i = 0; i < len; i++)
	{
		c[i] = a[i] - b[i] - e + '0';
		if(c[i] < '0')
		{
			e = 1;
			c[i] += 10;
		}
		else
		{
			e = 0;
		}
	}
	for(string::size_type i = len - 1; i > 0; i--)
	{
		if(c[i] == '0')
		{
			c.erase(i);
		}
		else
		{
			break;
		}
	}
	csize = c.size();
	for(string::size_type i = 0; i < csize / 2; i++)
	{
		swap(c[i] , c[csize-1-i]);
	}
	return c;
}

string mutipleString(string str,int num)
{
	int s = 9;
	string ret("0");
	for(s; num / exp[s] == 0 && s >= 0; s--);//s位数字
	string org(str);
	for(s; s>= 0; s--)
	{
		string s1(org);
		for(int i = 0; i < s; i++)
		{
			s1.push_back('0');
		}
		int time = num / exp[s];
		for(int i = 0; i < time; i++)
		{
			ret =  PreciseAdd(ret,s1);
		}
		num = num % exp[s];
	}
	return ret;
}
int compare(string a,string b)
{
	string::size_type lena = a.length();
	string::size_type lenb = b.length();
	if(lena > lenb)
		return 1;
	else
	{
		if(lena < lenb)
			return 0;
		else
		{
			if(a > b)
				return 1;
			else
				return 0;
		}
	}
}
string clearTheZeroAtFront(string str)
{
	string ret;
	bool bb = true;
	for(string::size_type i = 0; i < str.length(); i++)
	{
		if(bb && str[i] == '0')
		{
			continue;
		}
		else
		{
			bb = false;
			ret += str[i];
		}
	}
	if(ret.empty())
		ret = "0";
	return ret;
}
char numToChar(int num)
{
	char ret;
	ret = num + '0';
	return ret;
}
string  PreciseDivide(const string &val1,const string &val2, unsigned int base = 10)
{
	if(compare(val2,val1))
		return "0";
	string quotient;
	string dividend_part = val1.substr(0,val2.length()-1);
	string product_part;
	for(string::size_type index = val2.length() - 1; index < val1.length(); index++)
	{
		dividend_part += val1[index];
		dividend_part = clearTheZeroAtFront(dividend_part);
		unsigned int first = 0;
		unsigned int last = base;
		while(true)
		{
			unsigned int mid = (first + last) / 2;
			product_part = mutipleString(val2,mid);
			if(first == mid)
				break;
			
			if(compare(product_part,dividend_part) > 0)
			{
				last = mid;
			}
			else
			{
				first = mid;
			}
		}
		dividend_part = PreciseSub(dividend_part,product_part);
		quotient += numToChar(first);
	}
	quotient = clearTheZeroAtFront(quotient);
	return quotient;
}
string  PreciseMultiple(const string &val1,const string &val2)
{
	string ret("0");
	if(val1 == "0" || val2 == "0")
		return ret;
	int s;
	string::size_type len2 = val2.length();
	string org(val1);
	for(int i = 0; i < len2; i++)
	{
		s = len2 - i - 1;
		string s1(org);
		for(int j = 0; j < s; j++)
		{
			s1.push_back('0');
		}
		int time = val2[i] - '0';
		for(int j = 0; j < time; j++)
		{
			ret =  PreciseAdd(ret,s1);
		}
	}
	return ret;
}
string PreciseMod( string val1, string val2)
{
	string product;
	string chengshu;
	string ret;
	product = PreciseDivide(val1,val2, 10);
	chengshu = PreciseMultiple(val2,product);
	ret = PreciseSub(val1,chengshu);
	return ret;
}


void preprocess()
{
	string pattern;
	vector<string>::size_type len = Str.size();
	sort(Str.begin(),Str.end(),compare);
	vector<string> org(Str);
	Str.clear();
	Str.push_back(org[0]);
	pattern = org[0];
	for(vector<string>::size_type i = 1; i < len; i++)
	{
		if(org[i] == pattern)
		{
			continue;
		}
		else
		{
			Str.push_back(org[i]);
			pattern = org[i];
		}
	}
}
string gcdString(string a,string b)
{
	string c;
	if( b == "0")
		return a;
	else
	{
		c = PreciseMod(a,b);
		return gcdString(b,c);
	}
}
string solve()
{
	string::size_type n = Str.size();
	vector<string> cha;
	string t;
	vector<string>::size_type len;
	string gcd;
	string ret;
	for(string::size_type i = 0; i < n - 1; i++)
	{
		t = PreciseSub(Str[i],Str[i+1]);
		cha.push_back(t);
	}
	if(cha.empty())
		return "0";
	len = cha.size();
	if(len == 1)
	{
		gcd = cha[0];
	}
	else
	{
		gcd = cha[0];
		for(vector<string>::size_type i = 1; i < len ;i++)
		{
			if(compare(gcd,cha[i]))
			{
				gcd = gcdString(gcd,cha[i]);
			}
			else
			{
				gcd = gcdString(cha[i],gcd);
			}
		}
	}
	if(gcd == "1")
		return "0";
	if(compare(gcd,Str[n-1]))
	{
		ret = PreciseSub(gcd,Str[n-1]);
	}
	else
	{
		string bei;
		string r;
		bei = PreciseDivide(Str[n-1],gcd,10);
		r = PreciseSub(Str[n-1], PreciseMultiple(gcd,bei));
		if(r == "0")
			return "0";
		bei = PreciseAdd(bei,"1");
		r = PreciseMultiple(gcd,bei);
		ret = PreciseSub(r,Str[n-1]);
	}
	return ret;
}
int main()
{
	ifstream input("B-large.in");
	ofstream out("testlarge.out");
	int T;
	string temp;
	string result;
	input >> T;
	for(int i = 1; i <= T; i++)
	{
		input >> N;
		Str.clear();
		for(int j = 0; j < N; j++)
		{
			input >> temp;
			Str.push_back(temp);
		}
		preprocess();
		result = solve();
		out << "Case #" << i << ": " << result << endl;
	}
	return 0;
}