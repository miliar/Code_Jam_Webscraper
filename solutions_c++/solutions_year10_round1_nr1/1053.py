#include <iostream>
#include <fstream>
using namespace std;
//#define DEBUG

char status[50][50];
int N,K;
typedef struct _dir{
    int i;
    int j;
    int x;
    int y;
} dir;
dir dirs[4]={
    {0,-1,0,1},//row
    {-1,0,1,0},//colume
    {-1,-1,1,1},//
    {1,-1,-1,1}
};

string solve(){
    int i,j,k;
    int x,y;
    int found, pos;
    bool redok = false;
    bool blueok = false;
    for(i=0;i<N;i++){
	for(j=0;j<N;j++){
#ifdef DEBUG
	    cout<<"Pos"<<i<<","<<j<<endl;
#endif
	    if(status[i][j]=='.')
		continue;
	    if(status[i][j]=='R' && redok)
		continue;
	    if(status[i][j]=='B' && blueok)
		continue;
	    for(k=0;k<4;k++){
#ifdef DEBUG
		cout<<"Dir"<<k<<endl;
#endif
		found=1;
		x=i+dirs[k].i;
		y=j+dirs[k].j;
		while(x>=0 && x<N && y>=0 && y<N){
		    if(status[x][y]==status[i][j])
			found++;
		    else
			break;
		    x=x+dirs[k].i;
		    y=y+dirs[k].j;

		}
#ifdef DEBUG
		cout<<"Next"<<endl;
#endif
		x=i+dirs[k].x;
		y=j+dirs[k].y;
		while(x>=0 && x<N && y>=0 && y<N){
		    if(status[x][y]==status[i][j])
			found++;
		    else
			break;
		    x=x+dirs[k].x;
		    y=y+dirs[k].y;
		}
		if(found >= K){
		    if(status[i][j]=='R')
			redok=true;
		    else if(status[i][j]=='B')
			blueok=true;
		    if(redok && blueok)
			return "BOTH";
		    break;
		}
	    }
	}
    }
#ifdef DEBUG
    cout<<"Rotate"<<endl;
#endif
    if(redok)
	return "RED";
    else if(blueok)
	return "BLUE";
    for(i=0;i<N;i++){
	k=N-1;
	for(j=N-1;j>=0;j--){
	    if(status[i][j]!='.' && j != k){
		status[i][k--]=status[i][j];
		status[i][j]='.';
	    }
	}
    }
    for(j=0;j<N;j++){
	for(i=0;i<N-1;i++){
	    if(status[i][j]=='.')
		break;
	    if(status[i][j]=='R' && redok)
		continue;
	    if(status[i][j]=='B' && blueok)
		continue;
	    found=1;
	    for(k=i+1;k<N;k++){
		if(status[k][j]==status[i][j])
		    found++;
		else
		    break;
	    }
	    if(found>=K){
		if(status[i][j]=='R')
		    redok=true;
		if(status[i][j]=='B')
		    blueok=true;
		if(redok&&blueok)
		    return "BOTH";
	    }
	}
    }
    if(redok)
	return "RED";
    else if(blueok)
	return "BLUE";
    return "Neigher";
}
int main(){
    int T;
    cin>>T;
    int i,j,k;
    for(i=1;i<=T;i++){
	cin>>N>>K;
	for(j=0;j<N;j++){
	    for(k=0;k<N;k++){
		cin>>status[j][k];
	    }
	}
	cout<<"Case #"<<i<<": "<<solve()<<endl;
    }
    return 0;
}
