#include<iostream>
using namespace std;

int l,t,n,c;
int xunhuan[1005];
int goI(int res,int i)
{
 	if(res<t)
    {
		          if((res+xunhuan[i%c]*2)<=t)
		              res+=(xunhuan[i%c]*2);
                  else
                  {
				   	  res=t+xunhuan[i%c]-(t-res)/2;
  	              }
    }
    else
        res+=xunhuan[i%c];
    return res;
}
int main()
{
 	int tt;
 	int p,q;
 	freopen("B-small-attempt1.in","r",stdin);
    freopen("out1.txt","w",stdout);
    scanf("%d",&tt);
    int cas;
    int i,j,k;
    int sum;
    int res;
    for(cas=1;cas<=tt;cas++)
    {
	   scanf("%d%d%d%d",&l,&t,&n,&c);
	   sum=0;
	   for(i=0;i<c;i++)
	   {
	         scanf("%d",&xunhuan[i]);
	         sum+=(xunhuan[i]*2);
	   }
	   res=0;
       if(l==0)
       {
  		   res+=((n/c)*(sum));
  		   for(i=0;i<(n%c);i++)
  		       res+=(xunhuan[i]*2);
           printf("Case #%d: %d\n",cas,res);
           continue;
	   }
	   int minn=99999999;
	   if(l==1)
	   {
	       for(i=0;i<n;i++)
	       {
	          res=0;
			  for(j=0;j<i;j++)
			  {
			      res+=(xunhuan[j%c]*2);
			  }
			  //if(res<t) res=t;
			  //res+=xunhuan[i%c];
			  /*if(res<t)
			  {
		          if(res+xunhuan[i%c]*2<=t)
		              res+=(xunhuan[i%c]*2);
                  else
                  {
				   	  res=t+xunhuan[i%c]-(t-res)*0.5;
  	              }
		      }
		      else
		          res+=xunhuan[i%c];*/
              res=goI(res,i);
			  for(j=i+1;j<n;j++)
			      res+=(xunhuan[j%c]*2);
		      minn=minn<res?minn:res;
		     // cout<<"****"<<res<<endl;
           }
           printf("Case #%d: %d\n",cas,minn);
           continue;
	   }
	   if(l==2)
	   {
	   		   res=0;
	   		   minn=99999999;
	   		   for(i=0;i<n;i++)
   		       {
				    for(j=i+1;j<n;j++)
				    {
	 				   res=0;
 				       for(p=0;p<i;p++)
 				           res+=(xunhuan[p%c]*2);
	                   
	                  // if(res<t) res=t;
	                   //res+=xunhuan[i%c];
	                   res=goI(res,i);
					   for(p=i+1;p<j;p++)
					       res+=(xunhuan[p%c]*2);
	                   //res+=xunhuan[j%c];
	                   res=goI(res,j);
				       for(p=j+1;p<n;p++)
				           res+=(xunhuan[p%c]*2);
					   minn=minn<res?minn:res;
 				    }
 				    
		       }
		       printf("Case #%d: %d\n",cas,minn);
               continue;
	   }
    }
    return 0;
}
