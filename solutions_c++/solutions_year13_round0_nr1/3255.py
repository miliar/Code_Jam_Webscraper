#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
inline int p(int r,int c){return r*4+c;}
#define O 'O'
#define X 'X'
#define T 'T'
#define D '.'
int main(){
	//freopen("test.in","r",stdin);freopen("test.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("C-large-practice.in","r",stdin);freopen("C-large-practice.out","w",stdout);
	char* b=new char[16];
	int numIter;
	scanf("%d",&numIter);
	for(int t=0;t<numIter;t++){
		int gameState=0;
		string s;
		for(int i=0;i<4;i++){
			cin>>s;
			for(int z=0;z<4;z++){
				b[p(i,z)]=s[z];
			}
		}
		cin.get();
		/*for(int r=0;r<4;r++){
			for(int c=0;c<4;c++){
				cout<<b[p(r,c)];
			}
			cout<<endl;
		}*/
		int numPieces=0;
		int odcount=0,xdcount=0,oddcount=0,xddcount=0;
		for(int r=0;r<4;r++){
			int ohcount=0;
			int ovcount=0;
			int xvcount=0;
			int xhcount=0;
			
			for(int c=0;c<4;c++){
				if(b[p(r,c)]==O)ohcount++;
				else if(b[p(r,c)]==X)xhcount++;
				else if(b[p(r,c)]==T){ohcount++;xhcount++;}				
				if(b[p(c,r)]==O)ovcount++;
				else if(b[p(c,r)]==X)xvcount++;
				else if(b[p(c,r)]==T){ovcount++;xvcount++;}	
				if(b[p(r,c)]!=D)numPieces++;
			}
			if(b[p(r,r)]==O)odcount++;
			else if(b[p(r,r)]==X)xdcount++;
			else if(b[p(r,r)]==T){odcount++;xdcount++;}
			if(b[p(r,3-r)]==O)oddcount++;
			else if(b[p(r,3-r)]==X)xddcount++;
			else if(b[p(r,3-r)]==T){oddcount++;xddcount++;}
			if(ohcount==4||ovcount==4||odcount==4||oddcount==4){
				gameState=1;
				break;
			}else if(xhcount==4||xvcount==4||xdcount==4||xddcount==4){
				gameState=2;
				break;
			}
		}
		//cout<<"num pieces="<<numPieces<<endl;
		if(numPieces==16&&gameState==0){
			gameState=3;
		}
		cout<<"Case #"<<t+1<<": ";
		switch(gameState){
		case 0:
			cout<<"Game has not completed"<<endl;
			break;
		case 1:
			cout<<"O won"<<endl;
			break;
		case 2:
			cout<<"X won"<<endl;
			break;
		case 3:
			cout<<"Draw"<<endl;
			break;
		default:
			cout<<"wtf"<<endl;
		}
	}
	return 0;
}
