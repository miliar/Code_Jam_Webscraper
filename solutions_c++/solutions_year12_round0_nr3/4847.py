#include <limits>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

typedef struct pair{
	unsigned long long p1;
	unsigned long long p2;
}Pair;

class Recycled
{
	public:
		Recycled(){ mpA = NULL; mpB = NULL; mCount =0;} 
		void Construct()
		{ mpA = new unsigned long long[mT]; 
			mpB = new unsigned long long[mT];
			mpC = new int[mT];
		} 
		virtual ~Recycled() { delete [] mpA; delete []mpB; }

		ostream& operator<<(ostream & os);
		void Dump();
		void FileImport( const string& input_file_name );
		void Calculate();

		unsigned long long *mpA;
		unsigned long long *mpB;
		int *mpC;
		int mT;
		int mCount;
		std::multimap<string , unsigned long long> mSet;
};

#define SWAP_ROT(qA, len, kn) { qA[len] = qA[0]; \
for (int m=0;m<kn;m++) qA[m]=qA[m+1]; qA[kn] = qA[len]; qA[len]='\0';} 

void Recycled::Calculate()
{
	const char* file_name = "./Output.in";

	ofstream ofs(file_name);
	if (!ofs)
	{
		cerr << "The file " << file_name << " can not be opened!" << endl;
		return;
	}

	for (int i =0; i < mT; i++)
	{
		ofs << "Case #" << i+1 << ": ";
		cout << "Case #" << i+1<< ": ";

		char buff[200]; memset (buff, 0, sizeof(buff)); 
		sprintf(buff,"%lld",mpA[i]);
		int lenRot = strlen(buff);
		mCount = 0;

		for (unsigned long long j =mpA[i]; j <= mpB[i]; j++)
		{
			{
				sprintf(buff,"%lld",j);
				char oldbuff[200]; memset(oldbuff,0,sizeof(oldbuff));
				unsigned long long old = strtoll(buff,(char**)NULL,10);
				strcpy(oldbuff,buff);
				for (int l =0; l < lenRot - 1 ; l++)
				{
					SWAP_ROT(buff,lenRot, lenRot - 1);
					unsigned long long newNum = strtoll(buff,(char**)NULL,10);

					if (newNum > mpB[i] || newNum <= old || old < mpA[i] || newNum < mpA[i] || old > mpB[i])
						continue; 

					multimap <string, unsigned long long > :: iterator iter1;
					multimap <string, unsigned long long > :: iterator iter2;
					int found = 0;
					if((iter1 = mSet.find(buff)) != mSet.end())
					{
						iter2 = mSet.upper_bound(buff);
						for ( ; iter1 != iter2; ++iter1)
						{
							if ( iter1->second == old)
							{
								cout << "[=" << old << "," << strtoll(buff,(char**)NULL,10) << "=]" <<endl;
								found = 1; break;
							}
						} 
					}
					if (found) continue; found =0;
					if((iter1 = mSet.find(oldbuff)) != mSet.end())
					{
						iter2 = mSet.upper_bound(oldbuff);
						for ( ; iter1 != iter2; ++iter1)
						{
							if ( iter1->second == newNum)
							{
								cout << "[=" << old << "," << strtoll(buff,(char**)NULL,10) << "=]" <<endl;
								found = 1;break;
							}
						}
					}
					if (found ) continue;
					mCount++;
					mSet.insert(make_pair(oldbuff,newNum));
					mSet.insert(make_pair(buff,old));
					cout << "(" << old << "," << strtoll(buff,(char**)NULL,10) << ")" <<endl;
				}
			}
		}
		mpC[i] = mCount;
		cout << "+++" << mSet.size() << "+++" << endl;
		mSet.clear();
		ofs << mCount << endl;
		cout << mCount << endl;
	}
	ofs.close();
}

void Recycled::FileImport( const string& input_file_name )
{
	const char* file_name = input_file_name.c_str();

	ifstream ifs(file_name);
	if (!ifs)
	{
		cerr << "The file " << file_name << " can not be opened!" << endl;
		return;
	}

	//Start to read information from the input file. 
	//The first line has an probability to win 
	int tciter = 0;
	ifs >> mT;
	Construct();
	//In the following lines, each line contains a Number
	while(tciter < mT)
	{ 
		ifs >> mpA[tciter];
		ifs >> mpB[tciter];
		if  (mpA[tciter] == -1 || mpB[tciter] == -1) break;
		tciter++;
	}
	ifs.close();	
}
void Recycled::Dump()
{
	cout << "Testcases #" << mT << endl ;
	for (int i =0; i< mT;i++)
	{
		cout << "Testcase #" << i ;
		cout << " " << mpA[i];
		cout << " " << mpB[i];
		cout << endl;
	}
}

int main(int argc, char* argv[])
{
	cout << "Recycled" << endl;

	Recycled recycledSet;
	recycledSet.FileImport(argv[1]);
	recycledSet.Dump();
	recycledSet.Calculate();
}

