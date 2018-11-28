#include "cstdio"
#include "iostream"
#include "vector"

#define mp make_pair
using namespace std;

int move(int &pos1,int &pos2, int target1, int target2){
	
	int dist,dist2;
	dist =target1 - pos1;
	pos1=target1;
	if(dist < 0) dist*=-1;
	dist++;
	if(target2!=0){
		dist2=target2 - pos2;
		if(dist2<0) dist2*=-1;
		if(dist2>dist){
			if(target2>pos2) pos2+=dist;
			else pos2-=dist;
		}
		else pos2=target2;
	}
	return dist;
}

int main(){

int t,n,x,steps;
int posO,posB;
char c;
FILE *myFile=fopen("out","w");
FILE *myFile2=fopen("A-large.in","r");
vector<int> orange, blue, all;
vector<int> :: iterator iterO, iterB, iterA;

fscanf(myFile2,"%d",&t);
for(int j=1;j<=t;j++){
	blue.clear();
	orange.clear();
	all.clear();
	fscanf(myFile2,"%d",&n);
	posO=1;
	posB=1;
	
	for(int i=0; i<n; i++){
		fscanf(myFile2," %c%d",&c,&x);
		if(c=='O'){ 
			orange.push_back(x);
			all.push_back(0);
		}
		else{ 
			blue.push_back(x);
			all.push_back(1);
		}
	}
	orange.push_back(0);
	blue.push_back(0);

	iterO = orange.begin();
	iterB = blue.begin();
	iterA = all.begin();
	steps=0;

	while(iterA != all.end()){
		if(*iterA == 0){				
			steps+=move(posO, posB, *iterO, *iterB);
			iterO++;
		}
		else{
			steps+=move(posB, posO, *iterB, *iterO);
			iterB++;
		}
		iterA++;
	}
	fprintf(myFile,"Case #%d: %d\n",j,steps);

}
return 0;
}