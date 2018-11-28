#include <iostream>
#include <fstream>
#include <string>

using namespace std;

main()
{
	string temp;
	ifstream in;
	in.open("B-large.in");
	ofstream out;
	out.open("OUTPUT.txt");
	int N;
	int f,c,i; //counters
	in >> N;
	char colon;
	for (f=1;f<=N;f++)
	{
		int A,B; //for input
		out<<"Case #" << f << ": ";
		//Initializing Board
		int Board[1439][2];
		for (c=0;c<2;c++)
			for(i=0;i<1439;i++)
				Board[i][c]=0;
		int T,NA,NB;
		in >> T >> NA >> NB;
		for (i=0;i<NA;i++)
		{
			in >> A;
			in >> colon;
			in >> B;
			for (c=((A*60)+B);c<1439;c++)
				Board[c][0]=Board[c][0]-1;
			in >> A;
			in >> colon;
			in >> B;
			for (c=A*60+B+T;c<1439;c++)
			Board[c][1]=Board[c][1]+1;
		}
		for (i=0;i<NB;i++)
		{
			in >> A;
			in.get(colon);
			in >> B;
			for (c=A*60+B;c<1439;c++)
				Board[c][1]=Board[c][1]-1;
			in >> A;
			in.get(colon);
			in >> B;
			for (c=A*60+B+T;c<1439;c++)
				Board[c][0]=Board[c][0]+1;
		}
		int INA=Board[0][0];
		int INB=Board[0][1];
		for (i=1;i<1439;i++)
		{
			if (Board[i][0]<INA)
				INA=Board[i][0];
			if (Board[i][1]<INB)
				INB=Board[i][1];
		}
		out << abs(INA) << " " << abs(INB) << endl;
	}
	return 0;
}