#include <vector>
#include <iostream>

using namespace std;

class status
{
	unsigned int station_front;
	unsigned int station_back;
	status(unsigned int start):station_front(start),station_back(start){}
};

class times
{
public:
	unsigned int start;
	unsigned int end;
	int dir;
	bool operator<(const times& t) const
	{
		if(start<t.start)
			return true;
		else if(start==t.start)
		{
			if(end<t.end)
				return true;
			else
				return false;
		}
		else
			return false;
	}
};

int main(int argc,char* argv[])
{
	FILE* f=fopen(argv[1],"r");

	int num_cases;
	fscanf(f,"%u\n",&num_cases);
	for(int i=0;i<num_cases;i++)
	{
		int turn;
		fscanf(f,"%u\n",&turn);
		int na,nb;
		fscanf(f,"%u %u\n",&na,&nb);
		times* timesAB=new times[na+nb];
		bool* used=new bool[na+nb];

		for(int j=0;j<na+nb;j++)
		{
			int a,b,c,d;
			fscanf(f,"%u:%u %u:%u\n",&a,&b,&c,&d);
			timesAB[j].start=a*60+b;
			timesAB[j].end=c*60+d;
			if(j<na)
				timesAB[j].dir=1;
			else
				timesAB[j].dir=2;
			used[j]=false;
		}

		if(na+nb>0)
			sort(timesAB,timesAB+na+nb);
		int trains[3]={0,0,0};
		for(int j=0;j<na+nb;j++)
		{
			if(used[j])
				continue;
			int cur_dir=timesAB[j].dir;
			trains[cur_dir]++;
			used[j]=true;
			int time_now=timesAB[j].end;
			//unsigned int nearest=~0;
			for(int k=0;k<na+nb;k++)
			{
				if(used[k])
					continue;
				if(timesAB[k].start>=time_now+turn && timesAB[k].dir!=cur_dir)
				{
					used[k]=true;
					cur_dir=timesAB[k].dir;
					time_now=timesAB[k].end;
				}
			}
		}

		cout << "Case #" << i+1 << ": " << trains[1] << " " << trains[2] << endl;


	}

}
	
