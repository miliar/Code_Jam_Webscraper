#include<iostream> 
#include<cstdio>
#include<fstream>
using namespace std;

int main()
{
	int n , t , T , N;
	int i;
	int minn = 0;	//魁程candy
	int summ = 0;	//魁羆碭聋縸 
	int bin_sum[24];
	int input;
	bool crying = false; 

	ifstream fin ("C-large.in");
	ofstream fout ("C-large.out");

	fin >> T;
	for( t = 1 ; t <= T ; ++t )
	{
		fin >> N;
		summ = 0;
		minn = 1000002;	//璶 > 10せΩよ
		for( i = 0 ; i < 24 ; ++i )
			bin_sum[i] = 0; 
			

		for( n = 0 ; n < N ; ++n )
		{
			fin >> input;
			summ += input;
			if( minn > input )
				minn = input;
			//р┮Τ计常锣Θ2秈眖程计秨﹍ex. 10 莱ボ1010碞穦魁0101ぃ笵程穦材碭计 
			for( i = 0 ; input != 0 ; ++i )
			{
				bin_sum[i] += input%2;
				input =  input/2; 
			} 
		}
		crying = false; 
		for( i = 0 ; i < 24 ; ++i )
		{
			if(    bin_sum[i] % 2  ==  1    )
			{ 
				crying = true;
				break; 
			} 
		}
		fout << "Case #" << t << ": ";
		if( crying == true )
			fout << "NO" << endl;
		else
			fout << summ - minn << endl; 
	}//end while(cin)
}
