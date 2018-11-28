
//

#include <iostream>

using namespace std;

int n;
int table[100][100];
double rpi[100];
double wp[100];
double owp[100];
double oowp[100];
int win[100];
int ngame[100];

void compute(){
	int i,j,k;
	for (i=0;i<n;i++){
		rpi[i]=0;
		wp[i]=0;
		owp[i]=0;
		oowp[i]=0;
		win[i]=0;
		ngame[i]=0;
	}
	for (i=0;i<n;i++){
		for (j=0;j<n;j++){
			if (table[i][j]>=0) ngame[i]++;
			if (table[i][j]==1) win[i]++;
		}
		wp[i]=win[i]*1.0/ngame[i];
	}

	//owp
	for (i=0;i<n;i++){
		double owptmp=0;
		int count=0;
		for (j=0;j<n;j++){
			if (table[i][j]>=0){
				//printf("owp %d %d %d %d %d\n",i,j,table[i][j],win[j],ngame[j]);
				count++;
				owptmp+= (win[j]-!table[i][j])*1.0/(ngame[j]-1);
			}
		}
		owp[i]=owptmp/count;
	}

	//oowp
	for (i=0;i<n;i++){
		double oowptmp=0;
		int count=0;
		for (j=0;j<n;j++){
			if (table[i][j]>=0){
				count++;
				oowptmp+= owp[j];
			}
		}
		oowp[i]=oowptmp/count;
	}

	for (i=0;i<n;i++){
		rpi[i]=0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
	}
}

int main(){
	int t;
	int i,j,k;
	char ch;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>n;
		for (j=0;j<n;j++){
			for (k=0;k<n;k++){
				cin>>ch;	
				if (ch=='.') table[j][k]=-1;
				else if (ch=='0') table[j][k]=0;
				else if (ch=='1') table[j][k]=1;
			}
		}
		compute();
		cout<<"Case #"<<(i+1)<<":"<<endl;
		//for (j=0;j<n;j++) cout<<rpi[j]<<endl;
		for (j=0;j<n;j++) printf("%.12f\n",rpi[j]);
		//for (j=0;j<n;j++) printf("%f %f %f %.10f\n",wp[j],owp[j],oowp[j],rpi[j]);
	}
}
