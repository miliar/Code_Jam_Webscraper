#include <iostream>
#include <cmath>
#include <stdlib.h>
using namespace std;

#define max 1000
#define mn(a,b) ((a)<(b))?a:b

int main()
{
int T, N,p[max],i,j,res=0,bpos=1,opos=1,currt=0,lbt=0,lot=0,t1,t2,t3;
char n[max],line[max];

cin>>T;
//gets(line);
//T=atoi(line);
for(i=1;i<=T;i++){
	cin>>N;
	//gets(line);
	//N=atoi(line);
	for(j=1;j<=N;j++){
		cin>>n[j];
		cin>>p[j];
	}

	bpos=1;opos=1;currt=0;lbt=0;lot=0;	 
	for(j=1;j<=N;j++){
		if(n[j]=='B'){
			t1=abs(bpos-p[j]);
			t2=currt-lbt;
			if(t1<=t2)
				currt++;
			else{
				currt += (t1-t2+1);	   
			}
				//currt += (t2+(t1-t2));//gt(t1,t2);
			//currt++;
			lbt=currt;
			bpos=p[j];
		}else{
			t1=abs(opos-p[j]);
			t2=currt-lot;
			if(t1<=t2)
				currt++;
			else{
				currt += (t1-t2+1);	   
			}
			//currt++;
			//currt++;
			lot=currt;
			opos=p[j];
		}
		//cout<<"curt "<<currt<<" lbt "<<lbt<<" lot "<<lot<<"  opos "<<opos<<" bpos "<<bpos<<endl;
	}
	cout<<"Case #"<<i<<": "<<currt<<endl;;
}


return 0;
}

