#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main(){
	int tn;cin>>tn;
	for(int iii=0;iii<tn;iii++){
		cout<<"Case #"<<(iii+1)<<": ";
		vector<string> com;
		vector<string> opp;
		int cnum;cin>>cnum;
		for(int i=0;i<cnum;i++){
			string s;cin>>s;com.push_back(s);
		}
		int onum;cin>>onum;
		for(int i=0;i<onum;i++){
			string s;cin>>s;opp.push_back(s);
		}
		int n;cin>>n;string orig;cin>>orig;
		char mem[1000];
		int num=0;
		for(int i=0;i<n;i++){
			mem[num]=orig[i];
			num++;
			int f=0;
			if(num>=2){
				for(int j=0;j<cnum;j++){
					if((mem[num-1]==com[j][0]) && (mem[num-2]==com[j][1])){
						mem[num-2]=com[j][2];
						num--;
						f=1;
						break;
					}else if((mem[num-2]==com[j][0]) && (mem[num-1]==com[j][1])){
						mem[num-2]=com[j][2];
						num--;
						f=1;
						break;
					}
				}
			}
			if(f==0){
				for(int j=0;j<onum;j++){
					for(int k=0;k<num;k++){
						for(int l=0;l<k;l++){
							if((mem[k]==opp[j][0]) && (mem[l]==opp[j][1])){num=0;}
							else if((mem[k]==opp[j][1]) && (mem[l]==opp[j][0])){num=0;}
							if(num==0)break;
						}
					}
				}
			}
			//cout<<"[";
			//for(int i=0;i<num;i++){
			//	if(i!=0)cout<<", ";
			//	cout<<mem[i];
			//}
			//cout<<"]"<<endl;
		}
		cout<<"[";
		for(int i=0;i<num;i++){
			if(i!=0)cout<<", ";
			cout<<mem[i];
		}
		cout<<"]"<<endl;
	}
}
