#include<iostream>
using namespace std;

struct data{
	int n_surprise;
	int surprise;
};

int main(){
	data d[31];

	d[0].n_surprise=0;
	d[0].surprise=0;
	d[1].n_surprise=1;
	d[1].surprise=1;
	d[2].n_surprise=1;
	d[2].surprise=2;
	d[3].n_surprise=1;
	d[3].surprise=2;
	d[4].n_surprise=2;
	d[4].surprise=2;
	d[5].n_surprise=2;
	d[5].surprise=3;
	d[6].n_surprise=2;
	d[6].surprise=3;
	d[7].n_surprise=3;
	d[7].surprise=3;
	d[8].n_surprise=3;
	d[8].surprise=4;
	d[9].n_surprise=3;
	d[9].surprise=4;
	d[10].n_surprise=4;
	d[10].surprise=4;
	d[11].n_surprise=4;
	d[11].surprise=5;
	d[12].n_surprise=4;
	d[12].surprise=5;
	d[13].n_surprise=5;
	d[13].surprise=5;
	d[14].n_surprise=5;
	d[14].surprise=6;
	d[15].n_surprise=5;
	d[15].surprise=6;
	d[16].n_surprise=6;
	d[16].surprise=6;
	d[17].n_surprise=6;
	d[17].surprise=7;
	d[18].n_surprise=6;
	d[18].surprise=7;
	d[19].n_surprise=7;
	d[19].surprise=7;
	d[20].n_surprise=7;
	d[20].surprise=8;
	d[21].n_surprise=7;
	d[21].surprise=8;
	d[22].n_surprise=8;
	d[22].surprise=8;
	d[23].n_surprise=8;
	d[23].surprise=9;
	d[24].n_surprise=8;
	d[24].surprise=9;
	d[25].n_surprise=9;
	d[25].surprise=9;
	d[26].n_surprise=9;
	d[26].surprise=10;
	d[27].n_surprise=9;
	d[27].surprise=10;
	d[28].n_surprise=10;
	d[28].surprise=10;
	d[29].n_surprise=10;
	d[29].surprise=10;
	d[30].n_surprise=10;
	d[30].surprise=10;

	int t,j;
	cin>>t;
	for(j=1;j<=t;j++){
		int n,s,p,temp,count=0;
		cin>>n>>s>>p;
		int i=n;
		while(n--){
			cin>>temp;
			if(d[temp].n_surprise>=p){
				count++;
				continue;
			}
			else if(s>0)
				if(d[temp].surprise==p){
					count++;
					s--;
					continue;
				}
		}
		cout<<"Case #"<<j<<": "<<count<<endl;
	}
	return 0;
}
				
		
