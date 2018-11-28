#include<iostream>
using namespace std;
int a[40];
int main()
{
    freopen("A-large.in","r",stdin);
	freopen("1.txt","w",stdout);
	int cas=0;
	int t,n,i,j;scanf("%d",&t);while(t--){
	     scanf("%d",&n);
		 for(i=0;i<n;i++){
            a[i]=0;char c;
		    for(j=0;j<n;j++){
		    scanf(" %c",&c);
		    if(c=='1')
		    a[i]=j;
			}
			//printf("%d ",a[i]);
	     }int ans=0;
	     for(i=0;i<n;i++)
	     {
		    //for(j=0;j<n;j++)printf("%d ",a[j]);printf("\n");
			for(j=i;j<n;j++)
			if(a[j]<=i)break;//printf("%d\n",j);
			int temp=j;ans+=j-i; 
			for(j=temp;j>=i+1;j--)a[j]=a[j-1];				 
         }
	     printf("Case #%d: %d\n",++cas,ans);
	}
}
