#include<iostream>
using namespace std;

int xt[51][51],n,blue,red,row[51][51],col[51][51],xl[51][51],yl[51][51],k;
char t[51][51],r[51][51];

void ro0(){
	int i,j,len;
	for(i=0 ; i<n ; i++){
		len=0;
		for(j=0 ; j<n ; j++){
			if(t[i][j]!='.'){
				r[i][len++]=t[i][j];
			}
		}
		for( ; len<n ; len++)
			r[i][len]='.';
	}
}

void ro1(){
	int i,j,len;
	for(i=0 ; i<n ; i++){
		len=0;
		for(j=n-1 ; j>=0 ; j--){
			if(t[i][j]!='.'){
				r[i][len++]=t[i][j];
			}
		}
		for( ; len<n ; len++)
			r[i][len]='.';
	}
}

void find(){
	int i,j;
			memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));
		memset(yl,0,sizeof(yl));
		memset(xl,0,sizeof(xl));
	for(i=0 ; i<n ; i++){

		if(r[i][0]!='.'){
			row[i][0]=xl[i][0]=true;
		}
		if(r[0][i]!='.'){
			xl[0][i]=yl[0][i]=col[0][i]=true;
		}
		if(r[i][n-1]!='.'){
			yl[i][n-1]=true;
		}
	}
	for(i=0 ; i<n ; i++){
		for(j=1 ; j<n ; j++){
			if(r[i][j]!='.'){
				if(r[i][j]==r[i][j-1]){
					row[i][j]=row[i][j-1]+1;
					if(row[i][j]>=k){
						if(r[i][j]=='B') blue=true;
						if(r[i][j]=='R') red=true;
					}
				}
				else row[i][j]=1;
			}
			if(r[j][i]!='.'){
				if(r[j][i]==r[j-1][i]){
					col[j][i]=col[j-1][i]+1;
					if(col[j][i]>=k){
						if(r[j][i]=='B') blue=true;
						if(r[j][i]=='R') red=true;
					}
				}
				else col[j][i]=1;
			}
			if(i!=0){
				if(r[i][j]!='.'){
					if(r[i-1][j-1]==r[i][j]){
						xl[i][j]=xl[i-1][j-1]+1;
						if(xl[i][j]>=k){
							if(r[i][j]=='B') blue=true;
							if(r[i][j]=='R') red=true;
						}
					}
					else xl[i][j]=1;
				}
			}
		}
		if(i!=0){
			for(j=n-2 ; j>=0 ; j--){
				if(r[i][j]!='.'){
					if(r[i-1][j+1]==r[i][j]){
						yl[i][j]=yl[i-1][j+1]+1;
						if(yl[i][j]>=k){
							if(r[i][j]=='B') blue=true;
							if(r[i][j]=='R') red=true;
						}
					}
					else yl[i][j]=1;
				}
			}
		}
	}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("xpa.out","w",stdout);
	int i,j,c,cc;
	scanf("%d",&c);
	for(cc=1 ; cc<=c ; cc++){
		blue=red=0;
		scanf("%d%d",&n,&k);
		for(i=0 ; i<n ; i++){
			scanf("%s",&t[i]);
		}
//		ro0();
//		find();
		ro1();
		find();
		cout << "Case #" << cc << ": ";
		if(red+blue==0){
			cout << "Neither" << endl;
		}
		else if(red+blue==2){
			cout << "Both" << endl;
		}
		else if(red){
			cout << "Red" << endl;
		}
		else if(blue){
			cout << "Blue" << endl;
		}
	}
}
