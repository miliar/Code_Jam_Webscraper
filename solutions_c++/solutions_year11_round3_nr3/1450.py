#include<stdio.h>
FILE *in,*out;
long long int tt,t_store,j,k,l,n,h,i,high[1000],low[1000],leave,lcm,temp,flag,tempo;

int gcd(int a, int b){
    if(a == b)
        return a;
    if (a==0)
        return b;
    if (b==0)
        return a;
    if(a>b)return (gcd(a%b,b));
    else return gcd(b,a);
}
main()
{in=fopen("in.txt","r");
out=fopen("out.txt","w");
fscanf(in,"%lld",&tt);
t_store=tt;
  while(tt--)
{fscanf(in,"%lld%lld%lld",&n,&l,&h);
j=0;
k=0;
for(i=0;i<n;i++)
{fscanf(in,"%lld",&temp);
if(temp<l){low[j]=temp;j++;}
else {high[k]=temp;k++;}
                }
j--;              
k--;
temp=1;lcm=1;
if(j==-1)lcm=1;
else {for(i=0;i<=j;i++)
     {tempo=gcd(temp,low[i]);
      temp=temp*low[i]/tempo;
     if(temp>h)
     {flag=0;break;} 
      }
     lcm=temp;
     }
     flag=1;
leave=0;
temp=lcm;
if(lcm>h){flag=0;}
else {i=1;
     
     while(flag==1&&leave==0){temp=lcm*i;
                        if(temp<l){i++;}
                        else 
				{if(temp>h)
					{flag=0;leave=1;}
				else 
					{
					if(k!=-1)
						{
						for(j=0;j<=k;j++)
							{
                           if(high[j]%temp!=0&&temp%high[j]!=0)
								{
								flag=0;}
							}
if(flag==1)							leave=1;
         else {flag=1;i++;}                   }
                            else leave=1;
                        		}
				}
             		}
     	}
printf("%lld\n",t_store-tt);
if(flag==0)
fprintf(out,"Case #%lld: NO\n",t_store-tt);
else 
fprintf(out,"Case #%lld: %lld\n",t_store-tt,temp);      }

}
