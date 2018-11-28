// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <map>
#include <set>
#include <list>
#include <string>
#include <iostream>
#include <fstream>
#include <strstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <cassert>
#include <math.h>

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//asigna en a el minimo
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//asigna en a el maximo

#define bitN(X) (1<<(X))//bit enesimo
#define bitN64(X) (((int64)(1))<<(X))////bit enesimo int 64
#define contain(S,X) (((S)&bitN(X))!=0)//tiene el bit
#define contain64(S,X) (((S)&bitN64(X))!=0)//tiene el bit
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//Bit mas bajo (on el numero sino bit en el T 
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//cantidad de bits en 1 
using namespace std;


//INT_MAX,LLONG_MAX

int N,M;
ifstream in("inS.txt");
ofstream out("out.txt");

map<int,list<int> > wordsBySize;
vector<string> words;
vector<string> orders;

struct Word
{
	Word()
	{
		memset(m_letters,0,sizeof(m_letters));
	}
	int m_letters[26];
};
vector<set<char> > lettersInWord; 



vector<Word> data;
int Calc(int o,int w)
{
	int points = 0;
	string &word = words[w];
	list<int> valid = wordsBySize[word.size()];
	Word thisW;
	int bitsok = 0;
	int totalBits = word.size();
	REP(i,orders[o].size())
	{
		char letter = orders[o][i]-'a';
		///tengo la letra dada en las posibles

		bool bGotLetter = false;
		list<int>::iterator it;
		for(it = valid.begin();it != valid.end() && !bGotLetter ;++it)
		{
			if(data[*it].m_letters[letter] != 0)
			{
				bGotLetter = true;
			}
		}
		if(bGotLetter)
		{///La pide
			if(data[w].m_letters[letter] == 0)///pierde
			{
				///Saco todas las palabras que tengan la letra
				++points;
				for(it = valid.begin();it != valid.end();)
				{
					if(data[*it].m_letters[letter] != 0)
						valid.erase(it++);
					else
						++it;
				}
			}
			else
			{
				int pattern = data[w].m_letters[letter];
				bitsok += countbit(pattern);
				thisW.m_letters[letter] = data[w].m_letters[letter];///marco
				if(totalBits == bitsok )
					return points;
				for(it = valid.begin();it != valid.end();)
				{
					if(data[*it].m_letters[letter] != pattern)
						valid.erase(it++);
					else
						++it;
				}
			}
		}
		
	}
	return 0;
	
}

void Solve()
{
	REP(o,orders.size())
	{
		string winner;
		int points = -1;
		REP(w,words.size())
		{
			int pp = Calc(o,w);
			if(pp > points)
			{
				winner = words[w];
				points = pp;
			}
		}
		out << " " << winner;
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	int CCC;
	in >> CCC;
	REP(cccc,CCC)
	{
		in >> N >> M;
		words.clear();
		words.resize(N);
		wordsBySize.clear();
		data.clear();
		data.resize(N);

		REP(i,N)
		{
			string w;
			in >> w;
			data[i] = Word();
			words[i] = w;
			wordsBySize[w.size()].push_back(i);
			REP(j,w.size())
			{
				data[i].m_letters[w[j]-'a'] |= bitN(j);
			}
		}
		orders.clear();
		orders.resize(M);
		REP(i,M)
		{
			in >> orders[i];
		}
		out << "Case #" << cccc+1 << ":";
		Solve();
		out << endl;
	}	return 0;
}

