#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

char base[]={'Q','W','E','R','A','S','D','F'};

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		char ans[102];
		int lans=0;
		char res[256][256];
		memset(res,0,sizeof(res));
		char op[256][256];
		memset(op,0,sizeof(op));
		int tus[256];
		memset(tus,0,sizeof(tus));
		int c;
		cin>>c;
		for(int j=0;j<c;j++){
			string cb;
			cin>>cb;
			res[cb[0]][cb[1]]=cb[2];
			res[cb[1]][cb[0]]=cb[2];
		}

		int d;
		cin>>d;
		for(;d>0;d--){
			string ds;
			cin>>ds;
			op[ds[0]][ds[1]]=1;
			op[ds[1]][ds[0]]=1;
		}
		int n;
		string inv;
		cin>>n>>inv;
		for(int j=0;j<n;j++){
			char cc=inv[j];
			ans[lans]=cc;
			lans++;
			tus[cc]++;
			//printf("j:%d cc:%c ",j,cc);
			if(lans>1){
				char rs=res[ans[lans-2]][ans[lans-1]];
				//printf("rs:%c ",rs);
				if(rs){
					tus[ans[lans-2]]--;
					tus[ans[lans-1]]--;
					ans[lans-2]=rs;
					lans--;
					//printf("comb\n");
				}else{
					for(int k=0;k<8;k++){
						if(op[cc][base[k]] && tus[base[k]]){
							lans=0;
							memset(tus,0,sizeof(tus));
							//printf("rem\n");
							break;
						}
					}
					
				}
				
			}
			/*cout<<"\t [";
				for(int j=0;j<lans;j++){
					cout<<ans[j];
					if(j!=lans-1)
						cout<<", ";
				}
				cout<<"]"<<endl;*/
		}
		
		cout<<"Case #"<<i<<": [";
		for(int j=0;j<lans;j++){
			cout<<ans[j];
			if(j!=lans-1)
				cout<<", ";
		}
		cout<<"]"<<endl;	
	}
	return 0;
}
