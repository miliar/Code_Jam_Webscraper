#include <iostream>
#include <string>
using namespace std;

int T;
int N,K;
char chess_old[55][55];
char chess_new[55][55];

int main(void){
	freopen("large.in","r",stdin);
    freopen("large.out","w",stdout);
	cin>>T;
	int t=1;
	while(T--){
		memset(chess_old,0,sizeof(chess_old));
		memset(chess_new,0,sizeof(chess_new));
		cin>>N>>K;
		int i,j,k;
		for(i=1;i<=N;i++){
			for(j=1;j<=N;j++){
				cin>>chess_old[i][j];
				chess_new[j][N-i+1]=chess_old[i][j];
			}
		}
		for(j=1;j<=N;j++){
			for(i=N;i>=1;i--){
				k=i;
				while(chess_new[k][j]=='.'&&k>=1){
					k--;
				}
				if(k==i) continue;
				if(k==0) break;
				chess_new[i][j]=chess_new[k][j];
				chess_new[k][j]='.';
			}
		}
		string str_red="",str_blue="";
		string str="";
		bool flag_red=false;
		bool flag_blue=false;
		for(i=1;i<=K;i++){
			str_red+="R";
			str_blue+="B";
		}
		for(i=1;i<=N;i++){
			for(j=1;j<=N;j++){
				str+=chess_new[i][j];
			}
			//cout<<str<<endl;
			if((flag_red==0)&&(str.find(str_red)<=(N-K+1))) flag_red=true;
			if((flag_blue==0)&&(str.find(str_blue)<=(N-K+1))) flag_blue=true;
			str="";

			for(j=1;j<=N;j++){
				str+=chess_new[j][i];
			}
			if((flag_red==0)&&(str.find(str_red)<=(N-K+1))) flag_red=true;
			if((flag_blue==0)&&(str.find(str_blue)<=(N-K+1))) flag_blue=true;
			str="";

		}
		
		

		for(k=0; ;k++){
			i=1;j=K+k;
			if(j>N) break;
			str="";
			while(i<=N){
				str+=chess_new[i++][j--];
			}
			//cout<<str<<endl;
			if((flag_red==0)&&(str.find(str_red)<=(N-K+1))) flag_red=true;
			if((flag_blue==0)&&(str.find(str_blue)<=(N-K+1))) flag_blue=true;

		}

		for(k=0; ;k++){
			i=N;j=2+k;
			if(j+K-1>N) break;
			str="";
			while(j<=N){
				str+=chess_new[i--][j++];
			}
			//cout<<str<<endl;
			if((flag_red==0)&&(str.find(str_red)<=(N-K+1))) flag_red=true;
			if((flag_blue==0)&&(str.find(str_blue)<=(N-K+1))) flag_blue=true;
		}


		for(k=0; ;k++){
			i=1;j=2+k;
			if(j+K-1>N) break;
			str="";
			while(j<=N){
				str+=chess_new[i++][j++];
			}
			//cout<<str<<endl;
			if((flag_red==0)&&(str.find(str_red)<=(N-K+1))) flag_red=true;
			if((flag_blue==0)&&(str.find(str_blue)<=(N-K+1))) flag_blue=true;

		}
		
		for(k=1;k<=N;k++){
			i=k;j=1;
			if(N-i+1<K) break;
			str="";
			while(i<=N){
				str+=chess_new[i++][j++];
			}
			//cout<<str<<endl;
			if((flag_red==0)&&(str.find(str_red)<=(N-K+1))) flag_red=true;
			if((flag_blue==0)&&(str.find(str_blue)<=(N-K+1))) flag_blue=true;
		}
		cout<<"Case #"<<t++<<": ";
		if(flag_red==1&&flag_blue==1){
			cout<<"Both"<<endl;
		}
		else if(flag_red==1){
			cout<<"Red"<<endl;
		}else if(flag_blue==1){
			cout<<"Blue"<<endl;
		}else{
			cout<<"Neither"<<endl;
		}

	}
	return 0;
}
