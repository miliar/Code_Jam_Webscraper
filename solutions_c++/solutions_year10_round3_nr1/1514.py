#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<stack>
using namespace std;
class point
{
public:
	int l,r;
};
int mat[1000][1000];
point* vec;
int GLOBALN;
int check(int index1,int index2)
{
	
	if(index1>GLOBALN || index2>GLOBALN)
		return 0;
	if(mat[index1][index2]!=-1)return mat[index1][index2];
	
	int l1=vec[index1].l, r1=vec[index1].r, l2=vec[index2].l, r2=vec[index2].r;
	int result=-1;
	if((l1 <= l2 && r1<=r2) || (l1 >= l2 && r1>=r2))
	{
		
		
		mat[index1][index2]=0;
		mat[index2][index1]=0;
		result=mat[index1][index2];
	}
	else
	{
		
		mat[index1][index2]=1;
		mat[index2][index1]=1;
		result=mat[index1][index2];
	}
	result+= max(check(index1+1,index2),check(index1,index2+1));
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int T=0;
	cin>>T;
	for(int i=0; i<T;i++)
	{
		memset(mat,-1,sizeof(mat));
		int N=0;
		cin>>N;
		GLOBALN=N;
		vec=new point[N];
		for(int j=0; j<N; j++)
		{
			cin>>vec[j].l;
			cin>>vec[j].r;
		}
		int r=check(0,0),cal=0;
		r=0;
		for(int i=0; i<N;i++)
		{
			r=0;
			for(int j=0; j<N;j++)
			{
				
				r+=mat[i][j];
			}
			cal=max(cal,r);		
		}
			cout<<"Case #"<<(i+1)<<": "<<cal<<endl;
		delete vec;
	}
	return 0;
}
