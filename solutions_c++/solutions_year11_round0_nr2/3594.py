#include<iostream>
#include<map>
using namespace std;
int main(){
	int t;
	int cnt=0;
	cin>>t;
	map<char,int> justmap;
	justmap['Q']=0;
	justmap['W']=1;
	justmap['E']=2;
	justmap['R']=3;
	justmap['A']=4;
	justmap['S']=5;
	justmap['D']=6;
	justmap['F']=7;
	
	bool oppolist[8][8]={false};
	char combinelist[8][8]={'#'};
	//cout<<oppolist[2][5]<<endl;
	//cout<<combinelist[2][5]<<endl;
	while(t--){
		int i,j;
		for(i=0;i<8;i++){
			for(j=0;j<8;j++){
				oppolist[i][j]=false;
				combinelist[i][j]='#';
			}
		}
		int c,d,n,k1,k2;

		char temp[6];
		char input[110];
		char output[110];

		cin>>c;
		for(i=0;i<c;i++){
			cin>>temp;
			k1=justmap[temp[0]];
			k2=justmap[temp[1]];
			combinelist[k1][k2]=temp[2];
			combinelist[k2][k1]=temp[2];
		}

		cin>>d;
		for(i=0;i<d;i++){
			cin>>temp;
			k1=justmap[temp[0]];
			k2=justmap[temp[1]];
			oppolist[k1][k2]=oppolist[k2][k1]=true;
		}

		cin>>n;
		cin>>input;
		int oit=0;
//		output[0]=input[0];
//		k2=justmap[output[0]];
		bool combined;
		for(i=0;i<n;i++){
			output[oit]=input[i];
			if(oit==0){
				//cout<<output[oit]<<endl;
				oit++;
				continue;
			}

			combined=false;
			if(justmap.count(output[oit-1])!=0){
				k1=justmap[output[oit-1]];
				k2=justmap[output[oit]];
				if(combinelist[k1][k2]!='#'){
					oit--;
					output[oit]=combinelist[k1][k2];
					combined=true;
				}
			}
			if(!combined){
				k2=justmap[output[oit]];
				for(j=0;j<oit;j++){
					if(justmap.count(output[j])==0)continue;
					k1=justmap[output[j]];
					if(oppolist[k1][k2]){
						oit=-1;
						break;
					}
				}
			}
//			output[oit+1]='\0';
//			cout<<output<<endl;
			oit++;
				
		}
		output[oit]='\0';
		cnt++;
		cout<<"Case #"<<cnt<<": "<<"[";
		for(i=0;i<oit-1;i++){
			cout<<output[i]<<", ";
		}
		if(oit-1>=0)cout<<output[oit-1]<<"]"<<endl;
		else cout<<"]"<<endl;
//		cout<<output<<endl;
	}
	
	return 0;
}
