#include<fstream>
#include<iostream>

using namespace std;

int main()
{
	int t, tc=1;
	int number, surprise, least;
	int avg=0;
	int normal;
	int i=0;

	ifstream infile;
	infile.open("B-large.in");
	infile >> t;

	for( ; tc <=t; ++tc)
	{
		int ctr=0;

		infile >> number; infile >> surprise; infile >> least;
	//	cin>>number>>surprise>>least;
		int score[number];
		normal = number-surprise;

		for(i=0; i<number; ++i)
			infile >> score[i];

		for(i=0; i<number; ++i)
			for(int j =i+1; j<number; ++j)
				if(score[i]<score[j])
				{
					int temp;
					temp = score[i];
					score[i] = score[j];
					score[j] = temp;
				}


		for(i=0; i<number; ++i)
		{
			int cs=score[i];	//current score
			avg = cs/3;

			if(avg>=least)
			{
				if (normal==0)
					surprise--;

				ctr++;
			}
			
			else if(cs >= least*3-2)
			{
				if (normal==0)
					surprise--;

				ctr++;
			}
			
			else if(cs >= (least*3 - 4))
			{
				if(cs!=0 && cs!=1 && cs!=29 && cs!=30 && surprise>0)
				{
					surprise--;
					ctr++;
				}
			}

		
		}


		cout<<"Case #"<<tc<<": "<<ctr<<endl;
	}

	infile.close();

	return 0;

}

