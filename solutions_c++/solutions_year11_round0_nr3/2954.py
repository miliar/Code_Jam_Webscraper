#include<stdio.h>
#include<stdlib.h>
#include<set>

using namespace std;

typedef unsigned int ui;
struct entry_t
{
	ui patrick[2];
	ui sean[2];

	bool operator<(const entry_t &other) const
	{
		return (patrick[0]==other.patrick[0])?(patrick[1]<other.patrick[1]):(patrick[0]<other.patrick[0]);
	}
};

int n,values[1200];
set<entry_t> q[2];
int tq=0;

int comp(const void *in1, const void *in2)
{
	int i1=*(int*)in1;
	int i2=*(int*)in2;
	return i2-i1;
}

inline void sorted(entry_t &what)
{
	if (what.sean[0]<what.sean[1])
	{
		ui tmp=what.sean[0];
		what.sean[0]=what.sean[1];
		what.sean[1]=tmp;

		tmp=what.patrick[0];
		what.patrick[0]=what.patrick[1];
		what.patrick[1]=tmp;
	}
}

void append(int what)
{
	set<entry_t>::iterator i;

	for (i=q[tq].begin();i!=q[tq].end();i++)
	{
		struct entry_t trnt=*i,newstate;
		set<entry_t>::iterator ext;

		newstate.patrick[0]=trnt.patrick[0]^what;
		newstate.patrick[1]=trnt.patrick[1];
		newstate.sean[0]=trnt.sean[0]+what;
		newstate.sean[1]=trnt.sean[1];
		sorted(newstate);
		//printf("(%x,%x;%u,%u) + %d = (%x,%x;%u,%u)\n",trnt.patrick[0],trnt.patrick[1],trnt.sean[0],trnt.sean[1],what,newstate.patrick[0],newstate.patrick[1],newstate.sean[0],newstate.sean[1]);
		ext=q[tq^1].find(newstate);
		//if (ext!=q[tq^1].end()) { q[tq^1].erase(ext); }
		if (ext!=q[tq^1].end() && ext->sean[0]<newstate.sean[0]) { q[tq^1].erase(ext); }
		q[tq^1].insert(newstate);

		newstate.patrick[1]=trnt.patrick[1]^what;
		newstate.patrick[0]=trnt.patrick[0];
		newstate.sean[1]=trnt.sean[1]+what;
		newstate.sean[0]=trnt.sean[0];
		sorted(newstate);
		//printf("(%x,%x;%u,%u) + %d = (%x,%x;%u,%u)\n",trnt.patrick[0],trnt.patrick[1],trnt.sean[0],trnt.sean[1],what,newstate.patrick[0],newstate.patrick[1],newstate.sean[0],newstate.sean[1]);
		ext=q[tq^1].find(newstate);
		q[tq^1].insert(newstate);
	}

	tq^=1;
}

int main()
{
	int ncases,casenum;
	int i;
	entry_t empty;
	ui max;

	empty.patrick[0]=empty.patrick[1]=0;
	empty.sean[0]=empty.sean[1]=0;

	scanf("%d",&ncases);
	for (casenum=1;casenum<=ncases;casenum++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++) { scanf("%d",&values[i]); }
		//qsort(values,n,sizeof(int),comp);

		q[0].clear();
		q[1].clear();
		q[tq].insert(empty);

		for (i=0;i<n;i++)
		{
			append(values[i]);
			q[tq^1].clear();
			//printf("--------\n");
		}

		max=0;
		for (set<entry_t>::iterator j=q[tq].begin();j!=q[tq].end();j++)
		{
			if (j->patrick[0]==j->patrick[1] && j->sean[0]>max && j->sean[1]>0) { max=j->sean[0]; }
		}
		if (max==0) { printf("Case #%d: NO\n",casenum); } else { printf("Case #%d: %u\n",casenum,max); }
	}

	return 0;
}

