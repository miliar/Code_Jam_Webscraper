#pragma warning (disable:4786)
#include <algorithm>
#include <cstdio>
#include <list>

using namespace std;

typedef struct TableEle
{
	int time;
	int station;//1-A 2-B
	bool operator<(TableEle item)
	{
		if (this->time < item.time)
			return true;
		else
			return false;
	}
}TableEle;

typedef list<TableEle> STRUCTVECTOR; 

bool UDgreater(TableEle elem1, TableEle elem2)
{
	printf("%d, %d\n", elem1.time, elem2.time);
	return elem1.time < elem2.time;
}

int getNumber(char* str, int start, int length) 
{ 
	int i; 
	int n = 0; 
	for(i = start; i < start + length; i++) 
	{ 
		if(str[i] < '0' || str[i] > '9') 
			return 0; 
		n = n * 10 + str[i] - '0'; 
	} 
	return n; 
} 

int getTime(char* str)
{
	int hour = getNumber(str, 0, 2);
	int minute = getNumber(str, 3, 2);
	return hour*60 + minute;
}

bool FindEle(STRUCTVECTOR& vec, TableEle t)
{
	STRUCTVECTOR::iterator theIterator;
	for (theIterator=vec.begin(); theIterator!=vec.end(); theIterator++)
	{
		TableEle ele = *theIterator;
		if (ele.time == t.time && ele.station != t.station)
		{
			vec.erase(theIterator);
			return true;
		}
	}
	return false;
}

int main()
{
	FILE *fp, *fw;
	if ((fp = fopen("B-large.in.txt", "r")) == NULL) 
		return 1;
	if ((fw = fopen("B-large.out.txt", "w")) == NULL)
		return 1;
	int max_casenum = 0;
	fscanf(fp, "%d", &max_casenum);
	for (int casenum = 0; casenum < max_casenum; casenum++)
	{
		int train_in_A = 0, train_in_B = 0;
		//
		int interval = 0;
		fscanf(fp, "%d", &interval);
		//
		int tripA=0, tripB=0;
		fscanf(fp, "%d %d", &tripA, &tripB);
		bool tag = false;
		if (0 == tripA)
		{
			train_in_B = tripB;
			tag = true;
		}
		if (0 == tripB)
		{
			train_in_A = tripA;
			tag = true;
		}
		if (tag)
		{
			fprintf(fw, "Case #%d: %d %d \n", casenum+1, train_in_A, train_in_B);
			continue;
		}
		//
		STRUCTVECTOR v1, v2;
		for (int i=0; i<tripA; i++)
		{
			char cSTime[6], cETime[6];
			for (int j=0; j<6; j++)
			{
				cSTime[j] = '\0';
				cETime[j] = '\0';
			}
			fscanf(fp, "%s %s", cSTime, cETime);
			TableEle t1, t2;
			t1.time = getTime(cSTime);
			t2.time = getTime(cETime) + interval;
			t1.station = 1;
			t2.station = 1;
			if (!FindEle(v1, t1))
				v1.push_back(t1);
			if (!FindEle(v2, t2))
				v2.push_back(t2);
		}
		for (int k=0; k<tripB; k++)
		{
			char cSTime[6], cETime[6];
			for (int j=0; j<6; j++)
			{
				cSTime[j] = '\0';
				cETime[j] = '\0';
			}
			fscanf(fp, "%s %s", cSTime, cETime);
			TableEle t1, t2;
			t2.time = getTime(cSTime);
			t1.time = getTime(cETime) + interval;
			t1.station = 2;
			t2.station = 2;
			if (!FindEle(v1, t1))
				v1.push_back(t1);
			if (!FindEle(v2, t2))
				v2.push_back(t2);
		}
		//
		v1.sort();
		v2.sort();
		//
		STRUCTVECTOR::iterator theIterator;
		int temp = 0;
		//
		printf("Case%d:\n", casenum+1);
		for (theIterator=v1.begin(); theIterator!=v1.end(); theIterator++)
		{
			TableEle tmpEle = *theIterator;
			printf("%d %d \n", tmpEle.time, tmpEle.station);
		}
		printf("********************\n");
		temp = 0;
		for (theIterator=v2.begin(); theIterator!=v2.end(); theIterator++)
		{
			TableEle tmpEle = *theIterator;
			printf("%d %d \n", tmpEle.time, tmpEle.station);
		}
		printf("*******************************\n");
		//
		for (theIterator=v1.begin(); theIterator!=v1.end(); theIterator++)
		{
			TableEle tmpEle = *theIterator;
			if (tmpEle.station == 1)
				temp++;
			else
				temp--;
			if (train_in_A <= temp)
				train_in_A = temp;
		}
		temp = 0;
		for (theIterator=v2.begin(); theIterator!=v2.end(); theIterator++)
		{
			TableEle tmpEle = *theIterator;
			if (tmpEle.station == 2)
				temp++;
			else
				temp--;
			if (train_in_B <= temp)
				train_in_B = temp;
		}
		//
		fprintf(fw, "Case #%d: %d %d \n", casenum+1, train_in_A, train_in_B);
	}
	fclose(fp);
	fclose(fw);
	return 0;	
}