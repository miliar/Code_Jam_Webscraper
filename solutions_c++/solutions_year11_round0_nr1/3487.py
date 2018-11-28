#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<cmath>

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

int process_testcaseA(string s)
{
	int rv = 0;
	istringstream iss(s);
	int n = 0;
	iss >> n;
	int O[101];
	int B[101];
	int opressedtime[101];
	int bpressedtime[101];
	for(int i = 0; i < 101; i++)
		O[i] = B[i] = opressedtime[i] = bpressedtime[i] = 0;
	for(int i = 0; i < n; i++)
	{
		char rob;
		int btn;
		iss >> rob >> btn;
		if('O' == rob)
		{
			O[i+1] = btn;
		}
		else
		{
			B[i+1] = btn;
		}
	}
	O[0] = B[0] = 1;

	long oprevtime = 0;
	long bprevtime = 0;
	long opos = 1;
	long bpos = 1;
	for(int i = 1; i <= n; i++)
	{
		long myprevtime, neededtime, begtime, endtime, hisprevtime;
		char me, prev;
		if(0 != O[i])
		{
			//printf("O %d ", O[i]);
			me = 'O';
			prev = (O[i-1] == 0)?'B':'O';
			myprevtime = oprevtime;
			hisprevtime = bprevtime;
			neededtime = abs(O[i] - opos) + 1;
			opos = O[i];
		}
		else
		{
			//printf("B %d ", B[i]);
			me = 'B';
			prev = (B[i-1] == 0)?'O':'B';
			myprevtime = bprevtime;
			hisprevtime = oprevtime;
			neededtime = abs(B[i] - bpos) + 1;
			bpos = B[i];
		}
		begtime = myprevtime;
		if(me == prev)
			endtime = neededtime + begtime;
		else
			endtime = max(neededtime + begtime, hisprevtime+1);
		if('O' == me)
			oprevtime = endtime;
		else
			bprevtime = endtime;
	}

	rv = max(oprevtime, bprevtime);

	return rv;
}

int main(int argc, const char *argv[])
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
		cout << process_testcaseA(s) << endl;
	}
	is.close();
	return 0;
}
