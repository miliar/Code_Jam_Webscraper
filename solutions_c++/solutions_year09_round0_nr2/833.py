#include<iostream>
using namespace std;
int avail='a';
int H,W;
int map[100][100];
char mark[100][100];
char FindSink(int x,int y){
	if(mark[x][y]!='0')return mark[x][y];
	int diff=0,nextx,nexty,alt=map[x][y]; 
	char mk;
	//north
	if(x-1>=0 and map[x][y]-map[x-1][y]>diff){
		diff=map[x][y]-map[x-1][y];
		nextx=x-1;nexty=y;
	}
	if(y-1>=0 and map[x][y]-map[x][y-1]>diff){
		diff=map[x][y]-map[x][y-1];
		nextx=x;nexty=y-1;
	}
	if(y+1<W and map[x][y]-map[x][y+1]>diff){
		diff=map[x][y]-map[x][y+1];
		nextx=x;nexty=y+1;
	}
	if(x+1<H and map[x][y]-map[x+1][y]>diff){
		diff=map[x][y]-map[x+1][y];
		nextx=x+1;nexty=y;
	}
	if(diff!=0){
		mk=FindSink(nextx,nexty);
		mark[x][y]=mk;
		return mk;
	}
	mark[x][y]=avail;
	mk=avail;
//	cout<<x<<" "<<y<<" "<<mk<<endl;
	avail++;
	return mk;
}
int main(){
	int T,cas=0;
	cin>>T;
	while(cas++<T){
		int i,j;
		cin>>H>>W;
		avail='a';
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				cin>>map[i][j];
				mark[i][j]='0';
			}
		}
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
					FindSink(i,j);
					//avail++;
				}
			}
		cout<<"Case #"<<cas<<":"<<endl;
		for(i=0;i<H;i++){
			for(j=0;j<W-1;j++)
				cout<<mark[i][j]<<" ";
			cout<<mark[i][W-1]<<endl;
		}

	}
	return 0;
}
