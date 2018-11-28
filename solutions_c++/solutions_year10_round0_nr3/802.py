#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<deque>
#include<algorithm>

using namespace std;
const unsigned long  exp[10] = {1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000};
int R,K,N;
int M;
deque<int> state;
deque<int> g;
deque<int> start;
vector<int> mark;
vector<int> pre;
string perhold;
int startstate;
/*int solve()
{
	int ret = 0;
	int hold = 0;
	int person = 0;
	for(int i = 0; i < R; i++)
	{
		hold = g.front();
		person = 1;
		while(hold <= K && person < N)
		{
			int temp = g.front();
			g.pop_front();
			g.push_back(temp);
			hold += g.front();
			person++;
		}
		if(hold <= K)
		{
			ret += hold;
		}
		else
		{
			hold -= g.front();
			ret += hold;
		}
	}
	return ret;
}
*/
string numToString(int num)
{
	int s;
	string ret;
	s = 9;
	if(num == 0)
	{
		ret = "0";
		return ret;
	}
	for(s; num / exp[s] == 0 && s >= 0; s--);
	for(s; s >= 0; s--)
	{
		ret += num/exp[s] + '0';
		num = num % exp[s];
	}
	return ret;

}
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
string getStartState()
{
	int hold = 0;
	string ret("0");
	if(N == 1)
		return numToString(g[0]);
	deque<int> start(g);
	int status = 0;
	int person = 0;
	mark[0] = 1;
	while(true)
	{
		hold = g.front();
		person = 1;
		while(hold <= K && person < N)
		{
			int temp = g.front();
			int s = state.front();
			g.pop_front();
			state.pop_front();
			g.push_back(temp);
			state.push_back(s);
			hold += g.front();
			person++;
		}
		if(!mark[state.front()])
			mark[state.front()] = 1;
		else
		{
			startstate = state.front();
			break;
		}
	}
	mark.assign(N,0);
	mark[startstate] = 1;
	M = 0;
	while(true)
	{
		M++;
		hold = g.front();
		person = 1;
		while(hold <= K && person < N)
		{
			int temp = g.front();
			int s = state.front();
			g.pop_front();
			state.pop_front();
			g.push_back(temp);
			state.push_back(s);
			hold += g.front();
			person++;
		}
		if(hold <= K)
		{
			ret = PreciseAdd(ret,numToString(hold));
			if(!mark[state.front()])
				mark[state.front()] = 1;
			else
			{
				startstate = state.front();
				break;
			}
		}
		else
		{
			hold -= g.front();
			ret = PreciseAdd(ret,numToString(hold));
			if(!mark[state.front()])
				mark[state.front()] = 1;
			else
			{
				startstate = state.front();
				break;
			}
		}
	}
	return ret;
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

string  tsolve()
{
	string ret("0");
	string temp("0");
	int hold = 0;
	int person = 0;
	int r;
	for(int i = 0; i < N; i++)
	{
		state[i] = i;
	}
	g.assign(start.begin(),start.end());
	for(R; R > 0 ; )
	{
		R--;
		hold = g.front();
		person = 1;
		while(hold <= K && person < N)
		{
			int temp = g.front();
			int s = state.front();
			g.pop_front();
			state.pop_front();
			g.push_back(temp);
			state.push_back(s);
			hold += g.front();
			person++;
		}
		if(hold <= K)
		{
			ret = PreciseAdd(ret,numToString(hold));
			if(startstate == state.front())
				break;
		}
		else
		{
			hold -= g.front();
			ret = PreciseAdd(ret,numToString(hold));
			if(startstate == state.front())
				break;
		}
	}
	if(R > 0)
	{
		r = R / M;
		ret = PreciseAdd(ret,mutipleString(perhold,r));
		R = R % M;
	}
	for(R; R > 0 ; R--)
	{
		hold = g.front();
		person = 1;
		while(hold <= K && person < N)
		{
			int temp = g.front();
			int s = state.front();
			g.pop_front();
			state.pop_front();
			g.push_back(temp);
			state.push_back(s);
			hold += g.front();
			person++;
		}
		if(hold <= K)
		{
			ret = PreciseAdd(ret,numToString(hold));
		}
		else
		{
			hold -= g.front();
			ret = PreciseAdd(ret,numToString(hold));
		}
	}
	return ret;
}
int main()
{
	int T;
	ifstream input("C-large.in");
	ofstream out("test.out");
	input >> T;
	string result;
//	cout << mutipleString("123",23) << endl;
	for(int i = 1; i <= T; i++)
	{
		input >> R >> K >> N;
		g.assign(N,0);
		state.clear();
		mark.assign(N,0);
		pre.assign(N,-1);
		for(int j = 0; j < N; j++)
		{
			state.push_back(j);
		}
		for(int j = 0; j < N; j++)
		{
			input >> g[j];
		}
		start.assign(g.begin(),g.end());
		perhold = getStartState();
		
		result = tsolve();

		out << "Case #" << i << ": " << result << endl;
//		cout << M << endl;
	}
	return 0;
}