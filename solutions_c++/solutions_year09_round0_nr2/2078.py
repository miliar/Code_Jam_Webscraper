#include <iostream>
#include <map>
#include <list>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int a[101][101];
int ans[101][101];
int predx[101][101];
int predy[101][101];
int h,w;

int b[2][4] = {
		{-1,0,0,1},
		{0,-1,1,0}	
		};
char alphabets[30]="abcdefghijklmnopqrstuvwxyz";

int main()
{
  int tc,T;
  cin>>T;
  for(tc=1;tc<=T;++tc)
  {
     cin>>h>>w;
     for(int i=0;i<h;++i)
	for(int j=0;j<w;++j)
	   {cin>>a[i][j];ans[i][j]=0;predx[i][j]=predy[i][j]=-1;}
     //memset(predx,-1,sizeof predx);	
     //memset(predy,-1,sizeof predy);
     
     list<int> x;list<int> y;
	int ind=1;
     for(int m=0;m<h;++m)
       for(int n=0;n<w;++n)
     {
	if(ans[m][n]!=0) continue;
//	cout<<"new****\n";
	x.clear();y.clear();
     	x.push_back(m);y.push_back(n);
     	ans[m][n]=ind++;	
     	while(!x.empty())
     	{
		int p=x.front(),q=y.front();
		x.pop_front();y.pop_front();
		int mn = a[p][q],px=p,qy=q;
//		cout<<p<<' '<<q<<endl;
		for(int i=0;i<4;++i)
		{
	   		if(p+b[0][i]>=0 && p+b[0][i]< h && q+b[1][i]>=0 && q+b[1][i]<w)
	    		{
				if (a[p+b[0][i]][q+b[1][i]] < mn)
				{
					mn = a[p+b[0][i]][q+b[1][i]];
					px=p+b[0][i]; qy= q+b[1][i];		
				}
	    		}
		}
	   	if (px==p && qy==q) continue;
		//cout<<"px=="<<px<<" qy=="<<qy<<endl;
	   	predx[px][qy]=p;predy[px][qy]=q;
	   	if (ans[px][qy]==0)
	   		{ans[px][qy]=ans[p][q];x.push_back(px);y.push_back(qy);}
		else if (ans[px][qy]<ans[p][q]){
			int ii=p,jj=q;
			ans[ii][jj]=ans[px][qy];
			//cout<<"heeeee\n";
			  // cout<<p<<' '<<q<<"=="<<ans[px][qy]<<endl;
			while(predx[ii][jj]!=-1)
			{
			   ans[predx[ii][jj]][predy[ii][jj]] = ans[px][qy];
			   //cout<<predx[ii][jj]<<' '<<predy[ii][jj]<<"=*"<<ans[px][qy]<<endl;
			   int k=ii; 
			   ii=predx[ii][jj];jj=predy[k][jj];					
			}
			--ind;			
		}	
	}
     }
	
	cout<<"Case #"<<tc<<":\n";
	for(int i=0;i<h;++i)
	{
	   for(int j=0;j<w;++j)
		cout<<alphabets[ans[i][j]-1]<<' ';			
	   cout<<endl;	
	}

  }
    
}
