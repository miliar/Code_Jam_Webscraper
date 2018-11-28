#include<fstream>
#include<cstdio>
using namespace std;

int main(){
	int t,i,j,xc,xr,or,oc,xd,od,xdd,odd;
	char b[5][5];
	int cas;
	ifstream in("A-large.in");
	ofstream out("outputl.out");

	in>>t;
	for(cas=1;cas<=t;cas++){
		for(i=0;i<4;i++)
			in>>b[i];
		//check coulamn
		for(i=xd=xdd=od=odd=0;i<4;i++){
			xc=xr=or=oc=0;
			for(j=0;j<4;j++){
				if(b[i][j]=='X' ||b[i][j]=='T')
					xc++;
				if(b[i][j]=='O' ||b[i][j]=='T')
					oc++;
				if(b[j][i]=='X' ||b[j][i]=='T')
					xr++;
				if(b[j][i]=='O' ||b[j][i]=='T')
					or++;
			}
			if(xc==4 || oc==4 || xr==4 || or==4)
				break;
			if(b[i][i]=='X' ||b[i][i]=='T')
					xd++;
			if(b[i][i]=='O' ||b[i][i]=='T')
					od++;
			if(b[3-i][i]=='X' ||b[3-i][i]=='T')
					xdd++;
			if(b[3-i][i]=='O' ||b[3-i][i]=='T')
					odd++;
		}
		out<<"Case #"<<cas<<": ";
		if(xc==4 || xd==4 || xr==4 || xdd==4)
				out<<"X won"<<endl;
		else if(oc==4 || od==4 || or==4 || odd==4)
				out<<"O won"<<endl;
		else{
			bool t=true;
			for(i=0;i<4 && t;i++){
				for(j=0;j<4;j++){
					if(b[i][j]=='.'){						
						out<<"Game has not completed"<<endl;
						t=false;
						break;
					}
				}
			}
			if(t)
				out<<"Draw"<<endl;
		}
	}
	return 0;
}
	
