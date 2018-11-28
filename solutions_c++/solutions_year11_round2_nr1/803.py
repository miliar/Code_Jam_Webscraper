#include <fstream>
using namespace std;

ifstream input("input.txt");
ofstream output("output.txt");
int n;
char games[110][110];
double wp[100];
double owp[100];
double oowp[100];
int wins[100];
int loses[100];

int main()
{
	int t;
	input >> t;
	output.precision(10);
	for (int i=0;i<t;++i)
	{
		memset(wins, 0, sizeof(wins));
		memset(loses, 0, sizeof(loses));
		input >> n;
		for (int j=0;j<n;++j) wp[j] = owp[j] = oowp[j] = 0;
		for (int j=0;j<n;++j)
		{			
			input >> games[j];
			for (int k=0; k<n; ++k)
			{
				if (games[j][k] == '0') ++loses[j];
				else if (games[j][k] == '1') ++wins[j];
			}
			wp[j] = ((double)wins[j])/(wins[j]+loses[j]);
			for (int k=0; k<n; ++k)
			{
				if (games[j][k]!='.')
				{
					owp[k] += ((double)(wins[j]-((games[j][k]=='1')?1:0))) / (wins[j]+loses[j]-1);
				}
			}
		}
		for (int j=0;j<n;++j)
		{
			owp[j]/=(double)(wins[j]+loses[j]);
		}
		for (int j=0;j<n;++j)
		{
			for (int k=0;k<n;++k)
				if (games[j][k]!='.')
					oowp[j]+=owp[k];
			oowp[j]/=(double)(wins[j]+loses[j]);
		}		
		output << "Case #" << i+1 << ":" << endl;
		for (int j=0; j<n;++j)
			output << 0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j] << endl;
	}
	return 0;
}