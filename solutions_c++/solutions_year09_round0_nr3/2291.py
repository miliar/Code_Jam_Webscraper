

#include "stdafx.h"
#include <string>
#include <fstream>
#include <sstream>

using namespace std;
using std::string;
stringstream ss;

static struct Item
{
	char letter;
	int index[500];
	int instancesOfIndex[500];
	int num;
};

int caseNum = 0;
int findIndex(char c, int p, Item* a);
int calculateNum(Item* a, int elmIndex, int currIndex);

int _tmain(int argc, _TCHAR* argv[])
{
	char* answer = "welcome to code jam";
	const char *inputFileName;
	
	ifstream inp( "D:\\CodeJam09\\C-large.in" );
	string temp;
	getline( inp, temp );
	int caseNum = atoi(temp.c_str());

	FILE * pFile = fopen ("D:\\CodeJam09\\outputLargeFile.txt","w");

	for(int t=0 ; t<caseNum ; t++)
	{	

		Item data[19];

		for(int q=0 ; q<19 ; q++){
			data[q].num = 0;
			data[q].letter = answer[q];
		}	

		
		getline( inp, temp );
		const char* content = temp.c_str();


		for(int i=0 ; i<temp.length(); i++)
		{
			findIndex(content[i], i, data);
		}

		int total = 0;
		for(int i=0 ; i<data[18].num ; i++)
		{
			total += data[18].instancesOfIndex[i]%10000;
			//total += calculateNum(data, 1, data[0].index[i]);
		}
		

		total = total%10000;

		std::string s;
		std::stringstream out;
		out << total;
		s = out.str();		

		int len = s.length();
		if(len < 4)
		{
			for(int w=0 ; w<(4-len) ; w++)
				s.insert(0, "0");
		}
		else
			s = s.substr(len-4, 4);

		const char* cc = s.c_str();

		fprintf(pFile, "Case #%d: %s\n", t+1, cc);
	}	

	fclose (pFile);


	
	return 0;
}

int calculateNum(Item* a, int elmIndex, int currIndex)
{
	if(elmIndex == 18)
	{
		int num = 0;
		for(int i=0 ; i<a[elmIndex].num ; i++){
			if(a[elmIndex].index[i] > currIndex)
				num++;
		}
//printf("%d, ", num);
		return num;
	}
	else
	{
		int result = 0;
		for(int i=0 ; i<a[elmIndex].num ; i++)
		{
			if(a[elmIndex].index[i] > currIndex)
				result += calculateNum(a, elmIndex+1, a[elmIndex].index[i]);
		}
//printf("%d, ", result);
		return result;
	}
}

int findIndex(char c, int p, Item* a)
{
	int num = 0;
	if(c == 'w'){
		a[0].index[a[0].num] = p;
		a[0].instancesOfIndex[a[0].num++] = 1;
	}
	else if(c == 'e'){
		a[1].index[a[1].num] = p;
		num = 0;
		for(int i=0 ; i<a[0].num ; i++)
			if(a[0].index[i]<p)
				num+=a[0].instancesOfIndex[i];
		a[1].instancesOfIndex[a[1].num++] = num%10000;

		a[6].index[a[6].num] = p;	
		num = 0;
		for(int i=0 ; i<a[5].num ; i++)
			if(a[5].index[i]<p)
				num+=a[5].instancesOfIndex[i];
		a[6].instancesOfIndex[a[6].num++] = num%10000;


		a[14].index[a[14].num] = p;
		num = 0;
		for(int i=0 ; i<a[13].num ; i++)
			if(a[13].index[i]<p)
				num+=a[13].instancesOfIndex[i];
		a[14].instancesOfIndex[a[14].num++] = num%10000;
	}
	else if(c == 'l'){
		a[2].index[a[2].num] = p;
		num = 0;
		for(int i=0 ; i<a[1].num ; i++)
			if(a[1].index[i]<p)
				num+=a[1].instancesOfIndex[i];
		a[2].instancesOfIndex[a[2].num++] = num%10000;
	}
	else if(c == 'c'){
		a[3].index[a[3].num] = p;
		num = 0;
		for(int i=0 ; i<a[2].num ; i++)
			if(a[2].index[i]<p)
				num+=a[2].instancesOfIndex[i];
		a[3].instancesOfIndex[a[3].num++] = num%10000;

		a[11].index[a[11].num] = p;
		num = 0;
		for(int i=0 ; i<a[10].num ; i++)
			if(a[10].index[i]<p)
				num+=a[10].instancesOfIndex[i];
		a[11].instancesOfIndex[a[11].num++] = num%10000;
	}
	else if(c == 'o'){
		a[4].index[a[4].num] = p;
		num = 0;
		for(int i=0 ; i<a[3].num ; i++)
			if(a[3].index[i]<p)
				num+=a[3].instancesOfIndex[i];
		a[4].instancesOfIndex[a[4].num++] = num%10000;

		a[9].index[a[9].num] = p;
		num = 0;
		for(int i=0 ; i<a[8].num ; i++)
			if(a[8].index[i]<p)
				num+=a[8].instancesOfIndex[i];
		a[9].instancesOfIndex[a[9].num++] = num%10000;

		a[12].index[a[12].num] = p;
		num = 0;
		for(int i=0 ; i<a[11].num ; i++)
			if(a[11].index[i]<p)
				num+=a[11].instancesOfIndex[i];
		a[12].instancesOfIndex[a[12].num++] = num%10000;
	}
	else if(c == 'm'){
		a[5].index[a[5].num] = p;
		num = 0;
		for(int i=0 ; i<a[4].num ; i++)
			if(a[4].index[i]<p)
				num+=a[4].instancesOfIndex[i];
		a[5].instancesOfIndex[a[5].num++] = num%10000;

		a[18].index[a[18].num] = p;
		num = 0;
		for(int i=0 ; i<a[17].num ; i++)
			if(a[17].index[i]<p)
				num+=a[17].instancesOfIndex[i];
		a[18].instancesOfIndex[a[18].num++] = num%10000;
	}
	else if(c == ' '){
		a[7].index[a[7].num] = p;
		num = 0;
		for(int i=0 ; i<a[6].num ; i++)
			if(a[6].index[i]<p)
				num+=a[6].instancesOfIndex[i];
		a[7].instancesOfIndex[a[7].num++] = num%10000;

		a[10].index[a[10].num] = p;
		num = 0;
		for(int i=0 ; i<a[9].num ; i++)
			if(a[9].index[i]<p)
				num+=a[9].instancesOfIndex[i];
		a[10].instancesOfIndex[a[10].num++] = num%10000;

		a[15].index[a[15].num] = p;
		num = 0;
		for(int i=0 ; i<a[14].num ; i++)
			if(a[14].index[i]<p)
				num+=a[14].instancesOfIndex[i];
		a[15].instancesOfIndex[a[15].num++] = num%10000;
	}
	else if(c == 't'){
		a[8].index[a[8].num] = p;
		num = 0;
		for(int i=0 ; i<a[7].num ; i++)
			if(a[7].index[i]<p)
				num+=a[7].instancesOfIndex[i];
		a[8].instancesOfIndex[a[8].num++] = num%10000;
	}
	else if(c == 'd'){
		a[13].index[a[13].num] = p;
		num = 0;
		for(int i=0 ; i<a[12].num ; i++)
			if(a[12].index[i]<p)
				num+=a[12].instancesOfIndex[i];
		a[13].instancesOfIndex[a[13].num++] = num%10000;
	}
	else if(c == 'j'){
		a[16].index[a[16].num] = p;
		num = 0;
		for(int i=0 ; i<a[15].num ; i++)
			if(a[15].index[i]<p)
				num+=a[15].instancesOfIndex[i];
		a[16].instancesOfIndex[a[16].num++] = num%10000;
	}
	else if(c == 'a'){
		a[17].index[a[17].num] = p;
		num = 0;
		for(int i=0 ; i<a[16].num ; i++)
			if(a[16].index[i]<p)
				num+=a[16].instancesOfIndex[i];
		a[17].instancesOfIndex[a[17].num++] = num%10000;
	}

	return 0;
}