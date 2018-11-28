#include <iostream>
#include <ctime>
#include <vector>
#include <algorithm>
using namespace std;
int main (int argc, char * const argv[]) {
    // insert code here..

	//Read the Number of cases
	//loop through that number
	//Read the turnaround time
	//Read the a-b and b-a number
	long nCases;
	cin >> nCases;
	struct tm time_fmt;
	char *st;
	memset(&time_fmt,0,sizeof(time_fmt));
	time_fmt.tm_year = 2008 - 1900;
	time_fmt.tm_mon = 6;
	time_fmt.tm_mday = 15;
	time_fmt.tm_isdst = 1;
	for (int nCase=0; nCase < nCases; nCase++)
	{
			long turntime;
			cin >> turntime;
			int nA2B,nB2A;
			char time1[10], time2[10];
			cin >> nA2B;
			cin >> nB2A;
			time_t temp;
			vector<time_t> TimeAB, TimeBA;
			vector<time_t> AvailA, AvailB;
			for(int ctr = 0; ctr < nA2B ; ctr++)
			{
				cin >> time1;
				cin >> time2;
				st = strtok(time1,":");
				if (st != NULL)
				{					
					
					time_fmt.tm_hour = atoi(st);
					//cout << time_fmt.tm_hour << ":";
					st = strtok(NULL,"\0");
					if (st == NULL)
						return -1;					
					time_fmt.tm_min = atoi(st);										
					//cout << time_fmt.tm_min;
					temp = mktime(&time_fmt);
					if (temp < 0)
						return -1;
					TimeAB.push_back(temp);		
				}
				st = strtok(time2,":");
				if (st != NULL)
				{					
					time_fmt.tm_hour = atoi(st);
					st = strtok(NULL,"\0");
					if (st == NULL)
						return -1;
					time_fmt.tm_min = atoi(st);
					temp = mktime(&time_fmt);
					if (temp < 0)
						return -1;					
					AvailB.push_back(temp+(turntime*60));
				}
			}
			sort(TimeAB.begin(),TimeAB.end());
			sort(AvailB.begin(),AvailB.end());
			memset(time1,0,10);
			memset(time2,0,10);
			for(int ctr = 0; ctr < nB2A ; ctr++)
			{
				cin >> time1;
				cin >> time2;
				st = strtok(time1,":");
				if (st != NULL)
				{
					//cout << st << endl;
					time_fmt.tm_hour = atoi(st);
					st = strtok(NULL,"\0");
					if (st == NULL)
						return -1;
					time_fmt.tm_min = atoi(st);
					temp = mktime(&time_fmt);
					if (temp < 0)
						return -1;
					TimeBA.push_back(temp);
				}
				
				st = strtok(time2,":");
				if (st != NULL)
				{
					time_fmt.tm_hour = atoi(st);
					st = strtok(NULL,"\0");
					if (st == NULL)
						return -1;
					time_fmt.tm_min = atoi(st);
					temp = mktime(&time_fmt);
					if (temp < 0)
						return -1;
					AvailA.push_back(temp+(turntime*60));
				}
			}			
			sort(TimeBA.begin(),TimeBA.end());
			sort(AvailA.begin(),AvailA.end());
/*			
			for (int i = 0; i < TimeAB.size();i++)
				cout << TimeAB[i] << " ";
			cout << endl;
			for (int i = 0; i < AvailA.size();i++)
				cout << AvailA[i] << " ";
			cout << endl;			
			for (int i = 0; i < TimeBA.size();i++)
				cout << TimeBA[i] << " ";
			cout << endl;
			for (int i = 0; i < AvailB.size();i++)
				cout << AvailB[i] << " ";
			cout << endl;			
			
			cout << "OUT" << endl;
*/
			int count_a, count_b;
			count_a = count_b = 0;
			//cout <<"AvailB[0] = " << AvailA[0] << " AvailB[1] = " << AvailA[1] << endl;
			for (int i = 0 ; i < TimeAB.size(); i++)
			{
				//cout << "COMP: TimeAB =" << TimeAB[i] << " AVAILB = " << AvailA[0] << "Size: " <<AvailA.size() << endl;
				if (AvailA.size() > 0 && TimeAB[i] >= AvailA[0])
			{
					
						AvailA.erase(AvailA.begin());
						continue;
				}
				count_a++;
			}
			for (int i = 0 ; i < TimeBA.size(); i++)
			{
				if (AvailB.size() > 0 && TimeBA[i] >= AvailB[0])
				{
						AvailB.erase(AvailB.begin());
						continue;
				}
				count_b++;
			}
			cout << "Case #" << nCase+1 << ": " << count_a << " " << count_b <<endl;
	}
			
			
}
