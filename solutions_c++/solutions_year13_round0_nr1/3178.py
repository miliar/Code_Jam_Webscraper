#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int t;       
int main(){
 	freopen("a_input","rt",stdin);
 	freopen("a_output","wt",stdout);
 	cin>>t;
 	for(int x=1;x<=t;x++) {
		char a[5][5];
		string y="Game has not completed";
 	 	bool draw=1;
 	 	for(int i=0;i<4;i++) scanf(" %s ",a[i]);
 	 	for(int i=0;i<4;i++) {
 	 		int v=0;
 	 		int h=0;
 	 		int d1=0, d2=0;	
 	 		for(int j=0;j<4;j++) {
 	 			if(a[i][j]=='.') draw=0;
 	 			if(a[i][j]=='T') h+=11;
 	 			if(a[i][j]=='X') h++;
 	 			if(a[i][j]=='O') h+=10;	
 	 			if(a[j][i]=='T') v+=11;
 	 			if(a[j][i]=='X') v++;
 	 			if(a[j][i]=='O') v+=10;
 	 			if(a[j][j]=='T') d1+=11;
 	 			if(a[j][j]=='X') d1++;
 	 			if(a[j][j]=='O') d1+=10;
 	 			if(a[3-j][j]=='T') d2+=11;
 	 			if(a[3-j][j]=='X') d2++;
 	 			if(a[3-j][j]=='O') d2+=10;
 	 		}
 	 		//cout<<h<<" "<<v<<" "<<d1<<" "<<d2<<endl;
 			if(h/10==4) y="O won";
 			if(h%10==4) y="X won";
 			if(v/10==4) y="O won";
 			if(v%10==4) y="X won";
 			if(d1/10==4) y="O won";
 			if(d1%10==4) y="X won";
 			if(d2/10==4) y="O won";
 			if(d2%10==4) y="X won";
 	 	}
 		if((y[0]=='G')&&(draw)) y="Draw";
 		printf("Case #%d: ",x);
 		cout<<y<<endl;
 	}
 	return 0;
}