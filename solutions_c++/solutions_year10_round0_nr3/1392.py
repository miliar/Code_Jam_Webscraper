#include <fstream>
#include <iostream>

using namespace std;


void main(int argc, char* argv[])
{
	if(argc != 3)
	{
		cout<<"usage error"<<endl;
		exit(0);
	}

	ifstream caseReader(argv[1]);
	ofstream resWriter(argv[2]);
	int nLine;
	caseReader>>nLine;
	for(int i=0; i<nLine; i++)
	{
		int R;
		int K;
		caseReader>>R;
		caseReader>>K;

		int nGroup;
		caseReader>>nGroup;
		int* arrGroup = new int[nGroup];
		int sumGroup = 0;
		for(int j=0; j<nGroup; j++){
			caseReader>>arrGroup[j];
			sumGroup += arrGroup[j];
		}

		if(sumGroup <= K)
		{
			resWriter<<"Case #"<<i+1<<": "<<sumGroup*R<<endl;
		}else{
			bool* arrLabel = new bool[nGroup];
			memset(arrLabel, 0, sizeof(bool)*nGroup);
			int* arrRound = new int[nGroup];
			int* arrGroupRound = new int[nGroup];

			int pos=0;
			int nRound=0;
			int totNum=0;
			int nGroupRound = 0;
			for(nRound=0; nRound< R; nRound++)
			{
				if(arrLabel[pos])
					break;
				
				arrLabel[pos] = true;
				arrRound[pos] = nRound;
				arrGroupRound[pos] = nGroupRound;

				int curCap = 0;
				while(curCap + arrGroup[pos] <= K)
				{
					curCap += arrGroup[pos];

					pos++;
					if(pos == nGroup)
					{
						pos = 0;
						nGroupRound++;
					}
				}
				totNum += curCap;
			}

			if(nRound < R)
			{
				int rCycle = nRound - arrRound[pos];
				int kCycle = nGroupRound - arrGroupRound[pos];
				int cycle = (R-nRound)/rCycle;
				nRound += cycle*rCycle;
				totNum += cycle*kCycle*sumGroup;
			}

			for(; nRound< R; nRound++)
			{
				int curCap = 0;
				while(curCap + arrGroup[pos] <= K)
				{
					curCap += arrGroup[pos];
					pos++;
					if(pos == nGroup)
					{
						pos = 0;
					}
				}
				totNum += curCap;
			}
			
			resWriter<<"Case #"<<i+1<<": "<<totNum<<endl;

			delete []arrLabel;
			delete []arrRound;
			delete []arrGroupRound;

		}

		delete [] arrGroup;
	}

	caseReader.close();
	resWriter.close();
}