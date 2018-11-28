#include<iostream>
using namespace std;
int main(){
	int t,n,nx[2],tx,px[2],ox[2],r,tr;
	int bc[101],bcx[2][101];
	bool bcw[101];
	char c[2];
	cin>>t;
	for(int i=1;i<=t;++i){
		cin>>n;
		r=ox[0]=ox[1]=nx[0]=nx[1]=0;
		px[0]=px[1]=1;
		for(int x=0;x<n;++x){
			//scanf("%d %c",&bc[x],&c);
			cin>>c>>bc[x];
			bcw[x]= (c[0]=='O'?0:1);
			bcx[bcw[x]][nx[bcw[x]]] = bc[x];
			++nx[bcw[x]];
		}
		/*
		for(int x=0;x<n;++x)
			cout<<bc[x]<<' ';
		cout<<endl;
		for(int x=0;x<nx[0];++x)
			cout<<bcx[0][x]<<' ';
		cout<<endl;
		for(int x=0;x<nx[1];++x)
			cout<<bcx[1][x]<<' ';
		cout<<endl;
		*/
		for(int x=0;x<n;++x){
			tx = bcw[x];
			tr=0;
			//cout<<bcx[tx][ox[tx]]<<","<<tx<<" px:"<<px[0]<<','<<px[1]<<endl;
			if(px[tx]!=bcx[tx][ox[tx]]){
				//cout<<"!"<<px[tx]<<":"<<bcx[tx][ox[tx]]<<endl;
				tr = abs(px[tx]-bcx[tx][ox[tx]]);
				px[tx] = bcx[tx][ox[tx]];
			}
			if(px[!tx]!=bcx[!tx][ox[!tx]]){
				if(abs(px[!tx] - bcx[!tx][ox[!tx]])<=1+tr )
					px[!tx]=bcx[!tx][ox[!tx]];
				else{
					px[!tx] += (px[!tx] < bcx[!tx][ox[!tx]]?1:-1)*(1+tr);
				}
			}
			r+=(tr+1);
			//cout<<bcx[tx][ox[tx]]<<","<<tx<<" px:"<<px[0]<<','<<px[1]<<endl;
			++ox[tx];
			//cout<<tr<<':'<<r<<endl;
		}
		printf("Case #%d: %d\n",i,r);
	}

}
