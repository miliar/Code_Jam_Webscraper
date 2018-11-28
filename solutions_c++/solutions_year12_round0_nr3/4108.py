#include<iostream>
#include<algorithm>
#include<ctime>
using namespace std;

int main(){
	long long int t,b,sum,counter,start,end,temp,flag,temp2;
	bool *save;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>start>>end;
		save=new bool[end+1];
		for(b=start>10?start:10,sum=0,flag=100;b<=end;++b){
			fill(save,save+end+1,false);
			while(b>=flag)
				flag*=10;
			for(temp=10;temp<flag;temp*=10){
				temp2=b/temp+(b%temp)*flag/temp;
				if(temp2>b&&temp2<=end&&temp2>=start){
					if(!save[temp2]){
						++sum;
						save[temp2]=true;
					}
					//cout<<b<<"-"<<temp2<<endl;
				}
			}
			//cout<<b<<endl;
		}
		cout<<"Case #"<<counter<<": "<<sum<<endl;
	}
	//cout<<clock()<<endl;
	return 0;
}
