#include <iostream>

// basic file operations
#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream in ("input.in");
	ofstream out("output.out");
	
	int T;
	int N;
	int S;
	int p;
	int Case=0;

	in>>T;
	//while (!in.eof())
	for(Case = 1;Case<=T;Case++)
	{
		in>>N;
		in>>S;
		in>>p;

		int count=0;
		
		int count1=0; //possiblity for normal max 
		int count2=0; //possiblity for max with surprised triplet
		int curMax =0;

		for(int j=0;j<N;j++)
		{
			int total = 0;
			in>>total;

			int aver = total/3;
			int mod = total%3;
			
			if(aver==0 && mod==0 && p>0)
				continue;

			if ((aver+mod)>=p && (p<aver+2))
			{
				count1++;
				continue;
			}

			if (count2>=S)
				continue;
			
			if((mod<2) && (aver+1>=p))
				count2++;
			else if((mod ==2) &&(aver+2)>=p)
				count2++;
		}
		count = count1+count2;
		out<<"Case #"<<Case<<": "<<count<<endl;
	}
	in.close();
	out.close();
}