// a.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
#include <string>
//#include <cmath>
#include <cstdlib>

using namespace std;

#define fori(i_,f_,t_) for(int i_=f_;i_<t_;++i_)
#define fore(i_,c_) for(auto i_=c_.begin();i_!=c_.end();++i_)
#define pb	push_back

const size_t N=4;

char solve(string b)
{
	// test rows
	char w = 0;
	fori(k,0,N)
	{
		char m=0;
		fori(i,0,N)
		{
			char c = b[k*N+i];
			if (c=='T')
				continue;
			if (c=='.')
			{
				m=-1;
				break;
			}
			if (m && m!=c)
			{
				m=-1;
				break;
			}
			m=c;

		}
		if (m>0)
		{
			w=m;
			break;
		}
	}
	if (w) return w;
	// test columns
	fori(k,0,N)
	{
		char m=0;
		fori(i,0,N)
		{
			char c = b[i*N+k];
			if (c=='T')
				continue;
			if (c=='.')
			{
				m=-1;
				break;
			}
			if (m && m!=c)
			{
				m=-1;
				break;
			}
			m=c;

		}
		if (m>0)
		{
			w=m;
			break;
		}
	}

	if (w) return w;

	// test diagonals
	{
		char m=0;
		fori(i,0,N)
		{
			char c = b[i*N+i];
			if (c=='T')
				continue;
			if (c=='.')
			{
				m=-1;
				break;
			}
			if (m && m!=c)
			{
				m=-1;
				break;
			}
			m=c;

		}
		if (m>0)
		{
			w=m;
		}
	}

	{
		char m=0;
		fori(i,0,N)
		{
			char c = b[i*N+N-i-1];
			if (c=='T')
				continue;
			if (c=='.')
			{
				m=-1;
				break;
			}
			if (m && m!=c)
			{
				m=-1;
				break;
			}
			m=c;

		}
		if (m>0)
		{
			w=m;
		}
	}
	
	if (!w)
	{
		return ((b.find('.')!=string::npos)?-1:0);
	}
	return w;
}

int main(int argc, char* argv[])
{
	int T;
	cin>>T;
	fori(t,0,T)
	{
		cout<<"Case #"<<t+1<<": ";
		string b;
		string s;
		fori(i,0,N)
		{
			cin>>s;
			b +=s;
		}
		
		char w = solve(b);
		switch(w)
		{
		case 0:
			cout<<"Draw";
			break;
		case 'X':
			cout<<"X won";
			break;
		case 'O':
			cout<<"O won";
			break;
		default:
			cout<<"Game has not completed";
			break;
		}
        cout<<std::endl;
		
		//cin>>s;
	}

	return 0;
}

