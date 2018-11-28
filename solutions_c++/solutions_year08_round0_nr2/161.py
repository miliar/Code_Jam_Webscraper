#include <cstdio>
#include <vector>

using namespace std;

const int MINUTES = (24*60);

int isdigit(char c)
{
	if (c>='0' && c<='9') return 1;
	else return 0;
}

void readschedule(int* departure_time, int* arrival_time)
{
	char c;
	while (!isdigit(c = getchar()));
	
	*departure_time = 600*(c-'0');
	c=getchar();
	*departure_time += 60*(c-'0');
	c=getchar(); //:
	c=getchar();
	*departure_time += 10*(c-'0');
	c=getchar();
	*departure_time += (c-'0');
	
	while (!isdigit(c = getchar()));
	
	*arrival_time = 600*(c-'0');
	c=getchar();
	*arrival_time += 60*(c-'0');
	c=getchar(); //:
	c=getchar();
	*arrival_time += 10*(c-'0');
	c=getchar();
	*arrival_time += (c-'0');
	
}

int main()
{
	int N;
	scanf("%d",&N);
	
	for (int i=0;i<N;i++)
	{
		vector<int> Atrains(MINUTES,0), Btrains(MINUTES,0);
		vector< vector<int> > Adepartures(MINUTES,vector<int>(0)), Bdepartures(MINUTES,vector<int>(0));
		
		int T;
		scanf("%d",&T);
		
		int NA,NB;
		scanf("%d",&NA);
		scanf("%d",&NB);

		for (int j=0;j<NA;j++)
		{
			int departure_time=-1, arrival_time=-1;
			readschedule(&departure_time,&arrival_time);
			Adepartures[departure_time].push_back(arrival_time+T);
		}

		for (int j=0;j<NB;j++)
		{
			int departure_time=-1, arrival_time=-1;
			readschedule(&departure_time,&arrival_time);
			Bdepartures[departure_time].push_back(arrival_time+T);
		}
		
		int trainsA = 0, trainsB = 0;
		int trainsNeededA = 0, trainsNeededB = 0;
		
		for (int j=0;j<MINUTES;j++)
		{
			trainsA += Atrains[j];
			trainsB += Btrains[j];
			
			if (Adepartures[j].size() > 0)
			{
				for (int k=0;k<Adepartures[j].size();k++)
				{
					if (trainsA>0) --trainsA;
					else ++trainsNeededA;

					if (Adepartures[j][k]<MINUTES) Btrains[Adepartures[j][k]] += 1;
				}
			}

			if (Bdepartures[j].size() > 0)
			{
				for (int k=0;k<Bdepartures[j].size();k++)
				{
					if (trainsB>0) --trainsB;
					else ++trainsNeededB;

					if (Bdepartures[j][k]<MINUTES) Atrains[Bdepartures[j][k]] += 1;
				}
			}
		}

		printf("Case #%d: %d %d\n", i+1, trainsNeededA, trainsNeededB);
	}
	return 0;
}
