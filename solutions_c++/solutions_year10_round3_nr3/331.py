#include<iostream>
using namespace std;
const int MAXN=600;
char a[MAXN][MAXN];
int M,N;
bool in(int x,int y,int L)
{
	int cnt=0,i=x,j=y;
	for(i=x;i<x+L;i++)
		for(j=y;j<y+L;j++)
			if(a[i][j]==3)
			{
			  return true;
			}
  return false;
}

bool satisfy_oneLine(int x,int y,int L)
{
   for(int i=y;i<y+L-1;i++)
	   if(a[x][i]==a[x][i+1])
		   return false;
return true;
}

bool equ(int x,int y,int L)
{
     for(int i=y;i<y+L;i++)
		 if(a[x][i]==a[x+1][i])
			 return false;

		 return true;

}

bool can(int x,int y,int L)
{
	if(x+L>M||y+L>N)return false;

   if(in(x,y,L))return false;

 
   if(!satisfy_oneLine(x,y,L))return false;

  int i,j;
  for(i=0;i<L-1;i++)
	  if(!equ(x+i,y,L))
		  return false;


 
   	for(i=x;i<x+L;i++)
		for(j=y;j<y+L;j++)
			 a[i][j]=3;

return true;
		
}

int ans[MAXN],len,cnt[MAXN];
void solve()
{
	len=0;
	int L=N>M?M:N,i,j;
	memset(cnt,0,sizeof(cnt));
	bool ext=false;
   for(;L>0;L--)
   {
 

      for(i=0;i<M;i++)
		  for(j=0;j<N;j++)
		  {
		     if(can(i,j,L))
			 {
			   ans[len]=L;
			   cnt[len]++;
			   ext=true;
			   
			 }
		  }

		  if(ext)
		  {
			  ext=false;
		      len++;
		  }
   }
}

/*void out()
{
  int i,j;
  	for(i=0;i<M;i++)
		{
			for(j=0;j<N;j++)
			{
			 cout<<(char)(a[i][j]+'0');
			}
			cout<<endl;
		}
}*/

int main()
{
	 freopen("C-small-attempt0.in","r",stdin);
	 freopen("ans.txt","w",stdout);

   int T,i,j,temp;
   char str[MAXN];
   cin>>T;
   for(int t=1;t<=T;t++)
   {
	   cin>>M>>N;
	   int k;
	    for(i=0;i<M;i++)
		{
			cin>>str;
			for(k=0,j=0;j<N/4;j++)
			{
			   if(str[j]>='0'&&str[j]<='9')str[j]-='0';
			   else str[j]=str[j]-'A'+10;	 

			   temp=str[j];
               a[i][k++]= (temp>>3)&1;
			   a[i][k++]=(temp>>2)&1; 
			   a[i][k++]=(temp>>1)&1; 
			   a[i][k++]=temp&1; 
	 
			}
		}

 
	 
	solve();
       cout<<"Case #"<<t<<": "<<len<<endl;


      
	 for(i=0;i<len;i++)
	 {
	    cout<<ans[i]<<" "<<cnt[i]<<endl;
	 }



   }


return 0;
}