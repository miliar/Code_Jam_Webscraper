#include <fstream>

using namespace std;
ifstream fin("B-large.in");
ofstream fout("B-large.out");
const int MNAX=100;
const char alf[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
int kol=0,a[MNAX+2][MNAX+2],b[MNAX+2][MNAX+2];

int Rec(int x,int y){
	int Amin=min(a[x][y-1],min(a[x][y+1],min(a[x-1][y],a[x+1][y])));
	if (Amin>=a[x][y]){
		++kol;
		b[x][y]=kol;
		return kol;
	}
	else{
		int p=0;;
		if (a[x-1][y]==Amin){
			if (b[x-1][y]>0) p=b[x-1][y];
			else p=Rec(x-1,y);
			b[x][y]=p;
			return p;
		}
		else if (a[x][y-1]==Amin){
			if (b[x][y-1]>0) p=b[x][y-1];
			else p=Rec(x,y-1);		
			b[x][y]=p;
			return p;
		}
		else if (a[x][y+1]==Amin){
			if (b[x][y+1]>0) p=b[x][y+1];
			else p=Rec(x,y+1);		
			b[x][y]=p;
			return p;
		}
		else if (a[x+1][y]==Amin){
			if (b[x+1][y]>0) p=b[x+1][y];
			else p=Rec(x+1,y);
			b[x][y]=p;
			return p;
		}
	}
}

int main(){
	int test,t;
	fin>>test;
	for (t=1;t<=test;++t){
		kol=0;
		int n,m,i,j;
		memset(b,0,sizeof(int)*(MNAX+2)*(MNAX+2));
		fin>>n>>m;
		for (i=1;i<=n;++i){a[i][0]=100000;a[i][m+1]=100000;b[i][0]=100000;b[i][m+1]=100000;}
		for (j=1;j<=m;++j){a[0][j]=100000;a[n+1][j]=100000;b[0][j]=100000;b[n+1][j]=100000;}

		for (i=1;i<=n;++i){
			for (j=1;j<=m;++j){
				fin>>a[i][j];
			}
		}
		for (i=1;i<=n;++i){
			for (j=1;j<=m;++j){
				if (b[i][j]==0){
					b[i][j]=Rec(i,j);
				}
			}
		}


		fout<<"Case #"<<t<<":\n";
		for (i=1;i<=n;++i){
			for (j=1;j<=m;++j){
				fout<<alf[b[i][j]-1]<<' ';
			}
			fout<<'\n';
		}

	}
	
	return 0;
}