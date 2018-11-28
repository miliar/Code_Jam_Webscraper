#include <fstream>
#include <string>
using namespace std;

class group
{
	public:
	group * nextGroup;
	int groupSize;
};

int main()
{
	ifstream inputFile;
    inputFile.open( "input.txt", ios_base::in );
	ofstream outputFile;
    outputFile.open("output.txt", ios_base::out);
	int testCase;
	inputFile>>testCase;
	for(int i = 0;i<testCase;i++)
	{
		long int R,K,N;
		inputFile>>R;
		inputFile>>K;
		inputFile>>N;
		group * root = new group();
		inputFile>>(root->groupSize);
		group * cursor = root;
		for(int j = 1;j<N;j++)
		{
			cursor->nextGroup = new group();
			cursor = cursor->nextGroup;
			inputFile>>cursor->groupSize;
		}
		cursor->nextGroup = root;
		int totalPrice = 0;
		cursor = root;
		
		for(int j=0;j<R;j++)
		{
			group * startingGroup = cursor;
			int seats = 0;
			bool start = true;
			while(startingGroup!=cursor || start)
			{
				start = false;
				if ((cursor->groupSize+seats)>K)
					break;
				else
				{
					seats += cursor->groupSize;
					cursor = cursor->nextGroup;
				}
			}
			totalPrice += seats;
		}

		outputFile<<"Case #"<<(i+1)<<": "<<totalPrice<<endl;
	}
	return 0;
}