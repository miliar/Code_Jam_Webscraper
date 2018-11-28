#include <iostream>
#include <fstream>

using namespace std;

void main()
{
	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	if(fin == NULL){
		cout << "error" << endl;
		return ;
	}

	int T;
	fin >> T;


	for(int cnt=0; cnt<T; cnt++)
	{
		int N, K, onoff=0;
		int v=0, temp;
		
		fin >> N >> K;
		
		temp = 1;
		for(int i=0; i<N; i++)
			temp = temp + temp;
		
		while(K>temp)
			K = K - temp;

		v = K - (temp-1);

		if(v == 0) onoff=1;
		

		if(onoff==0)
			fout << "Case #" << cnt+1 << ": OFF" << endl;
		else
			fout << "Case #" << cnt+1 << ": ON" << endl;
	}
}