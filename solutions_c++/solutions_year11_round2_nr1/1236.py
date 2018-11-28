#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define IN fin
#define OUT fout

int main()
{
	ofstream fout("A.out");
	ifstream fin("A.in");
	int T;
	IN>>T;
	for(int t=1;t<=T;t++)
	{
		int N;
		IN>>N;
		string data[101];
		int count[101];
		double WP[101], OWP[101], OOWP[101], RPI[101];
		for(int i=0;i<N;i++)    IN>>data[i];
		for(int i=0;i<N;i++)
		{
			//WP
			count[i] = 0;
			WP[i] = 0;
			for(int j=0;j<N;j++)    if(data[i][j] != '.')
			{
				count[i] ++;
				WP[i] += (data[i][j] == '1');
			}
			WP[i] /= (count[i] + 0.0);
		}
		for(int i=0;i<N;i++)
		{
			//OWP
			OWP[i] = 0;
			for(int j=0;j<N;j++)    if(data[i][j] != '.')
			{
				OWP[i] += ( WP[j] - (('1' - data[i][j]) * 1.0 / count[j]) ) * count[j] / (count[j] - 1.0);
			}
			OWP[i] /= (count[i] + 0.0);
		}
		for(int i=0; i<N;i++)
		{
			OOWP[i] = 0;
			for(int j=0;j<N;j++)    if(data[i][j] != '.')
			{
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= (count[i] + 0.0);
		}
		for(int i=0; i<N;i++)   RPI[i] = 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i];
		
		OUT<<"Case #"<<t<<":\n";
		for(int i=0;i<N;i++)    OUT<<RPI[i]<<"\n";
	}
	return 0;
}
