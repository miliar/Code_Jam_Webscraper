#include<iostream> 
#include<cstdio>
#include<fstream>
using namespace std;

int main()
{
	int n , t , T , N;
	int i;
	int minn = 0;	//�����̤p��candy�]
	int summ = 0;	//�����`�@�X���} 
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
		minn = 1000002;	//�u�n > 10��������Y�i
		for( i = 0 ; i < 24 ; ++i )
			bin_sum[i] = 0; 
			

		for( n = 0 ; n < N ; ++n )
		{
			fin >> input;
			summ += input;
			if( minn > input )
				minn = input;
			//��Ҧ����Ʀr���ন2�i��A�ñq�̤p��ƶ}�l�sex. 10 ����ܬ�1010���N�|������0101�A�]�������D�̤j�|��ĴX��� 
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
