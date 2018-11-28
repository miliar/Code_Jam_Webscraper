
#include <iostream>
#include <fstream>
using namespace std;

void main()
{
	fstream infile, outfile;
	infile.open("input.txt");
	outfile.open("output.txt", ios::out);
	int T, N, S, P;
	infile>>T;
	for (int k = 1; k <= T; k++)
	{
		infile>>N>>S>>P;
		int t[100];
		memset(t, 0, 100 * sizeof(int));
		for (int i = 0; i < N; i++)
			infile>>t[i];
/*
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
*/
		int base = (P * 3 - 4);
		switch(base)
		{
		case -1:
			base = 1;
			break;
		case -4:
			base = 0;
			break;
		default:
			break;
		}
		outfile<<"Case #"<<k<<": ";
		if (base == 0)
			outfile<<N;
		else{
			int num = 0, equal = 0;
			for (int i = 0; i<N; i++)
			{
				if (t[i] == base || (base != 1 && t[i] == base + 1))
					equal++;
				else if (t[i] > base)
					num++;
			}
			if (base != 1)
			{num +=((equal < S) ? equal : S);
				outfile<<num;
			}
			else
				outfile<<num+equal;

		}
					if (k < T)
				outfile<<endl;
	}
	infile.close();
	outfile.close();
	cout<<"ok"<<endl;
}