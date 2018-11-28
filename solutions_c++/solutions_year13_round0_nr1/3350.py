#include<iostream>
using namespace std;
char data[4][4];
int solver(){
	int xh=0,oh=0,xv=0,ov=0;
	for(int i=0;i<4;i++){
		xh=0;
		oh=0;
		xv=0;
		ov=0;
		for(int k=0;k<4;k++){
			if(data[i][k]=='X' || data[i][k]=='T') xh++;
		    if(data[i][k]=='O' || data[i][k]=='T') oh++;
			if(data[k][i]=='X' || data[k][i]=='T') xv++;
		    if(data[k][i]=='O' || data[k][i]=='T') ov++;
		}
		if(xh==4 || xv==4)
			return 1;
		if(oh==4 || ov==4)
			return 2;
	}
	xh=0;
	oh=0;
	xv=0;
	ov=0;
	for(int k=0;k<4;k++)
	{
			if(data[k][k]=='X' || data[k][k]=='T') xh++;
		    if(data[k][k]=='O' || data[k][k]=='T') oh++;
			if(data[k][4-k-1]=='X' || data[k][4-k-1]=='T') xv++;
		    if(data[k][4-k-1]=='O' || data[k][4-k-1]=='T') ov++;
	}
	if(xh==4 || xv==4)
			return 1;
	if(oh==4 || ov==4)
			return 2;
	else
		return 3;
}
int main(){
	int n;
	bool empty;
	freopen("1.in", "r", stdin), freopen("1.out", "w", stdout);
	scanf("%i",&n);
	for(int i=0;i<n;i++)
	{
		empty=false;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++){
				cin>>data[j][k];
				if(!empty && data[j][k]=='.')
					empty=true;
			}
			int l=solver();
			if(l==1){
				printf("Case #%i: X won\n",i+1);
			}else if(l==2){
				printf("Case #%i: O won\n",i+1);
			}else if(l==3 && empty){
				printf("Case #%i: Game has not completed\n",i+1);
			}else{
				printf("Case #%i: Draw\n",i+1);
			}
	}
	return 0;
}