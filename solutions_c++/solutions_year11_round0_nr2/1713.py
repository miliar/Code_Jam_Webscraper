#include<iostream> 
using namespace std;
class key_count{
private:
	int count[8];
	int get_x(char c){
		switch(c){
			case 'A':
				return 0;
			case 'S':
				return 1;
			case 'D':
				return 2;
			case 'F':
				return 3;
			case 'Q':
				return 4;
			case 'W':
				return 5;
			case 'E':
				return 6;
			case 'R':
				return 7;
		}
	}
public:
	key_count(){
		clear_count();
	}
	int get_count(char c){
		return count[get_x(c)];
	}
	void add_count(char c,int t){
		count[get_x(c)]+=t;
	}
	void clear_count(){
		for(int x=0;x<8;++x)	count[x]=0;
	}
};
void print(char *out,int on,int i){
		printf("Case #%d: [",i);
		for(int x=0;x<on;++x){
			if(x==0)	cout<<out[x];
			else		printf(", %c",out[x]);
		}
		printf("]\n");

}
int main(){
	int c,d,n,t,sn;
	char combine[36][4];
	char inverse[28][3];
	char in[101],out[101];
	key_count kc;
	cin>>t;
	for(int i=1;i<=t;++i){
		kc.clear_count();
		cin>>c;
		for(int x=0;x<c;++x)
			cin>>combine[x];
		cin>>d;
		for(int x=0;x<d;++x)
			cin>>inverse[x];
		cin>>sn>>in;
		int on=0;
		for(int x=0;x<strlen(in);++x){
			//cout<<in[x]<<' ';
			out[on++]=in[x];
			kc.add_count(in[x],1);
			if(on>1){
				for(int y=0;y<c;++y){
					if(   (out[on-2]==combine[y][0]&&out[on-1]==combine[y][1])
						||(out[on-2]==combine[y][1]&&out[on-1]==combine[y][0]) ){
							kc.add_count(out[on-1],-1);
							kc.add_count(out[on-2],-1);
							out[on-2]=combine[y][2];
							--on;
					}
				}
				for(int y=0;y<d;++y){
					char c;
					if(inverse[y][0]==out[on-1]){
						c=inverse[y][1];
					}
					else if(inverse[y][1]==out[on-1]){
						c=inverse[y][0];
					}
					else	continue;
					if(kc.get_count(c)>0){
						on=0;
						kc.clear_count();
					}
				}
			}
			//print(out,on,i);
		}
		print(out,on,i);
	}
}
