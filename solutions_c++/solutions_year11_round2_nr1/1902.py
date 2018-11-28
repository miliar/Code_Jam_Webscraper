#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

char sc[100][100];
int win[100];
int total[100];
double RPI[100];
double OWP[100];

int main(){

	int T;
	cin>>T;

	for (int i=0;i<T;i++){
		cout<<"Case #"<<i+1<<":";

		int N;
		cin>>N;

		for (int i=0;i<N;i++) win[i]=0;
		for (int i=0;i<N;i++) total[i]=0;
		for (int i=0;i<N;i++) RPI[i]=0.0;
		for (int i=0;i<N;i++) OWP[i]=0.0;


		for (int i=0;i<N;i++)
			for (int j=0;j<N;j++)
			{
				cin>>sc[i][j];	
				if (sc[i][j]=='1') {
					total[i]++;
					win[i]++;
				}
				else if (sc[i][j]=='0') total[i]++;
			}

		for (int i=0;i<N;i++){
			int n=0;
			double w=0.0;
			for (int j=0;j<N;j++){
				if (j==i || sc[j][i]=='.') continue;
				n++;
				int wi=0;
				if (sc[j][i]=='1') wi=1;
				w+=(double)(win[j]-wi)/(total[j]-1);
			}
			OWP[i]=w/n;
		}


		for (int i=0;i<N;i++)
		{
			double OOWP=0.0;
			int n=0;
			for (int j=0;j<N;j++){
				if (j==i || sc[j][i]=='.') continue;
				OOWP+=OWP[j];
				n++;
			}

			OOWP=OOWP/n;
			RPI[i]=0.25*(double)win[i]/total[i]+0.50*OWP[i]+0.25*OOWP;
		}
		cout<<endl;
		for (int i=0;i<N;i++) cout<<fixed<<setprecision(12)<<RPI[i]<<endl;
	}


	return 0;
}
