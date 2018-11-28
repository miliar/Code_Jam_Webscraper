#include <fstream>
#include <iostream>
#include <cstring>

using namespace std;

/*ifstream fin("GCJ P A.in");
ofstream fout("GCJ P A.out");

#define cin fin
#define cout fout*/

int n,t;
char match[110][110];
double wp[110],owp[110],oowp[110];
int w[110],tot[110];

void clear(){
	memset(match,0,sizeof(match));
	memset(wp,0,sizeof(wp));
	memset(owp,0,sizeof(owp));
	memset(oowp,0,sizeof(oowp));
	memset(w,0,sizeof(w));
	memset(tot,0,sizeof(tot));
}

void init(){
	cin >> n;
	char p;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			do{
				cin >> p;
			}while(p=='\n');
			switch(p){
				case '1':
					w[i]++;
					//no break
				case '0':
					tot[i]++;
					//no break
				default:
					match[i][j]=p;
					//no break
			}
		}
		//cout << "Wi " << w[i] << " TOTi " << tot[i] <<  endl;
		wp[i]=((double)w[i])/tot[i];
	}
}

void process(){
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			switch(match[i][j]){
				case '1':
					owp[i]+=(double)w[j]/(double)(tot[j]-1);
					break;
				case '0':
					owp[i]+=(double)(w[j]-1)/(double)(tot[j]-1);
					break;
			}
				
		}
		owp[i]/=tot[i];
	}
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			if(match[i][j]!='.')
				oowp[i]+=owp[j];
		}
		oowp[i]/=tot[i];
		//cout << "WPI " << wp[i] << " OWP " << owp[i] << " OOWP " << oowp[i] << endl;
		cout << 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] << endl;
	}
}

int main(){
	cin >> t;
	for(int i=0;i<t;i++){
		cout << "Case #" << i+1 << ':' << endl;
		clear();
		init();
		process();	
	}
	return 0;
}
