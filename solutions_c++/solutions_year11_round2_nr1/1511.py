#include<cstdio>
#include<algorithm>
#include<set>
#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<memory.h>
#include<cstdlib>
#include<map>
#include<cmath>
using namespace std;

char tab[1010][1010];
long double x[1010][3];
int n,m,a,b,t;

int main(){
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		scanf("%d", &n);
		for(int j = 0; j < n; j++){
			for(int k = 0; k < n; k++){
				cin>>tab[j][k];
			}
		}
		for(int j = 0; j < n; j++){
			long double ile_1 = 0;
			long double how_much = 0;
			for(int k = 0; k < n; k++){
				if(tab[j][k] == '1'){ile_1++;how_much++;}
				else if(tab[j][k] == '0')how_much++;
			}
			//printf("ile = %d how = %d \n", ile_1, how_much);
			long double wynik = (double)(ile_1/how_much);
			//cout<<wynik<<endl;
			x[j][0] = wynik;
		}
		for(int j = 0; j < n; j++){
			long double wynik = 0;
			//cout<<"team " << j << " : " ;
			double ile_jest = 0;
			for(int k = 0; k < n; k++){
				long double ile_1 = 0, how_much = 0; 
				if(k==j)continue;
				if(tab[k][j] == '.')continue;
				ile_jest ++;
				for(int l = 0; l < n; l++){
					if(l == j)continue;
					if(tab[k][l] == '1'){ile_1++; how_much++;}
					else if(tab[k][l] == '0')how_much++;
				}
			//	cout <<" dodaje " << ile_1/how_much<< " " <<endl;
				wynik += (double)(ile_1/how_much);
			}
			//cout<<"Mam sume = " <<wynik<<endl;
			wynik /= ile_jest;
			x[j][1] = wynik;
			//cout<<"opw = " << wynik<<endl;
		}
		for(int j = 0; j < n; j++){
			long double wynik = 0;
			double ile_jest = 0;
			for(int k = 0; k < n; k++){
				if(tab[k][j] =='.')continue;
				ile_jest ++;
				if(k!=j)
					wynik += x[k][1];
				
			}
			//cout<<"mam " << wynik;
			x[j][2] = wynik/ile_jest;
		}
		cout<<"Case #"<<i+1<<":\n";
		for(int j = 0; j < n; j++){
			//cout<<j<<endl;
			//cout<<"wp : " <<x[j][0] << "owp " <<x[j][1] << " oowp : " << x[j][2]<<endl;
			long double rpi = 0.25*x[j][0] + 0.5*x[j][1] + 0.25*x[j][2];
			printf("%llf\n", rpi);
		}
	}
	return 0;
}

