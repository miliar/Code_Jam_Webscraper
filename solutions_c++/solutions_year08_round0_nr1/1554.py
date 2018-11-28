#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

string sengnames[101];
int sengcnt;

string qterms[1001];
int qtermcnt;

int posmin[1001];

int solveprob();

class srectype{
	public:
	int pos;   // position  
	int eng;   // which search engine
	int cnt;   // how many switches

	bool operator<(const srectype & xx)
	{
		return cnt > xx.cnt;
	}
};


int main()
{
	int probcnt;
	char buffer[512];
	
	cin.getline(buffer, 512);

	sscanf(buffer, "%d", &probcnt);

	for(int i=1;i<=probcnt;i++)
	{

		cin.getline(buffer, 512);
		sscanf(buffer, "%d", &sengcnt);

		for(int y=0;y<sengcnt;y++)
		{

			cin.getline(buffer, 512);
			sengnames[y] = buffer;
		}

		cin.getline(buffer, 512);
		sscanf(buffer, "%d", &qtermcnt);

		for(int y=0;y<qtermcnt;y++)
		{	
			cin.getline(buffer, 512);
			qterms[y] = buffer;

			posmin[y] = 0;
		}

		cout << "Case #" << i << ": " << solveprob() << endl;
	}

	return 0;
}



vector<srectype> srecords;

//brute force search
int solveprob()
{
	int count = -1;
	srectype crec;

	srecords.clear();

	crec.pos = -1;
	crec.eng = -1;
	crec.cnt = -1;
	srecords.push_back(crec);

	while(srecords.size() != 0)
	{
		pop_heap(srecords.begin(), srecords.end());
		crec = srecords.back();
		srecords.pop_back();

		if( crec.pos == qtermcnt )
		{
			count = crec.cnt;
			break;
		}

		if ( posmin[crec.pos] < crec.eng)
			posmin[crec.pos] = crec.eng;

		crec.pos++;

		int thiseng = crec.eng;

		if( thiseng != -1 && sengnames[thiseng].compare(qterms[crec.pos]) != 0) 
		{
			// no conflict
			// we can just use this one

			srecords.push_back(crec);
			make_heap(srecords.begin(), srecords.end());

		} else {
			// we must use a new one
			crec.cnt++;
			for(int i = posmin[crec.pos];i<sengcnt;i++) {

				if( sengnames[i].compare(qterms[crec.pos]) == 0) 
					continue;
	
				crec.eng = i;
				srecords.push_back(crec);
				make_heap(srecords.begin(), srecords.end());
			}
		}

	}

	return count;
}
