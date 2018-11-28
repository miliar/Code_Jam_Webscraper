#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		int N;
		cin>>N;
		vector<int> OP,OO,BP,BO;
		for(int i=0;i<N;i++){
			string str;
			int P;
			cin>>str>>P;
			if(str=="O"){
				OP.push_back(P);
				OO.push_back(i);
			}else{
				BP.push_back(P);
				BO.push_back(i);
			}
		}
		
		int sec,Opoint=1,Bpoint=1,Oindex=0,Bindex=0;
		int On=OP.size(),Bn=BP.size();
		for(sec=1;;sec++){
			bool Of=true,Bf=true;
			int OJ=(Oindex==On)?1000:OO[Oindex];
			int BJ=(Bindex==Bn)?1000:BO[Bindex];
			
			if(Oindex!=On&&Opoint==OP[Oindex]&&OJ<BJ){
				Of=false;
			}else if(Bindex!=Bn&&Bpoint==BP[Bindex]&&OJ>BJ){
				Bf=false;
			}
			
			if(Of){
				if(Oindex!=On){
					if(Opoint>OP[Oindex])Opoint--;
					else if(Opoint<OP[Oindex])Opoint++;
				}
			}else{
				Oindex++;
			}
			
			if(Bf){
				if(Bindex!=Bn){
					if(Bpoint>BP[Bindex])Bpoint--;
					else if(Bpoint<BP[Bindex])Bpoint++;
				}
			}else{
				Bindex++;
			}
			if(Oindex==On&&Bindex==Bn)
				break;
		}
		
		cout<<"Case #"<<tc<<": "<<sec<<endl;
	}
	return 0;
}
