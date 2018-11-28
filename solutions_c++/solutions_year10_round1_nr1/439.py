#include<cstdio>
#include<iostream>
using namespace std;
const int N=50;
int n,k;
char a[N][N];
int check(char target){
	int flag;
	for (int i=0;i<n;i++){
		flag=0;
		for (int j=0;j<n;j++)
			if (a[i][j]==target){
				flag++;
				if (flag==k)
					return 1;
			}else
				flag=0;
	}
	for (int i=0;i<n;i++){
		flag=0;
		for (int j=0;j<n;j++)
			if (a[j][i]==target){
				flag++;
				if (flag==k)
					return 1;
			}else
				flag=0;
	}
	int x,y;
	for (int i=0;i<n;i++){
		flag=0;
		for (x=0,y=i;y<n;x++,y++)
			if (a[x][y]==target){
				flag++;
				if (flag==k)
					return 1;
			}else 
				flag=0;
		flag=0;
		for (x=n-1,y=i;y<n;x--,y++)
			if (a[x][y]==target){
				flag++;
				if (flag==k)
					return 1;
			}else 
				flag=0;
	}
	for (int i=0;i<n;i++){
		flag=0;
		for (x=i,y=0;x<n;x++,y++)
			if (a[x][y]==target){
				flag++;
				if (flag==k)
					return 1;
			}else 
				flag=0;
		flag=0;
		for (x=i,y=0;x>=0;x--,y++)
			if (a[x][y]==target){
				flag++;
				if (flag==k)
					return 1;
			}else 
				flag=0;
	}
	return 0;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		cin>>n>>k;
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				cin>>a[j][n-i-1];
		for (int j=0;j<n;j++){
			int k=n-1;
			for (int i=n-1;i>=0;i--){
				while (k>=0 && a[k][j]=='.')
					k--;
				if (k>=0)
					a[i][j]=a[k--][j];
				else
					a[i][j]='.';
			}
		}
		int flag=check('R')+check('B')*2;
		cout<<"Case #"<<t<<": ";
		if (flag==0)
			cout<<"Neither"<<endl;
		else if (flag==1)
			cout<<"Red"<<endl;
		else if (flag==2)
			cout<<"Blue"<<endl;
		else if (flag==3)
			cout<<"Both"<<endl;
	}
	return 0;
}
