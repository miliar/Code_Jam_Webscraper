#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int main(){
	char dic[5050][100],c;
	bool w[100][100];
	int i,j,r,L,D,N,count,flag,kase=0,k;
	//freopen("1.txt","r",stdin);
	//freopen("a-simple.out","w",stdout);

	cin>>L>>D>>N;

	for(i=0;i<D;i++){
		scanf("%s",dic[i]);
	}
	scanf("%c",&c);
	for(k=0;k<N;k++){
		r=c=0;count=0;kase++;flag=0;
		memset(w,false,sizeof(w));
		while(scanf("%c",&c)==1 && c!='\n'){
			if(c==')'){r++;flag=0;}
			else if(c=='('){flag=1;continue;}
			else {
				if(flag==1){w[r][c-'a']=true;}
				else {
					w[r][c-'a']=true;
					r++;
				}
			}
		}

		for(i=0;i<D;i++){
			flag=1;
			for(j=0;dic[i][j];j++){
				if(w[j][dic[i][j]-'a']==false){
					flag=0;
					break;
				}
			}
			if(flag==1)count++;
		}
		memset(w,false,sizeof(w));
		printf("Case #%d: %d\n",kase,count);
	}
	return 0;
}

