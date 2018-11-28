#include <fstream.h>
#include <stdio.h>
#include <iostream.h>
ifstream in("/Users/SunKim/Desktop/Codejam1/Untitled/p1.in");
ofstream out("/Users/SunKim/Desktop/Codejam1/Untitled/p1.out");
int n,m;
int data[2][105];
int pos[2];
int nextpos[2][2];
int cnt;
int num[2];
int flag;
char acolor;
void findNext(int color){
	int i;
	int temp;
	for(i=0;i<m;i++){
		if(data[color][i]!=0){
			temp=data[color][i];
			nextpos[color][0]=temp;
			data[color][i]=0;
			nextpos[color][1]=i;
			if(nextpos[color][0]<pos[color]){
				num[color]=-1;
			}else{
				num[color]=1;
			}
			return;
		}
	}
	nextpos[color][0]=0;
}
int mini(int b,int o){
	if(b<o) return 0;
	return 1;
}
int main(){
	int i,j;
	in >> n;
	for(int z=0;z<n;z++){
		for(i=0;i<2;i++){
			for(j=0;j<101;j++){
				data[i][j]=0;
			}
		}
		for(i=0;i<2;i++){
			for(j=0;j<2;j++){
				nextpos[i][j]=0;
			}
		}
		in >> m;
		pos[0]=1;
		pos[1]=1;
		cnt=0;
		for(i=0;i<m;i++){
			in >> acolor;
			if(acolor=='B'){
				in >> data[0][i];
			}else if(acolor=='O'){
				in >> data[1][i];
			}
		}
		findNext(0);
		findNext(1);
		for(;;cnt++){
			if(nextpos[0][0]!=pos[0] && nextpos[1][0]!=pos[1]){
				if(nextpos[0][0]!=0) pos[0]+=num[0];
				if(nextpos[1][0]!=0) pos[1]+=num[1];
			}else if(nextpos[0][0]==pos[0] && nextpos[1][0]!=pos[1]){
				if(nextpos[0][1]<nextpos[1][1] || nextpos[1][0]==0){
					findNext(0);
				}
				if(nextpos[1][0]!=0) pos[1]+=num[1];
			}else if(nextpos[0][0]!=pos[0] && nextpos[1][0]==pos[1]){
				if(nextpos[1][1]<nextpos[0][1] || nextpos[0][0]==0){
					findNext(1);
				}
				if(nextpos[0][0]!=0) pos[0]+=num[0];
			}else if(nextpos[0][0]==pos[0] && nextpos[1][0]==pos[1]){
				int t=mini(nextpos[0][1],nextpos[1][1]);
				findNext(t);
			}

			if(nextpos[0][0]==0 && nextpos[1][0]==0) break;
		}
		out << "Case #" << z+1 << ": " << cnt+1 << "\n";
	}
	return 0;
}