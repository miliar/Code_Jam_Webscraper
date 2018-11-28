#include <fstream>
using namespace std;
int main()
{
	char mapArray[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	ifstream infile("F:\\A-small-attempt2.in");
	ofstream outfile("output.txt");
	char tempArray[102]={0};
	
	infile.getline(tempArray,100);
	int ival = tempArray[0] - 48;
	if (tempArray[1] !=0)
	{
		ival = ival*10 + (tempArray[1] -48);
	}
  	int times = 1;
	while(ival)
	{
		infile.getline(tempArray,102);
		char outArray[102]={0};
		for (int i = 0;i < 102;++i)
		{
			if (tempArray[i]>='a'&&tempArray[i]<='z')
			{
				 outArray[i]=mapArray[tempArray[i]-97];
				 continue;
			}
			
			outArray[i] = ' ';
			if (tempArray[i] ==0)
				break;
		}
		outfile << "Case #"<< times << ": "<< outArray <<'\n';
		ival--;
		times++;
	}
	infile.close();
	outfile.close();
}