#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
int nbTest;
int nbBoutonsSeq;

int main()
{
	scanf("%d\n", &nbTest);
	
	for(int i = 0; i < nbTest; i++)
	{
		scanf("%d", &nbBoutonsSeq);
		
		int dist=0;
		vector<int> seq[3];
		int pos[2]= {1, 1};
		
		for(int j = 0; j < nbBoutonsSeq; j++)
		{
			char str[2];
			scanf("%s", str);
			int type = (str[0]=='O');
			int id;
			scanf("%d", &id);
			seq[type].push_back(id);
			seq[2].push_back(type);
		}
		
		int id = 0;
		int next[2] = {0, 0};
		int tmp;
		for(tmp = 1; id != nbBoutonsSeq; tmp++)
		{
			bool mvd[2]={false, false};
			int man = seq[2][id];
			if(id < nbBoutonsSeq && seq[man][next[man]] == pos[man])
			{
				id++;
				next[man]++;
				mvd[man]=true;
				//man=seq[2][id];
			}
			if(id==nbBoutonsSeq)break;
			if(!mvd[0] && seq[0].size() > next[0]){
			if(pos[0] < seq[0][next[0]])pos[0]++;
			if(pos[0] > seq[0][next[0]])pos[0]--;}
			if(!mvd[1] && seq[1].size() > next[1]){
			if(pos[1] < seq[1][next[1]])pos[1]++;
			if(pos[1] > seq[1][next[1]])pos[1]--;}
		}
		
		printf("Case #%d: %d\n", i+1, tmp);
	}
	
	return 0;
}

