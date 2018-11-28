//GoogleCode1.cpp : Defines the entry point for the console application.
//Code written in C++ with using some ANSI-C features
//Compiled and run using MS Visual Studio 2008 SP1
//Tested on OS Windows Vista
//Code created by Danny Ritiu - 2009
//Copyright Danny Ritiu & Google inc.


#include <stdafx.h>
#include <stdlib.h>
#include <vector>

using namespace std;

vector<int> e;
int gsi;
struct word {
	int ID;
	char *w;
};

int comp(const void *, const void *);

int _tmain(int argc, _TCHAR* argv[])
{
	int L,D,N,i,j,n,zk,cs,sum;
	int *MS;
	bool wg,thissum;
	unsigned int k;
	word *W;
	vector<int> **A;
	char *ts;
	
	FILE *f;
	FILE *g;
	fopen_s(&f,"A-large.in","r");
	fopen_s(&g,"A-large.out","w");
	fscanf_s(f,"%d %d %d",&L,&D,&N);
	
	W=new word[D];
	for (i=0; i<D; ++i)	{
		W[i].ID=i;
		W[i].w=new char[L+1];
		W[i].w[L]=0;
		fscanf(f,"%s",W[i].w);
	}
	
	MS=new int[D];
	A=new vector<int>*[26];
	for (i=0; i<26; ++i) {
		A[i]=new vector<int>[L];
	}

	for (i=0; i<L; ++i) {
		gsi=i;
		qsort(W,D,sizeof(word),comp);
		for (j=0; j<D; ++j) {
			(&(A[W[j].w[gsi]-97][gsi]))->push_back(W[j].ID);
		}
	}
	
	ts=new char[L*28+1];

	for (i=0; i<N; ++i) {
		thissum=false;
		wg=true;
		fscanf(f,"%s",ts);
		n=strlen(ts);
		zk=0; cs=-1;
		for (j=0; j<D; ++j)
			MS[j]=0;
		for (j=0; j<n; ++j) {
			if (ts[j]=='(') 
				zk=1;
			else if (ts[j]==')')
				zk=0;
			else {
				if (zk==0 || (zk==1 && ts[j-1]=='(')) {
					if (!wg) thissum=true;
					cs++;
					wg=false;
				}
				if ((A[ts[j]-97][cs]).size()>0)
					wg=true;
				for (k=0; k<(A[ts[j]-97][cs]).size(); ++k)
					MS[(A[ts[j]-97][cs]).at(k)]++;
			}
			if (thissum) j=n+1;
		}
		sum=0;
		if (!thissum)
			for (j=0; j<D; ++j)
				if (MS[j]==L) sum++;
		fprintf(g,"Case #%d: %d\n",i+1,sum);
	}


	fclose(f);
	fclose(g);
	return 0;
}

int comp(const void *a, const void *b)
{
	if ((*(word*)a).w[gsi] > (*(word*)b).w[gsi]) return 1;
	if ((*(word*)a).w[gsi] < (*(word*)b).w[gsi]) return -1;
	return 0;
}