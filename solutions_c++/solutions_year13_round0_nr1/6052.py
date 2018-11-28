#include<iostream>
#include<cstdio>
char A[4][4];
using namespace std;
bool isx(int i,int j){
	if(A[i][j]=='X'||A[i][j]=='T')
		return true;
	return false;
}
bool iso(int i,int j){
	if(A[i][j]=='O'||A[i][j]=='T')
		return true;
	return false;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int u=1;u<=T;++u){
		for(int i=0;i<4;++i){
			for(int j=0;j<4;++j)
				cin>>A[i][j];
		}
		bool xwin=false;
		bool owin=false;
		
		for(int i=0;i<4;++i){
			bool xcur=true;
			bool ocur=true;
			for(int j=0;j<4;++j){
				if(!isx(i,j))
					xcur=false;
				if(!iso(i,j))
					ocur=false;
			}
			if(xcur)
				xwin=true;
			if(ocur)
				owin=true;
		}
		for(int j=0;j<4;++j){
			bool xcur=true;
			bool ocur=true;
			for(int i=0;i<4;++i){
				if(!isx(i,j))
					xcur=false;
				if(!iso(i,j))
					ocur=false;
			}
			if(xcur)
				xwin=true;
			if(ocur)
				owin=true;
		}
		if(iso(0,0)&&iso(1,1)&&iso(2,2)&&iso(3,3))
			owin=true;
		if(isx(0,0)&&isx(1,1)&&isx(2,2)&&isx(3,3))
			xwin=true;
		if(iso(3,0)&&iso(2,1)&&iso(1,2)&&iso(0,3))
			owin=true;
		if(isx(3,0)&&isx(2,1)&&isx(1,2)&&isx(0,3))
			xwin=true;
		cout<<"Case #"<<u<<": ";
		if(xwin)
			cout<<"X won"<<endl;
		else if(owin)
			cout<<"O won"<<endl;
		else{
			bool isd=true;
			for(int i=0;i<4;++i)
				for(int j=0;j<4;++j)
					if(A[i][j]=='.')
						isd=false;
			if(isd)
				cout<<"Draw"<<endl;
			else
				cout<<"Game has not completed"<<endl;
		}
	}
	return 0;
}
