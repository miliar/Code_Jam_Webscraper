#include<iostream>
using namespace std;

class group{
	public:
		int people;
		int next;
		int money;
		group(){
			people=0;
			next=0;
			money=0;
		}
};

group *save;

int main(){
	int t,r,k,m,counter,b,c;
	long long int sum;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>r>>k>>m;
		save=new group[m];
		for(b=0;b<m;++b){
			cin>>save[b].people;
		}
		for(b=0;b<m;++b){
			save[b].money=save[b].people;
			for(c=b+1;c%m!=b;++c){
				if(k-save[b].money>=save[c%m].people)
					save[b].money+=save[c%m].people;
				else
					break;
			}
			save[b].next=c%m;
			//cout<<"group["<<b<<"] : "<<save[b].people<<"-"<<save[b].next<<"-"<<save[b].money<<endl;
		}
		for(sum=0,b=0;r>0;--r){
			sum+=save[b].money;
			b=save[b].next;
		}
		cout<<"Case #"<<counter<<": "<<sum<<endl;
	}
	return 0;
}
