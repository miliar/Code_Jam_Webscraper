#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	int t,i,j,k,l,m,n,r,c;
	char A[100][100];
	scanf("%d",&t);
	char C;
	l=1;
	pair<int,int> p;
	while(l<=t){
		printf("Case #%d:\n",l++);
		//vector<pair<int,int> > V;
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++){
			C=getchar();
			for(j=0;j<c;j++){
				C=getchar();
				A[i][j]=C;
			}
		}
		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
		//		p = make_pair(i,j);
				if(A[i][j] == '#'){
					bool e1,e2,e3;
					e1 = i<r&&j+1<c&&A[i][j+1]=='#';
					e2 = i+1<r&&j<c&&A[i+1][j]=='#';
					e3 = i+1<r&&j+1<c&&A[i+1][j+1]=='#';
					if(e1&&e2&&e3){
						A[i][j]='/';
						A[i][j+1]='\\';
						A[i+1][j]='\\';
						A[i+1][j+1]='/';
					}
				}
			}
		}
		bool check=true;
		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				if(A[i][j]=='#') check=false;
			}
		}
		if(!check){
			printf("Impossible\n");
		}else{
			for(i=0;i<r;i++){
				for(j=0;j<c;j++){
					printf("%c",A[i][j]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}

