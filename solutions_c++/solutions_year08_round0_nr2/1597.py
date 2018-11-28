#include <iostream>
#include <cstring>
#include <list>

using namespace std;
int T, NA, NB;

struct typTRIP {
	int departure;
	int arrival;
	int usedFlag;
} NATrip[100], NBTrip[100];

list<string> split(string str, string delim) {
	list<string> result;
	unsigned int cutAt;
	while((cutAt = str.find_first_of(delim))!= string::npos)
	{
		if (cutAt >0) {
			result.push_back(str.substr(0,cutAt));
		}
		str = str.substr(cutAt +1);
	}
	if (str.length()>0) {
		result.push_back(str);
	}
	return result;
}

int main() {
	int i, j, k, N;
	string str;
	int countA, countB;

	/* Begin read data from stdin */
	getline(cin, str);
	N = atoi(str.c_str());
	for (i=0; i<N; i++) {
		getline(cin, str);
		T = atoi(str.c_str());
		getline(cin, str);
		list<string> strList = split(str," ");
		list<string>::iterator iter = strList.begin();
		NA = atoi(string(*iter).c_str()); iter++;
		NB = atoi(string(*iter).c_str());
		for (j=0; j<NA; j++) {
			int h,m;
			string str1,str2;
			getline(cin, str);
			strList = split(str," ");
			iter = strList.begin();
			str1 = *iter; iter++;
			str2 = *iter;

			strList = split(str1,":");
			iter = strList.begin();
			h = atoi(string(*iter).c_str()); iter++;
			m = atoi(string(*iter).c_str());
			NATrip[j].departure = h*60+m;

			strList = split(str2,":");
			iter = strList.begin();
			h = atoi(string(*iter).c_str()); iter++;
			m = atoi(string(*iter).c_str());
			NATrip[j].arrival = h*60+m;
			NATrip[j].usedFlag = 0;
		}

		for (j=0; j<NB; j++) {
			int h,m;
			string str1,str2;
			getline(cin, str);
			strList = split(str," ");
			iter = strList.begin();
			str1 = *iter; iter++;
			str2 = *iter;

			strList = split(str1,":");
			iter = strList.begin();
			h = atoi(string(*iter).c_str()); iter++;
			m = atoi(string(*iter).c_str());
			NBTrip[j].departure = h*60+m;

			strList = split(str2,":");
			iter = strList.begin();
			h = atoi(string(*iter).c_str()); iter++;
			m = atoi(string(*iter).c_str());
			NBTrip[j].arrival = h*60+m;
			NBTrip[j].usedFlag = 0;
		}
		/* End read data from stdin */

		//debug
		/*
		for (j=0; j<NA; j++) {
			cout << NATrip[j].departure << ' ' << NATrip[j].arrival << endl;
		}
		cout <<"--------"<<endl;
		for (j=0; j<NB; j++) {
			cout << NBTrip[j].departure << ' ' << NBTrip[j].arrival << endl;
		}
*/
		int arriveTime, pos;
		countA = NA; countB = NB;
		for (j=0; j<NA; j++)
		{
			arriveTime = 0; pos = -1;
			for (k=0; k<NB; k++)
				if ((T+NBTrip[k].arrival<=NATrip[j].departure) && (NBTrip[k].usedFlag==0) && (NBTrip[k].arrival>arriveTime))
				{
					arriveTime = NBTrip[k].arrival;
					pos = k;
				}
			if (arriveTime>0) {
				countA--; NBTrip[pos].usedFlag = 1;
			}
		}
		for (j=0; j<NB; j++)
		{
			arriveTime = 0; pos = -1;
			for (k=0; k<NA; k++)
				if ((T+NATrip[k].arrival<=NBTrip[j].departure) && (NATrip[k].usedFlag==0) && (NATrip[k].arrival>arriveTime))
				{
					arriveTime = NATrip[k].arrival;
					pos = k;
				}
			if (arriveTime>0) {
				countB--; NATrip[pos].usedFlag = 1;
			}
		}
		cout << "Case #" << i+1 << ": " << countA << ' ' << countB << endl;
	} // for N
	return 0;
}
