#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <deque> 
#include <string>

using namespace std;  

vector<string> tokenize(const string& str, const string& delimiters = " ")
{     
    vector<string> tokens;
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);     
    string::size_type pos  = str.find_first_of(delimiters, lastPos);
    
    while (string::npos != pos || string::npos != lastPos)
    {         
	tokens.push_back(str.substr(lastPos, pos - lastPos));         
	lastPos = s.find_first_not_of(delimiters, pos);        
	pos = s.find_first_of(delimiters, lastPos);
    }

    return tokens;
} 

string strdiff(string a, string b)
{
    if (lessthan(a, b))
	return '-' + strdiff(b, a);	

    deque<char> tmp;
    int isb = false;
    b.insert(0, a.size() - b.size(), '0');

    for (int i = b.size() - 1; i >= 0; --i)
    {
	int u = a[i] - '0';
	int v = b[i] - '0';
	if (isb)
	{
	    v = v + 1;
	}
	if (u < v)
	{
	    isb = true;
	    tmp.push_front(10 + u - v + '0');
	}
	else
	{
	    isb = false;
	    tmp.push_front(u - v + '0');
	}
    }	

    while (!tmp.empty() && (tmp.front() == '0'))
	tmp.pop_front();

    string res(tmp.begin(), tmp.end());	

    return res;		
} 

string strmod(string a, string b)
{
    if (a == b)
	return "";

    if (lessthan(a, b))
	return a;

    while (a.size() > b.size() + 1)
    {
	string tmp = b;
	tmp.insert(tmp.size(), a.size() - b.size() - 1, '0');
	a = strdiff(a, tmp);
    }

    while (lessthan(b, a))
    {
	a = strdiff(a, b);
    }

    if (a == b)
	return "";

    return a;
}


string gcd(string a, string b)
{	 
    if (lessthan(b, a))
        return gcd(b, a);

    if (a == "")
	return b;

    return gcd(strmod(b, a), a);
} 


string gcd(vector<string> arr)
{
    string res = arr[0];

    for (int i = 0; i < arr.size(); i++)
    {
	res = gcd(res, arr[i]);
    }

    return res;
} 

bool lessthan(string s1, string s2)
{
    if (s1.size() > s2.size())
	return false;

    if (s1.size() < s2.size())
	return true;
	
    return s1 < s2;	
}

int main()
{      
    int T;
    string s;
    ifstream inf("D:\\in.txt");
    ofstream out("D:\\out.txt");
    getline(inf, s);
    T = atoi(s.c_str()); 	 
	 
    for (int i = 0; i < T; ++i)
    {	
	cout << i << endl;
	string res;
	getline(inf, s);
	vector<string> str = tokenize(s);	
	int N = atoi(str[0].c_str());
	vector<string> t;
	for (int i = 0; i < N; ++i)
	    t.push_back((str[i + 1].c_str()));
	
	sort(t.begin(), t.end(), lessthan);
	string minv = t[0]; 

	vector<string> d;
	for (int i = 0; i < N; ++i)
	{
	    if (times[i] != minv)
		d.push_back(strdiff(t[i], minv));
	}		 
	string g = gcd(d);
	string r = strmod(m, g);
	res = strmod(strdiff(g, r), g);			

	if (res == "")
            res = "0";
	outf << "Case #" << i + 1 << ": " << res << endl;		
    } 

    return 1;
}  

 