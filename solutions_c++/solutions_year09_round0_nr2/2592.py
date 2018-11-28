#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int a[100][100],b[100][100];
int row,col,num,inx;

bool check(int r1,int c1,int r2,int c2);
void work();
void work_it(int r,int c);

int main()
{
	ifstream fin("f:\\input.txt");
	ofstream fout("f:\\output.txt");
	fin>>num;
	for (int i=0; i<num;i++){
		fin>>row>>col;
		for(int j=0;j<row;j++){
			for (int k=0;k<col;k++){
				fin>>a[j][k];
				b[j][k]=-1;
			}
		}
		inx=0;
		work();
		fout<<"Case #"<<i+1<<":"<<endl;
		for(int j=0;j<row;j++){
			for(int k=0;k<col-1;k++){
				fout<<(char)('a'+b[j][k])<<" ";
				cout<<b[j][k]<<" ";
			}
			fout<<(char)(b[j][col-1]+'a')<<endl;
			cout<<b[j][col-1]<<endl;
		}
	}
	return 0;
}

bool check(int r1,int c1,int r2,int c2)
{
	int tc1,tr1;
	int tmp[4];
	if( a[r1][c1]==a[r2][c2]) return false;
	if( a[r1][c1]>a[r2][c2]){
		tr1=r1;
		tc1=c1;
		r1=r2;
		c1=c2;
		r2=tr1;
		c2=tc1;
	}
	tmp[0]=100000;tmp[1]=100000;tmp[2]=100000;tmp[3]=100000;
	int m,n;

	n=r2-1;
	m=c2;
	if(m>=0 && m<col && n>=0 && n<row){
		tmp[0]=a[n][m];
	}
	n=r2;
	m=c2-1;
	if(m>=0 && m<col && n>=0 && n<row){
		tmp[1]=a[n][m];
	}
	n=r2;
	m=c2+1;
	if(m>=0 && m<col && n>=0 && n<row){
		tmp[2]=a[n][m];
	}
	n=r2+1;
	m=c2;
	if(m>=0 && m<col && n>=0 && n<row){
		tmp[3]=a[n][m];
	}

	int k=0,kmin=tmp[0];
	for (int i=1;i<4;i++){
		if(tmp[i]<kmin){
			kmin=tmp[i];
			k=i;
		}
	}
	switch (k){
		case 0: n=r2-1;m=c2;break;
		case 1: n=r2;m=c2-1;break;
		case 2: n=r2;m=c2+1;break;
		case 3: n=r2+1;m=c2;break;
	}
	if(n==r1 && m==c1) return true;
	return false;
	
}
void work_it(int r,int c)
{
	if(b[r][c]!=-1) return;
	b[r][c]=inx;
	int m,n;
	n=r-1;
	m=c;
	if(m>=0 && m<col && n>=0 && n<row){
		if(check(r,c,n,m)){
			work_it(n,m);
		}
	}
	n=r;
	m=c-1;
	if(m>=0 && m<col && n>=0 && n<row){
		if(check(r,c,n,m)){
			work_it(n,m);
		}

	}
	n=r;
	m=c+1;
	if(m>=0 && m<col && n>=0 && n<row){
		if(check(r,c,n,m)){
			work_it(n,m);
		}

	}
	n=r+1;
	m=c;
	if(m>=0 && m<col && n>=0 && n<row){
		if(check(r,c,n,m)){
			work_it(n,m);
		}

	}

}
void work()
{
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			if(b[i][j]==-1){
				work_it(i,j);
				inx+=1;
			}
		}
	}
}
