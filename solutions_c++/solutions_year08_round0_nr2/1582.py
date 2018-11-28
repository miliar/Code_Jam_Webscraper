//CODEJAM

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct train
{
	int t1,t2;
	bool a;
};

int cmp(const void *a, const void *b)
{
	train *A = (train*)a;
	train *B = (train*)b;
	return( (A->t1) - (B->t1) );
}

int main()
{
	//vars
	ifstream f ("B-large.in");
	ofstream g ("B-large.out");
	int t,tt;
	int turn,nA,nB,cntA,cntB,a,b,c;
	string s;
	train tr[300];
	int avA[20000],avB[20000];
	//tescase loop
	f >> tt;
		for (t=1; t<=tt; t++)
		{
			//input
			f >> turn >> nA >> nB;
			b=0;
				for (a=0; a<nA; a++)
				{
					f >> s;
					tr[b].t1=((s[0]-'0')*10+(s[1]-'0'))*60 + ((s[3]-'0')*10+(s[4]-'0'));
					f >> s;
					tr[b].t2=((s[0]-'0')*10+(s[1]-'0'))*60 + ((s[3]-'0')*10+(s[4]-'0'));
					tr[b++].a=true;
				}
				for (a=0; a<nB; a++)
				{
					f >> s;
					tr[b].t1=((s[0]-'0')*10+(s[1]-'0'))*60 + ((s[3]-'0')*10+(s[4]-'0'));
					f >> s;
					tr[b].t2=((s[0]-'0')*10+(s[1]-'0'))*60 + ((s[3]-'0')*10+(s[4]-'0'));
					tr[b++].a=false;
				}
			//sort by first time
			qsort(tr,b,sizeof(train),cmp);
			//simulate
			cntA=0;
			cntB=0;
			nA=0;
			nB=0;
				for (a=0; a<b; a++)
					if (tr[a].a)
					{
						//look for an available train
							for (c=0; c<nA; c++)
								if (avA[c]<=tr[a].t1)
								{
									avA[c]=99999;
									goto skip1;
								}
						//need a new train here
						cntA++;
skip1:
						avB[nB++]=tr[a].t2+turn;
					}
					else
					{
						//look for an available train
							for (c=0; c<nB; c++)
								if (avB[c]<=tr[a].t1)
								{
									avB[c]=99999;
									goto skip2;
								}
						//need a new train here
						cntB++;
skip2:
						avA[nA++]=tr[a].t2+turn;
					}
			//output
			cout << "Case #" << t << ": " << cntA << ' ' << cntB << endl;
			g << "Case #" << t << ": " << cntA << ' ' << cntB << endl;
		}
	return(0);
}