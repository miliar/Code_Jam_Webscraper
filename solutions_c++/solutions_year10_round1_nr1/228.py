#include<iostream>
#include<string>

using namespace std;


int N,K;
char map[60][60];
char mapr[60][60];
int ansr,ansb;

void checkr(int a,int b){
	if(map[a][b]!='R')return;

	int i;
	for(i=1;i<K;i++){
		if(a+i>=N || map[a+i][b]!='R')break;
	}
	if(i==K) ansr = 1;
	for(i=1;i<K;i++){
		if(b+i>=N || map[a][b+i]!='R')break;
	}
	if(i==K) ansr = 1;

	for(i=1;i<K;i++){
		if(a+i>=N || b+i>=N || map[a+i][b+i]!='R')break;
	}
	if(i==K) ansr = 1;

	for(i=1;i<K;i++){
		if(a+i>=N || b-i<0 || map[a+i][b-i]!='R')break;
	}
	if(i==K) ansr = 1;
}

void checkb(int a,int b){
	if(map[a][b]!='B')return;

	int i;
	for(i=1;i<K;i++){
		if(a+i>=N || map[a+i][b]!='B')break;
	}
	if(i==K) ansb = 1;
	for(i=1;i<K;i++){
		if(b+i>=N || map[a][b+i]!='B')break;
	}
	if(i==K) ansb = 1;

	for(i=1;i<K;i++){
		if(a+i>=N || b+i>=N || map[a+i][b+i]!='B')break;
	}
	if(i==K) ansb = 1;

	for(i=1;i<K;i++){
		if(a+i>=N || b-i<0 || map[a+i][b-i]!='B')break;
	}
	if(i==K) ansb = 1;
}

void calc(){
	for(int j=0;j<N;j++){
		for(int i=N-1;i>=0;i--){
			if(map[i][j]!='.'){
				for(int k=N-1;k>i;k--){
					if(map[k][j]=='.'){
						map[k][j] = map[i][j];
						map[i][j] = '.';
						break;
					}
				}
			}
		}		
	}


	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			checkr(i,j);
			checkb(i,j);
		}
	}
}
void rotate(){
	int i,j,p,q;
	for(i=0,p=0;i<N;i++,p++){
		for(j=0,q=N-1;j<N;j++,q--){
			mapr[i][j] = map[q][p];
		}
	}

	//cout<<"rotate"<<endl;

	for(i=0;i<N;i++){
		//printf("%s\n",mapr[i]);
		for(j=0;j<N;j++){
			map[i][j] = mapr[i][j];
		}
	}
	//cout<<endl;
}



int main(){
	int cs,cscnt;

	freopen("out.out","w",stdout);

	cin>>cs;
	for(cscnt=1;cscnt<=cs;cscnt++){
		
		cin>>N>>K;
		for(int i=0;i<N;i++){
			scanf("%s",map[i]);
		}
		ansr = ansb = 0;
		rotate();
		calc();

		printf("Case #%d: ",cscnt);
		if(ansr==1&&ansb==1){
			cout<<"Both";
		}
		if(ansr==1&&ansb==0){
			cout<<"Red";
		}
		if(ansr==0&&ansb==1){
			cout<<"Blue";
		}
		if(ansr==0&&ansb==0){
			cout<<"Neither";
		}



		cout<<endl;
	}

	return 0;
}