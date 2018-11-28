#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main(){
	int h;
	cin>>h;
	for(int cc=0;cc<h;++cc){
		int n;
		scanf("%d",&n);//cin>>n;
		int c;
		//cin>>c;
		scanf("%d",&c);
		int ts[n][2];
		vector<int>cus[c];
		for(int i=0;i<c;++i){
			int count;
			//cin>>count;
			scanf("%d",&count);
			for(int t=0;t<count;++t){
				int temp,temp1;
				//cin>>temp>>temp1;
				scanf("%d %d",&temp,&temp1);
				cus[i].push_back(temp);
				cus[i].push_back(temp1);
			}
		}
		string per="";
		for(int i=0;i<n;++i)
			per=per+"0";
		for(int i=0;i<n;++i)
			per=per+"1";
		int flag1=0;
		do{
			int flag2=0;
			for(int i=0;i<c;++i){
				int flag=0;
				for(int j=0;j<cus[i].size();j=j+2){
					if(per[cus[i][j]-1]==(char)(cus[i][j+1]+'0')){
						flag=1;
						break;
					}
				}
				if(flag==0){
					flag2=1;
					break;
				}
			}
			if(flag2==0){
				flag1=1;
				break;
			}
		}while(next_permutation(per.begin(),per.end()));
		//cout<<"Case #"<<cc+1<<": ";
		printf("Case #%d: ",cc+1);
		if(flag1==1){
			//cout<<per[0];
			printf("%c",per[0]);
			for(int i=1;i<n;++i){
				//cout<<" "<<per[i];
				printf(" %c",per[i]);
			}
			//cout<<endl;
		}
		else
			printf("IMPOSSIBLE");
			//cout<<"IMPOSSIBLE"<<endl;
		printf("\n");
	}
	return 0;
}