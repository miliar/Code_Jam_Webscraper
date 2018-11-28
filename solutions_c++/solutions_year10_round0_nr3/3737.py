#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

vector<int> groups;
int round,knum,num;

int total;

int main()
{
	int ncase;
	//cin>> ncase;
	int g;
	int pnum=0;

	char *filename="../C-small-attempt2.in";
	char *outfilename="../C-small-attempt2.out";
	
	ifstream infile;
	ofstream outfile;
	outfile.open(outfilename,ofstream::app);
	if(!outfile)
	{
		cerr<<"error: unalbe to open input file"<<outfile <<endl;
		return -1;

	}
	infile.open(filename,ifstream::app);
	if(!outfile)
	{
		cerr<<"error: unalbe to open input file"<<infile <<endl;
		return -1;
	}
	infile>>ncase;
	while(ncase--)
	{
		pnum++;
		total =0;
		//cin>>round>>knum>>num;
		infile>>round>>knum>>num;
		if(!groups.empty())
		{
			groups.clear();
		}
		for(int i=0;i<num;i++)
		{
			/*cin>>g;*/
			infile>>g;
			groups.push_back(g);
			
		}

		int curtime=0;
		int k=0;
		int temp=0,test;
		int numg=0;
		while(curtime<round)
		{
			k=k%num;
			test=temp+groups[k];
			if(test<=knum&&numg<num)
			{
				temp=test;
				numg++;
				k++;
			}
			else
			{
				total+=temp;
				temp=0;
				numg=0;
				curtime++;
			}
		}

		/*cout << "Case #"<<pnum<<":"<<" "<<total<<endl;*/
		outfile<<"Case #"<<pnum<<":"<<" "<<total<<endl;;
	}
	infile.close();
	outfile.close();
}