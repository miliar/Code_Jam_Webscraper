#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int cases; cin >> cases;

	for(int iii=0;iii<cases;iii++)
	{
		int nNormal = 0;
		int suprising = 0;
		int googlers, nSuprising, nBest;
		cin >> googlers >> nSuprising >> nBest;
		vector<int> TotalScores;
		for(int j=0; j<googlers; j++)
		{
			int TotalScore; cin>>TotalScore;
			int PartScore;
			if(TotalScore == 0)
			{
				if(nBest==0)
					nNormal++;
				continue;
			}
			if(TotalScore%3==0)
			{
				PartScore = TotalScore/3-1;
			}
			else
			{
				PartScore = TotalScore/3;
			}
			if(PartScore+1>=nBest)
				nNormal++;
			else if(PartScore+2>=nBest && TotalScore%3!=1)
				suprising++;
		}
		cout << "Case #" << iii+1 <<": "<<(suprising>nSuprising?nSuprising:suprising)+nNormal<<endl;
	}
	return 0;
}