#include<iostream>
#include<fstream>

using namespace std;

void main()
{
	ifstream input("input.txt");
	ofstream output("output.txt");

	int T;	//Test Count Number;
	int N;	//Task Count Number;
	int P[101];	// Button Locate
	char R[101];	// Robot Color


	input>>T;

	for(int i=1; i<=T; i++)
	{
		//read N
		input>>N;

		int orange = 1;
		int blue = 1;
		int answer = 0;

		int OData[101];	//Orange Queue	
		int BData[101];	//Blue Queue
		int OCount=0;
		int BCount=0;

		//read One Line other Data
		for(int j=0; j<N; j++)
		{
			input>>R[j]>>P[j];
			
			if(R[j] == 'O')
				OData[OCount++] = P[j];
			else
				BData[BCount++] = P[j];
		}
		//read end

		int oi, bi, current, push;
		oi=bi=current=0;

		while(oi < OCount || bi < BCount)
		{
			push = 0;
			if(bi < BCount)
			{
				if(blue == BData[bi])
				{
					if(R[current] == 'B')
					{
						bi++;		//if orange push, don't blue push
						push = 1;
						current++;
					}
				}
				else
				{
					if(blue < BData[bi])
						blue++;
					else if(blue > BData[bi])
						blue--;
				}
			}
			
			if(oi < OCount)
			{
				if(orange == OData[oi])
				{
					if(R[current] == 'O' && push != 1)		//if blue push, don't orange push
					{
						oi++;
						current++;
					}
				}
				else
				{
					if(orange < OData[oi])
						orange++;
					else if(orange > OData[oi])
						orange--;
				}
			}

			answer++;
		}


		output<<"Case #"<<i<<": "<<answer<<endl;
	}
	
	input.close();
	output.close();
}