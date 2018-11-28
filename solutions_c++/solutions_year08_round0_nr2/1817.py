#include<string>
#include<fstream>
#include<vector>
#include<stdlib.h>
using namespace std;

struct traffic{
	   int time;
	   bool isget;
};

int compare( const void *arg1, const void *arg2){
	traffic* a=(traffic*)arg1;
	traffic* b=(traffic*)arg2;
	if(a->time==b->time){
 	    if(a->isget){return -1;}
 	    if(b->isget){return 1;}
 	    else return 0;
 	}
	return (a->time-b->time);
}
int string_num(string& n){
	int k=0,j=n.size()-1,num=0;
	while(k<n.size() && j>=0){
		   num=num*10+(n[k]-'0');
 	   	   j--;
 	   	   k++;
  		}
	return num;
}
int time(string & t){
	int hour=(t[0]-'0')*10+(t[1]-'0');
	int second=(t[3]-'0')*10+(t[4]-'0');
	return (hour*60+second);
}


int main(){
	ifstream in("B-small.in");
	ofstream out("B-small.out");
	int n;
	traffic A[41];
	traffic B[41];
	string num;
	getline(in,num);
	n=string_num(num);
	int i=0;
	while(i<n){
 	    getline(in,num);
 	    int trainA=0,remainA=0;
 	    int trainB=0,remainB=0;
 	    int m=string_num(num);
 	    int ata,atb;
 		getline(in,num,' ');
 	    ata=string_num(num);
 	    getline(in,num);
 	    atb=string_num(num);
 	    int j=0;
 	    while(j<ata){
		    getline(in,num,' ');
		    A[j].time=time(num);
		    A[j].isget=false;
		    getline(in,num);
		    B[j].time=time(num)+m;
		    B[j].isget=true;
			j++;
 		}
 		while(j<atb+ata){
		    getline(in,num,' ');
		    B[j].time=time(num);
		    B[j].isget=false;
		    getline(in,num);
		    A[j].time=time(num)+m;
		    A[j].isget=true;
			j++;
        }
 	    qsort(A,ata+atb,sizeof(traffic),compare);
 	    qsort(B,ata+atb,sizeof(traffic),compare);
 	    j=0;
 		while(j<ata+atb){
		   if(A[j].isget){
		     remainA++;
		   }
		   else if(!A[j].isget){
   		     if(remainA==0){
 				trainA++;
		 	 } 
		 	 else remainA--;
	  	   }
		   if(B[j].isget){
			  remainB++;
		   }
		   else if(!B[j].isget){
   		      if(remainB==0){
 				trainB++;
		 	 } 
		 	 else remainB--;
	  	   }
		   j++;
 		}
 		out<<"Case #"<<i+1<<": "<<trainA<<" "<<trainB<<endl;
 		i++;
 	}
	return 0;
}	
