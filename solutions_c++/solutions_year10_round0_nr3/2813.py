#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream fin("C-small-attempt1.in");
	ofstream fout("out.txt");
	if(fin == NULL){
		cout << "error" << endl;
		return ;
	}

	int T;
	fin >> T;

	for(int cnt=0; cnt<T; cnt++)
	{
		int R, k, N;

		fin >> R >> k >> N;

		int gi[10] = {0,};

		for(int i=0; i<N; i++)
			fin >> gi[i];

		int pt=0;
		int total=0;
		for(int j=0; j<R; j++)
		{
			int sum=0;
			for(int y=0; y<N; y++){
				sum += gi[pt];
				total += gi[pt];
				if(sum > k)
				{
					sum -= gi[pt];
					total -= gi[pt];
					break;
				}
				pt++;				
				if(pt == N) pt=0;
				if(sum == k){ break; }
								
				
			}
		}
		fout << "Case #" << cnt+1 << ": " <<  total << endl;
	}
}