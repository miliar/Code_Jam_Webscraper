#include<iostream>
#include<vector>

using namespace std;

int input_time(){
	int total,hrs,mins;
	char seperator;
	cin>>hrs>>seperator>>mins;
	total=hrs*60+mins;
	return total;
}

int addtimes(int a,int b){
	int total=a+b;
	if(total>=1440)
		total-=1440;
	return total;
}

struct event{
	int t;
	char type;
};

typedef struct event event;

bool operator < (const event e1,const event e2){
	if(e1.t<e2.t)
		return true;
	else if(e1.t>e2.t)
		return false;
	else{
		if(e1.type=='a' && e2.type=='A'){
			return true;
		}
		else if(e1.type=='A' && e2.type=='a'){
			return false;
		}
		else if(e1.type=='b' && e2.type=='B'){
			return true;
		}
		else if(e1.type=='B' && e2.type=='b'){
			return false;
		}
		else{
			return true;
		}
	}
}

//Capital means Leaving the station, Small means arriving at it...

main(){
	int tc,cn;
	cin>>tc;
	for(cn=1;cn<=tc;cn++){
		int i,num_events,tbt,NA,NB,SA=0,SB=0,atA=0,atB=0;
		cin>>tbt;
		cin>>NA>>NB;
		vector<event> e;
		for(i=0;i<NA;i++){
			event temp1,temp2;
			temp1.type='A';
			temp1.t=input_time();
			e.push_back(temp1);
			temp2.type='b';
			temp2.t=addtimes(input_time(),tbt);
			e.push_back(temp2);
		}
		for(i=0;i<NB;i++){
			event temp1,temp2;
			temp1.type='B';
			temp1.t=input_time();
			e.push_back(temp1);
			temp2.type='a';
			temp2.t=addtimes(input_time(),tbt);
			e.push_back(temp2);
		}
		num_events=2*(NA+NB);
		sort(e.begin(),e.end());
		for(i=0;i<num_events;i++){
			if(e[i].type=='A'){
				if(atA>0){
					atA--;
				}
				else if(atA==0){
					SA++;
				}
			}
			else if(e[i].type=='a'){
				atA++;
			}
			else if(e[i].type=='B'){
				if(atB>0){
					atB--;
				}
				else if(atB==0){
					SB++;
				}
			}
			else if(e[i].type=='b'){
				atB++;
			}
		}
		cout<<"Case #"<<cn<<": "<<SA<<" "<<SB<<endl;
	}
}


