#include<iostream>
using namespace std;
int main(){

	int t,i,j;
	char a[4][4];
	cin>>t;
	for(int counter=1;counter<=t;counter++){
			bool c=false;
			for(i=0;i<4;i++)
				scanf("%s",a[i]);
			for(i=0;i<4;i++){
				for(j=0;j<4;j++)
					if(a[i][j]=='.'){
						c=true;
						break;
					}
			}
			int x=0,o=0,countx,counto,wo=0,wx=0;
			
			for(i=0;i<=3;i++){
				countx=0;counto=0;
				for(j=0;j<4;j++){
					if(a[i][j]=='X') countx++;
					if(a[i][j]=='O') counto++;
					if(a[i][j]=='T'){countx++;counto++;}
				}
				if(countx==4) wx++;
				if(counto==4) wo++;
			}
			for(i=0;i<=3;i++){
				countx=0;counto=0;
				for(j=0;j<4;j++){
					if(a[j][i]=='X') countx++;
					if(a[j][i]=='O') counto++;
					if(a[j][i]=='T'){countx++;counto++;}
				}
				if(countx==4) wx++;
				if(counto==4) wo++;
			}

			countx=0;counto=0;
			for(i=0;i<4;i++){
				if(a[i][i]=='X') countx++;
				if(a[i][i]=='O') counto++;
				if(a[i][i]=='T'){countx++;counto++;}
			}
			if(countx==4) wx++;
			if(counto==4) wo++;

			countx=0;counto=0;
			for(i=0;i<4;i++){
				if(a[i][3-i]=='X') countx++;
				if(a[i][3-i]=='O') counto++;
				if(a[i][3-i]=='T'){countx++;counto++;}
			}
			if(countx==4) wx++;
			if(counto==4) wo++;

			if(wx>0) {cout<<"Case #"<<counter<<": X won"<<endl; continue;}
			if(wo>0) {cout<<"Case #"<<counter<<": O won"<<endl; continue;}
			if(c==false) {cout<<"Case #"<<counter<<": Draw"<<endl; continue;}
			cout<<"Case #"<<counter<<": Game has not completed"<<endl;
			getchar();

	}
	return 0;
}