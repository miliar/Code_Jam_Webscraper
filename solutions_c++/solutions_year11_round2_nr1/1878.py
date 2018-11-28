#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
using namespace std;

int pl[101][101];

double wp(int p, int n){
	int sum=0;
	int num=0;
	for(int i=0;i<n;i++){
		int temp = pl[p][i];
		if(temp == 1) sum++;
		if(temp != 0) num++;
	}
	if (num == 0) return 0;
	return (double)sum/num;
}

double wpWithout(int p, int without, int n){
	int sum=0;
	int num=0;
	for(int i=0;i<n;i++){
		if(i==without)continue;
		int temp = pl[p][i];
		if(temp == 1) sum++;
		if(temp != 0) num++;
	}
	if (num == 0) return 0;
	return (double)sum/num;
}

double owps[101];
double owp(int p, int n){
	double sum=0;;
	int num=0;
	for(int i=0; i<n; i++){
		if(pl[p][i]==0)continue;
		num++;
		sum+=wpWithout(i,p,n);
	}
	if(num==0){
		owps[p]=0.0;
		return 0.0;
	}
	owps[p]=sum/num;
	return sum/num;
}

double oowp(int p, int n){
	double sum=0.0;
	int num =0;
	for(int i=0; i<n; i++){
		if(pl[p][i]==0) continue;
		num++;
		sum+= owps[i];
	}
	return sum/num;
}

double res[101];


int main(int argc, char ** argv)
{
#ifdef KOMPA_NA_MISHO
	freopen ("in.txt","r",stdin);
#endif
	/////////////////////////////Code goes here:
	int T;
	cin>>T;
	for(int tt=1; tt<=T; tt++){
		int n;
		cin>>n;
		vector<string> playss(n);
		
		for(int i=0; i<n; i++){
			cin>>playss[i];
			for(int j=0; j<n; j++){
				if(playss[i][j] == '.')
					pl[i][j]=0;
				else if(playss[i][j] == '1')
					pl[i][j]=1;
				if(playss[i][j] == '0')
					pl[i][j]=-1;
			}
		}
		cout<<"Case #"<<tt<<":\n";
		//for(int i=0; i<n; i++){
		//	//for(int j=0; j<n; j++)
		//	//	cout<<" "<<pl[i][j];
		//	cout<<owp(i,n);
		//	cout<<"\n";
		//}
		//for(int i=0; i<n; i++){
		//	//for(int j=0; j<n; j++)
		//	//	cout<<" "<<pl[i][j];
		//	cout<<oowp(i,n);
		//	cout<<"\n";
		//}
		
		for(int i=0; i<n; i++)
			res[i] = 0.25 * wp(i,n);
		for(int i=0; i<n; i++)
			res[i] += 0.5 * owp(i,n);
		for(int i=0; i<n; i++)
			res[i] += 0.25 * oowp(i,n);
		for(int i=0; i<n; i++)
			cout<<setprecision(10)<<res[i]<<endl;
		
		
	}


	////////////////////////////////////////////
#ifdef KOMPA_NA_MISHO
	fclose (stdin);
#endif
	return 0;
}