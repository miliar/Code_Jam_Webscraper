#include<iostream>
#include<fstream>
using namespace std;

struct skip
{
	long total;
	long skip;
};

//Prototypes
void buildSkipTable(ifstream&, long, long);
void printSkipTable(long);

skip* skipTable;

int main(int argc, char* argv[])
{
	ifstream ifs;
	int cases;
	long rides, rsize, groups, profit, pos;

	ifs.open(argv[1]);

	ifs >> cases;

	for(int i = 1; i <= cases; i++)
	{
		profit = 0;
		pos = 0;
		
		ifs >> rides >> rsize >> groups;
		//Build the table for the next data set
		buildSkipTable(ifs, rsize, groups);
		//printSkipTable(groups);
		
		for(long j = 0; j < rides; j++)
		{
			profit += skipTable[pos].total;
			pos = ((pos + skipTable[pos].skip) % groups);
		}	
		
		cout << "Case #" << i << ": " << profit << endl;	
	}
	ifs.close();

	return 0;	
}

void buildSkipTable(ifstream& ifs, long rsize, long groups)
{
	//delete if it already exists
	if(skipTable != NULL) delete [] skipTable;
	
	//allocate and read in data
	skipTable = new skip[groups];
	long* group = new long[groups];
	for(long i = 0; i < groups; i++)
		ifs >> group[i];

	long skip, count, pos = 0, next;
	//build the table
	for(long i = 0; i < groups; i++)
	{
		skip = 0, count = 0, pos = i;
		next = group[pos];
		do
		{
			count += next;
			pos = (pos+1) % groups;	
			next = group[pos];
			skip++;	
		} while(skip < groups && (count + next) <= rsize);
	
		skipTable[i].total = count;
		skipTable[i].skip = skip;	
	}
	delete [] group;
}

void printSkipTable(long groups)
{
	for(long i = 0; i < groups; i++)
	{
		printf("index: %ld, total: %ld, skip: %ld\n", i, skipTable[i].total, skipTable[i].skip);	
	}	
}
