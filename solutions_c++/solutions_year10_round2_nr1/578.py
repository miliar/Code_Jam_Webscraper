#include <iostream>
#include <vector>
using namespace std;

public class LinearTravellingSalesman
{
int dis(int x1,int y1,int x2,int y2)
{int ans=0;
if(x1>x2)
 ans+=x1-x2;
else ans+=x2-x1;
if(y1>y2)
 ans+=y1-y2;
else ans+=y2-y1;
return ans;
}

int prim(int n,int mat[60][60],int *pre){
	int min[60],ret=0;
	int v[60],i,j,k,*pre;
	for (i=0;i<n;i++)
		{min[i]=10000;v[i]=0;pre[i]=-1;}
	for (min[j=0]=0;j<n;j++){
		for (k=-1,i=0;i<n;i++)
			if (!v[i]&&(k==-1||min[i]<min[k]))
				k=i;
		for (v[k]=1,ret+=min[k],i=0;i<n;i++)
			if (!v[i]&&mat[k][i]<min[i])
				min[i]=mat[pre[i]=k][i];
	}
	return ret;
}

int findMinimumDistance(vector <int> x, vector <int> y)
{
int mat[60][60];
int n=x.size();
for(int i=1;i<=n;i++)
  for(int j=1;j<=n;j++)
    mat[i][j]=mat[j][i]=dis(x[i-1],x[j-1],y[i-1],y[j-1]);
return prim(n,mat);

}
/*
int main()
{
vector<int> v1,v2;
int l;
cin >>l;
for(int i=1;i<=l;i++)
  cin>>v1[i-1];
for(int i=1;i<=l;i++)
  cin>>v2[i-1];
cout <<findMinimumDistance(v1,v2);
return 0;
}
*/


};
