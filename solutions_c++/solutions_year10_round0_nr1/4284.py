#include<iostream>
using namespace std;
int t,n,k;
int a[11];
int b[11];
int main()
{
    int i=0,j,flag,s;
    freopen("A-small-attempt13.in.txt","r",stdin);
    freopen("hh.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&k);   
        for(j=1;j<=10;j++){a[j]=0;b[j]=0;}
        printf("Case #%d: ",++i);
        for(j=1;j<=k;j++)
        {
			b[1]=1;
            for(s=1;s<=n;s++)
				if(b[s])a[s]=1-a[s];
            for(s=2;s<=n;s++)
			{
			    if(a[s-1]&&b[s-1])b[s]=1;
			    if(!a[s-1]||!b[s-1])b[s]=0;
			} 
        }
        if(a[n]&&b[n])printf("ON\n");
        else printf("OFF\n");
    }
   // fclose(stdin);
   // fclose(stdout);
    return 0;
}
