#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ofstream output("2.output");
	if(output)
	{
		int cases;
		cin >> cases;
		for(int iterations=0; iterations<cases; iterations++)
		{
			int N, S, p;
			int counter(0);
			int specials(0);
			int normals(0);
			int correction(0);
			int val(0);
			cin >> N >> S >> p;
			if(p > 1)
			{
				for(int i=0; i<N; i++)
				{
					int tmp(0);
					cin >> tmp;
					if(tmp >= 3*p-2)
					{
						counter++;
						normals++;
					}
					else if(tmp >= 3*p-4 && specials < S)
					{
						counter++;
						specials++;
					}

				}
				if(normals > N-S) {
					correction = 1;
					int tmp = -N+S+normals;
					val = tmp;
					specials += tmp;
					if(specials > S)
						counter -= specials-S;
				}
			}
			else if(p==1)
			{
				for(int i=0; i<N; i++)
				{
					int tmp;
					cin >> tmp;
					if(tmp > 0)
						counter++;
				}
			}
			else if(p==0)
			{
				int tmp;
				for(int i=0; i<N; i++)
					cin >> tmp;
				counter = N;
			}
			output << "Case #" << iterations+1 << ": " << counter << endl;
		}
		return 0;
	}
	return 1;
}
