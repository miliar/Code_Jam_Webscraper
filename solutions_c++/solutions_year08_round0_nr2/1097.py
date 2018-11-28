
#include<iostream>
#include<fstream>
#include<string>
#include<set>
using namespace std;


ifstream filein("B-large.in");
ofstream fileout("cj2.out");

struct tm1{
	int de_tm;
	int arr_tm;
};




int min(tm1 c[],bool var,char setc[],int num){
	int pc,pmin = 0;
	bool chg = false;
	if(!var){
		for(pc=0;pc<num;pc++){
			if(setc[pc]!=1){
				if(!chg)pmin=pc;
				else if(c[pc].de_tm<=c[pmin].de_tm)pmin = pc;
				chg = true;
			}
		}
	}
	if(chg)return pmin;
	else return 1600;
}

int main(){
	int n;
	int i,j,k,u,v,w,s,t,u1,v1;
	string str;
	filein>>n;
	for(i = 0;i<n;i++){	
		char seta[100],setb[100];
		tm1 a[100],b[100];
		filein>>t>>u>>v;
		u1 = u;
		v1 = v;
		w = 1;
		for(j = 0;j<2*u;j++){
			filein>>str;
			if(w==1){
				a[j/2].de_tm = ((str[0]-'0')*10+(str[1]-'0'))*60+(str[3]-'0')*10+(str[4]-'0');
				w--;
			}
			else{
				a[j/2].arr_tm = ((str[0]-'0')*10+(str[1]-'0'))*60+(str[3]-'0')*10+(str[4]-'0');
				w++;
			}
			
		}
		w = 1;
		for(j = 0;j<2*v;j++){
			filein>>str;
			if(w==1){
				b[j/2].de_tm = ((str[0]-'0')*10+(str[1]-'0'))*60+(str[3]-'0')*10+(str[4]-'0');
				w--;
			}
			else{
				b[j/2].arr_tm = ((str[0]-'0')*10+(str[1]-'0'))*60+(str[3]-'0')*10+(str[4]-'0');
				w++;
			}			
		}
		for(j = 0;j<100;j++){
			seta[j] = 0;
			setb[j] = 0;
		}
		int next = 0;
		bool has_next = false;
		while(u1 && v1){
			s = min(a,false,seta,u);
			k = min(b,false,setb,v);
			if (s == 1600 && k == 1600)break;
			if(k==1600 ||(k!=1600 && s!=1600 && a[s].de_tm<b[k].de_tm)){
				while(1){
					next = 0;
					has_next = false;
					for(j=0;j<v;j++){
						if(a[s].arr_tm+t<=b[j].de_tm && setb[j]==0 ){
							if(!has_next)next = j;
							else if(b[j].de_tm<b[next].de_tm)next = j;
							else if(b[j].de_tm==b[next].de_tm && b[j].arr_tm<b[next].arr_tm)next = j;
							has_next = true;
						}
					}
					seta[s] = 1;
					if(has_next){
						v1--;
					}
					else break;
					k = next;
					setb[next] = 1;
					next = 0;
					has_next = false;
					for(j=0;j<u;j++){
						if(b[k].arr_tm+t<=a[j].de_tm && seta[j]==0){
							if(!has_next)next = j;
							else if(a[j].de_tm<a[next].de_tm)next = j;
							else if(a[j].de_tm==a[next].de_tm && a[j].arr_tm<a[next].arr_tm)next = j;
							has_next = true;
						}
					}
					if(has_next){
						u1--;
						s = next;
						seta[next] = 1;
					}
					else break;
				}
			}
			else{				
				while(1){
					next = 0;
					has_next = false;
					for(j=0;j<u;j++){
						if(b[k].arr_tm+t<=a[j].de_tm && seta[j]==0){
							if(!has_next)next = j;
							else if(a[j].de_tm<a[next].de_tm)next = j;
							else if(a[j].de_tm==a[next].de_tm && a[j].arr_tm<a[next].arr_tm)next = j;
							has_next = true;
						}
					}
					setb[k] = 1;
					if(has_next){
						u1--;
						seta[next] = 1;
					}
					else break;
					s = next;
					next = 0;
					has_next = false;
					for(j=0;j<v;j++){
						if(a[s].arr_tm+t<=b[j].de_tm && setb[j]==0){
							if(!has_next)next = j;
							else if(b[j].de_tm<b[next].de_tm)next = j;
							else if(b[j].de_tm==b[next].de_tm && b[j].arr_tm<b[next].arr_tm)next = j;
							has_next = true;
						}
					}
					if(has_next){
						v1--;
						k = next;
						setb[next]=1;
					}
					else break;
				}
			}
		}
		fileout<<"Case #"<<i+1<<": "<<u1<<" "<<v1<<endl;
	}
	return 0;
}