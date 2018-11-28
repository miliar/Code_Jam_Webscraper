#include<iostream>
#include<string>
#include<vector>

using namespace std;

struct st{
	int num;
	int time;
};

int main(){
	int tn;cin>>tn;
	for(int i=0;i<tn;i++){
		cout<<"Case #"<<(i+1)<<": ";
		int ans=0;
		int n;cin>>n;
		vector<st> o;
		vector<st> b;
		for(int i=0;i<n;i++){
			char c;int tmp;
			cin>>c>>tmp;
			if(c=='O'){
				st a;a.num=tmp;
				a.time=i;
				o.push_back(a);
			}else{
				st a;a.num=tmp;
				a.time=i;
				b.push_back(a);
			}
		}
		int time=0;
		int nnum=0;
		int onum=0;
		int bnum=0;
		int op=1;
		int bp=1;
		while(nnum!=n){
			int f=0;
			if(onum!=o.size()){
				if((nnum==o[onum].time) && (op==o[onum].num)){
					onum++;f=1;
				}else{
					if(op<o[onum].num)op++;
					if(op>o[onum].num)op--;
				}
			}
			if(bnum!=b.size()){
				if((nnum==b[bnum].time) && (bp==b[bnum].num)){
					bnum++;f=1;
				}else{
					if(bp<b[bnum].num)bp++;
					if(bp>b[bnum].num)bp--;
				}
			}
			if(f)nnum++;
			time++;
		}
		cout<<time<<endl;
	}
}
