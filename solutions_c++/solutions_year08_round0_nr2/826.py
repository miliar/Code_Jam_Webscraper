#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

struct TrainSchedule
{
	int nBeginMin;
	int nEndMin;
};

int GetLatesTrain(vector<int> &watiList, int &nIndex)
{
	int nLastest = 0x7fffffff;
	nIndex = 0;

	for (int i=0; i<watiList.size(); i++)
	{
		if (nLastest > watiList[i])
		{
			nLastest = watiList[i];
			nIndex = i;
		}
	}

	return nLastest;
}


void SortSchedule(vector<TrainSchedule> &schedule)
{
	if (schedule.empty()) return;
	for (int i=0; i<schedule.size()-1; i++)
	{
		for (int j=i+1; j<schedule.size(); j++)
		{
			if (schedule[i].nBeginMin > schedule[j].nBeginMin)
			{
				TrainSchedule temp = schedule[i];
				schedule[i] = schedule[j];
				schedule[j] = temp;
			}
		}
	}
}

int GetTimeInMinute(char *strTime)
{
	int Hour = (strTime[0]-'0') * 10 + (strTime[1]-'0');
	int Minute = (strTime[3]-'0') * 10 + (strTime[4]-'0');

	return Hour * 60 + Minute;
}

int main(int argc, char **argv)
{
	FILE *fp = fopen(argv[1], "rt");
	char szTimeStr[256];

	int N = 1;
	fscanf(fp, "%d", &N);

	for (int nCase=0; nCase<N; nCase++)
	{
		vector<TrainSchedule> AB_S;
		vector<TrainSchedule> BA_S;

		vector<int> A_Wait;
		vector<int> B_Wait;

		int nTurnMin = 0;
		fscanf(fp, "%d\n", &nTurnMin);

		int AB, BA;

		fscanf(fp, "%d %d\n", &AB, &BA);
		for (int i=0; i<AB; i++)
		{
			fgets(szTimeStr, 256, fp);	

			TrainSchedule schedule;
			
			schedule.nBeginMin = GetTimeInMinute(szTimeStr);
			schedule.nEndMin = GetTimeInMinute(szTimeStr + 6);

			AB_S.push_back(schedule);
		}


		for (int i=0; i<BA; i++)
		{
			fgets(szTimeStr, 256, fp);	

			TrainSchedule schedule;
			
			schedule.nBeginMin = GetTimeInMinute(szTimeStr);
			schedule.nEndMin = GetTimeInMinute(szTimeStr + 6);
			BA_S.push_back(schedule);
		}

		SortSchedule(AB_S);
		SortSchedule(BA_S);

		int FromA = 0, FromB = 0;

		int n1 = 0, n2 = 0;
		int nIndex;
		do
		{
			if (n2 == BA && n1 == AB)
			{
				break;
			}

			else if(n2 == BA || (n1 != AB && AB_S[n1].nBeginMin <= BA_S[n2].nBeginMin))
			{
				if (A_Wait.empty() || GetLatesTrain(A_Wait, nIndex) > AB_S[n1].nBeginMin)
				{
					FromA++;
				}
				else
				{
					A_Wait.erase(A_Wait.begin() + nIndex);
				}
				
				B_Wait.push_back(AB_S[n1].nEndMin + nTurnMin);
				n1++;

			}
			else if(n1 == AB || (n2 != BA && AB_S[n1].nBeginMin > BA_S[n2].nBeginMin))
			{
				if (B_Wait.empty() || GetLatesTrain(B_Wait, nIndex) > BA_S[n2].nBeginMin)
				{
					FromB++;
				}
				else
				{
					B_Wait.erase(B_Wait.begin() + nIndex);
				}

				A_Wait.push_back(BA_S[n2].nEndMin + nTurnMin);
				n2++;
			}

		}while(n1<=AB || n2<=BA);


		printf("Case #%d: %d %d\n", nCase+1, FromA, FromB);

	}


	fclose(fp);
	return 0;
}