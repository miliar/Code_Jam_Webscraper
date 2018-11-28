#include<iostream>
using namespace std;
char M[52][52],RM[52][52];
 

bool find(int n,int k,char key)
{
    int i,j,t,ii,jj;
   for(i=0;i<n;i++)
	   for(j=0;j<n;j++)
		   if(RM[i][j]==key)
		   {
			   int cnt=0;
		       for(t=j;t<n;t++)if(RM[i][t]==key)cnt++; else break;
			   if(cnt>=k)
				   return true;

			   cnt=0;
		       for(t=i;t<n;t++)if(RM[t][j]==key)cnt++; else break;
			   if(cnt>=k)
				   return true;

			    cnt=0;
				for(ii=i,jj=j;jj>=0 && ii<n;jj--,ii++)
					  if(RM[ii][jj]==key)cnt++; else break;
			   if(cnt>=k)
				   return true;

			    cnt=0;
			   	for(ii=i,jj=j;jj>=0 && ii<n;jj++,ii++)
					   if(RM[ii][jj]==key)cnt++; else break;
			   if(cnt>=k)
				   return true;

		   }
  return false;
}

int Count(int n,int k)
{

	bool R=find(n,k,'R'),B=find(n,k,'B');

    if(R&&B)return 2;

	if(R)return 0;
	if(B)return 1;

return -1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ans.txt","w",stdout);
	int i,j,T,K,n;
	cin>>T;
	for(int ca=1;ca<=T;ca++)
	{
	 cout<<"Case #"<<ca<<": ";
	   cin>>n>>K;
      for(i=0;i<n;i++)
		    cin>>M[i];

		   for(i=0;i<n;i++)
			   for(j=0;j<n;j++)
			     RM[j][n-1-i]=M[i][j];


			   int bu;
			 for(j=0;j<n;j++)
			   for(bu=n-1,i=n-1;i>=0;i--)
				   if(RM[i][j]!='.')
				   {
					   RM[bu][j]=RM[i][j];
				       if(bu!=i)RM[i][j]='.';
				      bu--;
				   }

 //for(i=0;i<n;i++)
//	 cout<<RM[i]<<'\n';


     int cnt=Count(n,K);
	  switch (cnt)
	  {
	  case 0:
		  cout<<"Red"<<endl;
		  break;
	  case 1:
		  cout<<"Blue"<<endl;
		  break;
	  case 2:
		  cout<<"Both"<<endl;
		  break;
	  default:
         cout<<"Neither"<<endl;

	  }

	   
	}
  return 0;
}