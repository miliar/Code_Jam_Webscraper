using namespace std;

#include <iostream>
#include <list>
#include <vector>

unsigned int inline add(unsigned int a, unsigned int b)
{/*
	return ((a & 0x10000) ^ (b & 0x10000)) |
		   ((a & 0x08000) ^ (b & 0x08000)) |
		   ((a & 0x04000) ^ (b & 0x04000)) |
		   ((a & 0x02000) ^ (b & 0x02000)) |
		   ((a & 0x01000) ^ (b & 0x01000)) |
		   ((a & 0x00800) ^ (b & 0x00800)) |
		   ((a & 0x00400) ^ (b & 0x00400)) |
		   ((a & 0x00200) ^ (b & 0x00200)) |
		   ((a & 0x00100) ^ (b & 0x00100)) |
		   ((a & 0x00080) ^ (b & 0x00080)) |
		   ((a & 0x00040) ^ (b & 0x00040)) |
		   ((a & 0x00020) ^ (b & 0x00020)) |
		   ((a & 0x00010) ^ (b & 0x00010)) |
		   ((a & 0x00008) ^ (b & 0x00008)) |
		   ((a & 0x00004) ^ (b & 0x00004)) |
		   ((a & 0x00002) ^ (b & 0x00002)) |
		   ((a & 0x00001) ^ (b & 0x00001));*/
	return a^b;
}

unsigned int inline powOfTow(unsigned int a)
{
	unsigned int i = 21;
	while(((a >> i) & 0x00001) == 0x00)
	{
		i--;
	}
	return i;
}

//#define TEST
//#define SMALL
#define LARGE
int main(void) {
#ifdef TEST
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

#ifdef SMALL
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif

	int T;
	int N;

	int C;
	list<unsigned int> listC;

	int y;

	cin >> T;

	for(int i=0; i<T; i++){
		cin >> N;
		listC.clear();

		unsigned int sum = 0;
		for(int j=0; j<N; j++)
		{
			cin >> C;
			listC.push_back(C);
			sum = add(sum, C);
		}

		if(sum!=0)
		{		
			cout << "Case #" << (i+1) << ": NO" << endl;
		}
		else
		{
			listC.sort();
			for(int j = 0; j<N-1; j++)
			{
				sum +=listC.back();
				listC.pop_back();
			}

			cout << "Case #" << (i+1) << ": " << sum << endl;
		}
		
	}
	return 0;
}
