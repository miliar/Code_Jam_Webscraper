// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
// Some solutions using BigInteger from http://mattmccutchen.net/bigint/
#include "bigint/BigIntegerAlgorithms.hh"
#include "bigint/BigIntegerUtils.hh"
#include "utilUtils.h"
#include "utilFile.h"
#include "utilString.h"
#include "assert.h"
#include "utilArray.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "utilRand.h"
#include "utilHashTable2.h"
#include <vector>
#include <set>
#include <map>
using namespace std;

#pragma warning(disable:4018)

int D, I, M;

class State;
typedef State *PState;

bool diff(int x, int y)
{
	int d = x - y;
	if (d<0)
		d = -d;
	return d>M;
}

class State
{
public:
	State()
	{
		cost = 0;
	}
	State(State &s)
	{
		cost = s.cost;
	}
	vector<int> p;
	int cost;
	bool isSmooth()
	{
		if (!p.size())
			return true;
		int lastv=p[0];
		for (int i=1; i<(int)p.size(); i++)
		{
			if (diff(p[i], lastv))
				return false;
			lastv = p[i];
		}
		return true;
	}
	vector<PState>getSucc()
	{
		vector<PState> ret;
		// Check deletes
		for (int i=0; i<p.size(); i++)
		{
			if (i <p.size()-1 && diff(p[i], p[i+1]) ||
				i>0 && diff(p[i], p[i-1]))
			{
				State *s2 = new State(*this);
				s2->cost+=D;
				for (int j=0; j<p.size(); j++)
				{
					if (j!=i)
						s2->p.push_back(p[j]);
				}
				ret.push_back(s2);
			}
		}
		// Check inserts
		if (M>0)
		{
			for (int i=0; i<p.size()-1; i++)
			{
				// full insert
				if (diff(p[i], p[i+1]))
				{
					State *s2 = new State(*this);
					for (int j=0; j<=i; j++)
						s2->p.push_back(p[j]);
					if (p[i+1] > p[i])
					{
						for (int j=p[i]+M; j<p[i+1]; j+=M)
						{
							s2->p.push_back(j);
							s2->cost+=I;
						}
					} else {
						for (int j=p[i]-M; j>p[i+1]; j-=M)
						{
							s2->p.push_back(j);
							s2->cost+=I;
						}
					}
					for (int j=i+1; j<p.size(); j++)
						s2->p.push_back(p[j]);
					ret.push_back(s2);

					// Insert + edit
					s2 = new State(*this);
					for (int j=0; j<=i; j++)
						s2->p.push_back(p[j]);
					if (p[i+1] > p[i])
					{
						for (int j=p[i]+M; j<p[i+1]-M; j+=M)
						{
							s2->p.push_back(j);
							s2->cost+=I;
						}
					} else {
						for (int j=p[i]-M; j>p[i+1]+M; j-=M)
						{
							s2->p.push_back(j);
							s2->cost+=I;
						}
					}
					for (int j=i+1; j<p.size(); j++)
						s2->p.push_back(p[j]);
					ret.push_back(s2);

					// Insert + edit
					s2 = new State(*this);
					for (int j=0; j<=i; j++)
						s2->p.push_back(p[j]);
					if (p[i+1] > p[i])
					{
						vector<int> t;
						for (int j=p[i+1]-M; j>p[i]+M; j-=M)
						{
							t.push_back(j);
							s2->cost+=I;
						}
						for (int j=0; j<t.size(); j++)
						{
							s2->p.push_back(t[t.size() - j - 1]);
						}
					} else {
						vector<int> t;
						for (int j=p[i+1]+M; j<p[i]-M; j+=M)
						{
							t.push_back(j);
							s2->cost+=I;
						}
						for (int j=0; j<t.size(); j++)
						{
							s2->p.push_back(t[t.size() - j - 1]);
						}
					}
					for (int j=i+1; j<p.size(); j++)
						s2->p.push_back(p[j]);
					ret.push_back(s2);

				}

			}
		}
		// Check edits
		if (p.size()>1)
		{
			// edit middles
			for (int i=0; i<p.size(); i++)
			{
				if (i>0 && diff(p[i-1], p[i]))
				{
					State *s2 = new State(*this);
					for (int j=0; j<p.size(); j++)
					{
						s2->p.push_back(p[j]);
					}
					int newv;
					if (p[i] > p[i-1])
						newv = p[i-1] + M;
					else
						newv = p[i-1] - M;
					s2->cost+=ABS(p[i] - newv);
					s2->p[i] = newv;
					ret.push_back(s2);
				}
				if (i < p.size()-1 && diff(p[i], p[i+1]))
				{
					State *s2 = new State(*this);
					for (int j=0; j<p.size(); j++)
					{
						s2->p.push_back(p[j]);
					}
					int newv;
					if (p[i] > p[i+1])
						newv = p[i+1] + M;
					else
						newv = p[i+1] - M;
					s2->cost+=ABS(p[i] - newv);
					s2->p[i] = newv;
					ret.push_back(s2);
				}
			}
		}
		return ret;
	}
};


unsigned int hashState(const PState s)
{
	return 0;
}

int cmpState(const PState s1, const PState s2)
{
	int d = s2->p.size() - s1->p.size();
	if (d)
		return d;
	d = s2->cost - s1->cost;
	if (d)
		return d;
	for (int i=0; i<s1->p.size(); i++)
	{
		d = s2->p[i] - s1->p[i];
		if (d)
			return d;
	}
	return 0;
}

char *doB(char **&toks)
{
	D = atoi(*toks++);
	I = atoi(*toks++);
	M = atoi(*toks++);
	int N = atoi(*toks++);

	State *s0 = new State();
	vector<PState> states;
	HashTable2<PState, bool> searched(256, hashState, cmpState);
	for (int i=0; i<N; i++)
	{
		s0->p.push_back(atoi(*toks++));
	}
	int best=-1;
	if (s0->isSmooth())
		return "0";
	states.push_back(s0);
	searched.add(s0, true, true);
	while (states.size())
	{
		PState sss = states[states.size()-1];
		states.pop_back();
		if (best!=-1 && sss->cost >= best)
			continue;
		vector<PState> succ = sss->getSucc();
		for (int i=0; i<succ.size(); i++)
		{
			PState s2 = succ[i];
			if (s2->isSmooth())
			{
				if (best==-1 || s2->cost < best)
					best = s2->cost;
			} else {
				if (searched.find(s2))
				{
					// Already in list
				} else {
					searched.add(s2, true, true);
					states.push_back(s2);
				}
			}
		}
	}
	// delete all entries

	static char buf[16384];
	sprintf(buf, "%d", best);
	return buf;
}
