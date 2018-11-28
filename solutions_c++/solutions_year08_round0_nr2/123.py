#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

int T, NA,NB;

map<int,int> atA, atB;

const int MAXM=10000;

int s2mins(string s)
{
	if(s[2]!=':' || s.size()!=5)
		fprintf(stderr,"stupid\n");
	int h=(s[0]-'0')*10 + s[1]-'0';
	int m=(s[3]-'0')*10 + s[4]-'0';
	//printf("%s -> %d\n", s.c_str(), 60*h+m);
	return 60*h+m;
}

int main()
{
	int ttt;
	cin >> ttt;
	for(int cutest=1;cutest<=ttt;cutest++){
		atA.clear();
		atB.clear();
	
		cin >> T >> NA >> NB;
		fprintf(stderr, "T%d NA%d NB%d\n",T,NA,NB);
		for(int marsh=0;marsh<NA;marsh++){
			string st, fi;
			cin >> st >> fi;
			int dep=s2mins(st);
			int ariv=s2mins(fi);
			
			for(int mi=dep;mi<MAXM;mi++)
				atA[mi]--;
			for(int mi=ariv+T;mi<MAXM;mi++)
				atB[mi]++;
		}

		fprintf(stderr, "read B\n");

		for(int marsh=0;marsh<NB;marsh++){
			string st, fi;
			cin >> st >> fi;
			int dep=s2mins(st);
			int ariv=s2mins(fi);
			
			for(int mi=dep;mi<MAXM;mi++)
				atB[mi]--;
			for(int mi=ariv+T;mi<MAXM;mi++)
				atA[mi]++;
		}
		
		int SA=0, SB=0;
		for(int mi=0;mi<MAXM;mi++){
			SA=max(SA, -atA[mi]);
			SB=max(SB, -atB[mi]);
		}
		fprintf(stderr, "T%d NA%d NB%d ==> %d %d\n",T,NA,NB, SA, SB);
		printf("Case #%d: %d %d\n",cutest, SA,SB);
	}//endtest
	return 0;
}
