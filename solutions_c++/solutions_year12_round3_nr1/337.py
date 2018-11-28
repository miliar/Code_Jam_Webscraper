#include<iostream>
#include<algorithm>
using namespace std;

int k;

class node{
	public:
		int count;
		int *next;
		node(){
			count=0;
			next=NULL;
		}
};

bool *visit;
node *save;

bool find(int n){
	int b;
	if(visit[n])
		return true;
	else{
		visit[n]=true;
		for(b=0;b<save[n].count;++b){
			if(find(save[n].next[b]))
				return true;
		}
		return false;
	}
}

int main(){
	int t,counter,b,c;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>k;
		visit=new bool[k+1];
		save=new node[k+1];
		for(b=1;b<=k;++b){
			cin>>save[b].count;
			save[b].next=new int[save[b].count];
			for(c=0;c<save[b].count;++c)
				cin>>save[b].next[c];
		}
		for(b=1;b<=k;++b){
			fill(visit,visit+k+1,false);
			if(find(b)){
				cout<<"Case #"<<counter<<": Yes"<<endl;
				break;
			}
		}
		if(b==k+1)
			cout<<"Case #"<<counter<<": No"<<endl;
	}
	return 0;
}
