#include<iostream>
#include<algorithm>
using namespace std;

class wire{
	public:
		int left;
		int right;
};

bool compare(wire a,wire b){
	return a.left<=b.left;
}

wire *save;

int main(){
	int t,m,counter,sum,b,c;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>m;
		save=new wire[m];
		for(b=0;b<m;++b)
			cin>>save[b].left>>save[b].right;
		sort(save,save+m,compare);
		for(b=0,sum=0;b<m;++b){
			for(c=b+1;c<m;++c){
				if(save[c].right<save[b].right)
					++sum;
			}
		}
		cout<<"Case #"<<counter<<": "<<sum<<endl;	
	}
	return 0;
}
