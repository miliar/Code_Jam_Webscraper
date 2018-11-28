#include <iostream>
#include <fstream>

using namespace std;

int caltruthlowlimit(int N,int P)
{
	int lower=P-1;
	if(lower<0)
		lower=0;
	return P+lower*(N-1);
}

int calsurprisinglowlimit(int N,int P)
{
	int lower=P-2;
	if(lower<0)
		lower=0;
	return P+lower*(N-1);
}

int main(int argc,char * argv[])
{
	int casenumber;
	int N,S,P;
	int truthnumber,surprisingnumber;
	int truthlimit,surprisinglimit;
	int score;
	ifstream infile("B-large.in");
	ofstream outfile("result.txt");
	string readresult;
	if(infile&&outfile)
	{
		infile>>casenumber;
		for(int i=0;i<casenumber;i++)
		{
			truthnumber=0;
			surprisingnumber=0;
			infile>>N>>S>>P;
			truthlimit=caltruthlowlimit(3,P);
			surprisinglimit=calsurprisinglowlimit(3,P);
			for(int k=0;k<N;k++)
			{
				infile>>score;
				if(score>=truthlimit)
					truthnumber++;
				else if(score>=surprisinglimit)
					surprisingnumber++;
			}
			if(surprisingnumber>S)
				surprisingnumber=S;
			outfile<<"Case #"<<i+1<<": "<<truthnumber+surprisingnumber<<endl;
		}
		infile.close();
		outfile.close();
	}
	return 0;
}
