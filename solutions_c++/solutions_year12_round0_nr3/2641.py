#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<cmath>
#include<map>

using namespace std;

#if 0
int process_testcase(string s)
{
	int rv = 0;
	istringstream iss(s);
	int n = 0;
	iss >> n;
	//string steps;
	//iss >> steps;
	//cout << "Num steps == " << n << endl;
	int curr = 0;
	int prev = 0;
	char Rcurr = ' ';
	char rob;
	int btn;
	int prevbtn = 1;
	iss >> rob >> btn;
	Rcurr = rob;
	curr = (btn-prevbtn)+1;
	prevbtn = btn;
	int Otot = 0;
	int Btot = 0;
	if(1 == n)
	{
		if('O' == Rcurr)
			Otot = curr;
		else
			Btot = curr;
		return max(Otot, Btot);
	}
	int Obtn = 1;
	int Bbtn = 1;
	prev = 0;
	for(int i = 1; i < n; i++)
	{
		char rob;
		int btn;
		iss >> rob >> btn;
		//cout << rob << " " << btn << endl;
		if(rob == Rcurr)
		{
			//printf("Moving robot %c from %d to %d", rob, prevbtn, btn);
			int ttt = btn - prevbtn;
			if(ttt < 0)
				ttt=-ttt;
			ttt+=1;
			prevbtn = btn;
			curr += ttt;
		}
		else
		{
			if(curr <= prev)
				curr = prev+1;
			if('O' == Rcurr)
			{
				Obtn = prevbtn;
				Otot += curr;
				prevbtn = Bbtn;
			}
			else
			{
				Bbtn = prevbtn;
				Btot += curr;
				prevbtn = Obtn;
			}
			prev = curr - prev;
			curr = 0;
			int ttt = btn - prevbtn;
			if(ttt < 0)
				ttt=-ttt;
			ttt+=1;
			prevbtn = btn;
			curr += ttt;
			//printf("Moving robot %c from %d to %d", rob, prevbtn, btn);
		}
	}
	
	if(curr <= prev)
		curr = prev+1;
	if('O' == Rcurr)
	{
		Otot += curr;
	}
	else
	{
		Btot += curr;
	}
	rv = max(Otot, Btot);
	return rv;
}

#endif // 0

int process_testcaseC(string s, string ss)
{
	int rv = 0;
	
	istringstream is(s);
	int n = 0;
	is >> n;
	istringstream iss(ss);
	
	long minnum = 1000002L;
	long tot = 0;
	long samsum = 0;
	
	for(int i = 0; i < n; i++)
	{
		long num;
		iss >> num;
		minnum = min(minnum, num);
		samsum ^= num;
		tot += num;
	}
	
	if(samsum != 0)
		rv = -1;
	else
		rv = tot-minnum;
	return rv;
}

int mainC(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("ttt.txt");
	else
		is.open(argv[1]);
	
	
	// find total number of testcases
	string s;
	getline(is,s); 
	istringstream iss(s);
	iss >> tc;
	//printf("num tc == %d\n", tc);
	
	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ",i);
		getline(is,s);
		string ss;
		getline(is,ss);
		int rv = process_testcaseC(s, ss);
		if(-1 == rv)
			cout << "NO" << endl;
		else
			cout << rv << endl;
	}
	is.close();
	return 0;
}

int process_testcaseC(string s)
{
	int rv = 0;
	istringstream iss(s);
	int a,b;
	iss >> a >> b;
	int numdigits = 0;
	int multiplier = 1;
	int x = a;
	map<string, int>found;

	while(x)
	{
		numdigits++;
		x/=10;
		multiplier *= 10;
	}
	
	for(int n = a; n <= b; n++)
	{
		int m = n;
		int ttt = 10;
		for(int times = numdigits-1; times > 0; times--, ttt*=10)
		{
			int rem = n%ttt;
			m=n/ttt;
			m+=(rem*(multiplier/ttt));

			if( (m <= n) || (m>b) )
				continue;
			else
			{
				std::string z;
				std::stringstream outz;
				outz << n << "," << m;
				z = outz.str();
				if(found.end() == found.find(z))
				{
					found[z] = 1991;
					rv++;
				}

			}
		}
	}
	
	return rv;
}

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("inp.txt");
	else
		is.open(argv[1]);
	
	
	// find total number of testcases
	string s;
	getline(is,s); 
	istringstream iss(s);
	iss >> tc;
	//printf("num tc == %d\n", tc);
	
	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ",i);
		getline(is,s);
		cout << process_testcaseC(s) << endl;
	}
	is.close();
	return 0;
}
