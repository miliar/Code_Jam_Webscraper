#include<iostream>
#include<fstream>
using namespace std;

int inverse[1000];
char temp[1000];
int place;
void convert(long long n )
{
	place = 999;
	while( n > 0 )
	{
		inverse[ place--] = n%10;
		n/=10;
	}
}

int main()
{
	ofstream fout("out");
	int test;
	cin >> test;
	cin.getline(temp,1000);
	int Case = 1;
	while( test > 0 )
	{
		test --;
		for(int i=0;i<1000;i++)
			inverse[i] = 0;
		long long int n ;
		cin.getline(temp,1000);
		for(int i=999-strlen(temp)+1,k=0;i<=999;i++)
			inverse[i] = temp[k++]-'0';
		place = 999-strlen(temp);
		//convert( n );
		int rev = 999;
		for(int i=998;i>=place;i-- )
		{
			if( inverse[i] >= inverse[i+1] )
				rev = i;
			else
			{
				int tmp[1000],k;
				for(int j=999,k=0;j>=rev;j--)
					tmp[k++] = inverse[j];
				for(int j=rev,k=0;j<=999;j++)
					inverse[j] = tmp[k++];
				int Min = 99999;
				int p = -1;
				for(int j=rev;j<=999;j++)
					if( inverse[j] > inverse[rev-1] )
						if( inverse[j] < Min )
						{
							Min = inverse[j];
							p = j;
						}
				inverse[rev-1] ^= inverse[p] ^= inverse[rev-1] ^= inverse[p];
				break;
			}
		}
		fout << "Case #" << Case++ << ": ";
		for(int i=0;i<=999;i++)
			if( inverse[i] != 0 )
			{
				while( i <= 999 )
					fout << inverse[i++];
				fout << endl;
				break;
			}
	}
}