#include <iostream>
#include <fstream>
#include <vector>
#include <inttypes.h>
#include <assert.h>
#include <stdlib.h>

using namespace std;

enum STATE {UNSEEN=0,SEEN,COUNTING,DONE};
class sequence
{
public:
	STATE state;
	uint64_t lastSeen;
	uint64_t period;
	sequence():state(UNSEEN),lastSeen(0),period(0){}
};

int main(int argc, char* argv[])
{
	ifstream f(argv[1]);
	int testCases;
	f >> testCases;

	for(int i=0;i<testCases;i++)
	{
		uint64_t R,k,N;
		f >> R >> k >> N;
		vector<uint64_t> groups(N);
		assert(groups.size()==N);
		for(int j=0;j<N;j++)
			f >> groups[j];

		vector<sequence> sequences(N);
		assert(sequences.size()==N);

		uint64_t rounds=0;
		uint64_t total=0;
		uint64_t money=0;
		uint64_t baseMoney=0;
		uint64_t usedGroups=0;
		bool searchLoops=true;

		sequences[0].state=SEEN;
		sequences[0].lastSeen=0;

		for(int j=0;j<N;j=(j+1)%N)
		{
			if((total+groups[j])>k || usedGroups==N) //This cannot be added
			{
				money+=total; //*1 €
				rounds++;
				if(rounds==R)
					break;

				if(searchLoops)
				{
					if(sequences[j].state==UNSEEN)
					{
						sequences[j].state=SEEN;
						sequences[j].lastSeen=rounds;
					}
					else if(sequences[j].state==SEEN)
					{
						//Loop detected
						sequences[j].state=COUNTING;
						searchLoops=false;
						sequences[j].period=rounds-sequences[j].lastSeen;
						baseMoney=money;
						money=0;
					}
					else
						::abort();
				}
				else
				{
					if(sequences[j].state==COUNTING)
					{
						//Loop resolved
						//Let's see how many periods remains
						uint64_t remainingRounds=R-rounds;
						uint64_t periods=remainingRounds/sequences[j].period;
						rounds+=(periods*sequences[j].period);
						money*=(periods+1);
						if(rounds==R)
							break;
						sequences[j].state=DONE;
					}
					else if(sequences[j].state==DONE)
						::abort();
				}

				total=groups[j];
				usedGroups=1;
			}
			else
			{
				total+=groups[j];
				usedGroups++;
			}
		}
		money+=baseMoney;
		cout << "Case #" << (i+1) << ": " << money << endl;
	}
}
