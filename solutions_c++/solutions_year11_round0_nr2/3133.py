#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


//{Q, W, E, R, A, S, D, F}
vector<char> theOutput;
unsigned int combine[90][2];
unsigned int oppose[90];
unsigned int causeClear[90];

int main()
{

	int T,C,D,N;
	ifstream in;
	ofstream out;

	in.open("input.txt");
	out.open("output.txt");


	in >> T;
	for ( int i=0;i<T;i++)
	{
		theOutput.clear();
		for (int p=0;p<90;p++)
		{
			combine[p][0] = 0;
			combine[p][1] = 0;
			oppose[p] = 0;
			causeClear[p] = 0;
		}
		in >> C;
		char temp[3];
		for ( int j=0;j<C;j++)
		{
			in >> temp[0];
			in >> temp[1];
			in >> temp[2];
			combine[(int)temp[0]][0] = (int)temp[1];
			combine[(int)temp[0]][1] = (int)temp[2];
		}
		in >> D;
		for (int k=0;k<D;k++)
		{
			in >> temp[0];
			in >> temp[1];
			oppose[(int)temp[0]] = temp[1];
			oppose[(int)temp[1]] = temp[0];
		}

		in >> N;
		theOutput.reserve(N);
		char theLast = 91;
		for (int l = 0;l<N;l++)
		{
			in >> temp[0];
			if ( (unsigned int)theLast == combine[(int)temp[0]][0] )
			{
				theOutput.pop_back();
				theOutput.push_back((char)combine[(int)temp[0]][1]);
				causeClear[oppose[(int)theLast]]--;
				theLast = 91;
			}
			else if ( combine[(int)theLast][0] == (unsigned int)temp[0])
			{
				theOutput.pop_back();
				theOutput.push_back((char)combine[(int)theLast][1]);
				causeClear[oppose[(int)theLast]]--;
				theLast = 91;
			}
			else if ( causeClear[(int)temp[0]] )
			{
				theLast = 91;
				theOutput.clear();
				for(int q=0;q<90;q++)
				{
					causeClear[q] = 0;
				}
			}
			else{
				theOutput.push_back(temp[0]);
				causeClear[oppose[(int)temp[0]]]++;
				theLast = temp[0];
			}
		}
		out << "Case #" <<i+1<<": [";
		for (int y=0;y<theOutput.size();y++)
		{
			if( y!= 0 )
			{
				out << ", " << theOutput[y];
			}
			else
			{
				out<<theOutput[y];
			}
		}
		out <<"]"<<endl;
	}
}
