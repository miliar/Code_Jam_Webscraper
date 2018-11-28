#include<iostream>
#include<cstdio>
int main()
{
    int n,s,p,i,j,k,t,T,m;
    freopen("C:/inputb.in","r",stdin);
    freopen("C:/outputb.txt","w",stdout);
    scanf("%d",&T);
    //printf("%d",T);
    t=0;
    while(t++<T)
    {
                 scanf("%d %d %d",&n,&s,&p);
                 //printf("%d %d %d ",n,s,p);
                 for(i=0,j=0;i<n;i++)
                 {
                                     scanf("%d",&m);
                                     if(m==0){k=0;}
                                     else{k=m/3;m-=3*k;}
                                     
                                     
                                     if(p<=k)
                                     j++;
                                     else if(p<=k+1 && m>0)
                                     j++;
                                     else if(s>0 && p<=k+1 && k>0)
                                     {j++;s--;}
                                     else if(s>0 && p<=k+2 && m==2)
                                     {j++;s--;}
                  
                                     }
                  printf("Case #%d: %d\n",t,j);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
