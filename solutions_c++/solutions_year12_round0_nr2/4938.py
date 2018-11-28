#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int T,N,S,p;//t casos de prueba, n cantidad de personas, s tripletes sorprendentes, p mejor puntaje
	cin>>T;
	int v[30]={1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,10,10};
	for(int i = 0; i<T; i++){
		int cont = 0,nota;
		cin>>N>>S>>p;
		vector<int> vec;
		for(int o = 0; o<N; o++){
			cin>>nota;
			vec.push_back(nota);
		}
		sort(vec.begin(),vec.end());
		for(int j = 0; j<N; j++){
			if(vec[j]==30) {cont++;continue;}
			if(vec[j]==29) {cont++;continue;}
			if(vec[j]==1 && p<=1) {cont++;continue;}
			if(vec[j]==0 && p==0) {cont++;continue;}
			if((vec[j]%3==1) && ((v[vec[j]-1])>=p)) {cont++;continue;}
			if((vec[j]%3==2) && ((v[vec[j]-1])>=p) && S ){cont++; S--;continue;}
			if((vec[j]%3==0) && ((v[vec[j]-1])>=p) && S) {cont++; S--;continue;}
			if((vec[j]%3==2) && ((v[vec[j]-1]-1)>=p)) {cont++;continue;}
			if((vec[j]%3==0) && ((v[vec[j]-1]-1)>=p)) {cont++;continue;}
			
		}
		cout<<"Case #"<<i+1<<": "<<cont<<endl;
	}
	return 0;
}
