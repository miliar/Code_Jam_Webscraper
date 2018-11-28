#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	unsigned int N,P;
	char R;
	cin>>t;
	int ctime,ocp,bcp,opp,bpp,blt,olt;
	for(int i=1;i<=t;i++){
		ocp=bcp=opp=bpp=1;
		cin>>N;
		ctime=blt=olt=0;
		for(int j=0;j<N;j++){
			cin>>R>>P;
			if(R=='O'){
				ocp=P;
				if(olt+abs(opp-ocp)>ctime)
					ctime=olt+abs(opp-ocp);
				olt=++ctime;
				opp=P;
			}else{
				bcp=P;
				if(blt+abs(bpp-bcp)>ctime)
					ctime=blt+abs(bpp-bcp);
				blt=++ctime;
				bpp=P;				
			}
		}
		cout<<"Case #"<<i<<": "<<ctime<<endl;
	}
	return 0;
}