#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

int main(int argc, char** argv)
{
	int t;
	FILE *f = fopen(argv[1], "rt");
	fscanf(f, "%d", &t);
	int crt = 0;
	
	while(crt<t)
	{
		int n;
		fscanf(f, "%i", &n);
		vector<pair<int, int> > wires;
		int ret=0;
		
		while(n)
		{
			int m,l;
			fscanf(f, "%i %i", &m, &l);
			
			for (unsigned int i=0;i<wires.size();i++)
			{
				if (m<wires[i].first && l>wires[i].second)
					ret++;
				if (m>wires[i].first && l<wires[i].second)
					ret++;
			}
			wires.push_back(make_pair(m,l));
			n--;
		}
		printf("Case #%i: %i\n", ++crt, ret);
	}
	
	return 0;
}
