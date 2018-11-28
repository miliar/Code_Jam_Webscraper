#include<stdio.h>
#include<math.h>
int main()
{
    freopen("C-large.in","rt",stdin);
    freopen("output.out","wt",stdout);
    int T,k=1,i,j,r,len,no,count,rtemp=0,notemp=0,q=0,h=0,flag=0,arr[10000];
    long long A,B;
    double a;
    scanf("%d",&T);
    while(T)
    {
            scanf("%ld%ld",&A,&B);
            count=0;
            for(i=A;i<B;i++)
            {
                            no=i;
                            len=0;
                          
                            while(no)
                            {
                                    no/=10;
                                    len++;
                            }
                            no=i;
                            q=0;
                            
                            for(j=1;j<len;j++)
                            
                            {
                                              
                                    a=pow(10,j);
                                    r=no%(int)a;
                                    rtemp=r;
                                    no/=(int)a;
                                    notemp=no;
                                    a=pow(10,len-j);
                                    r*=(int)a;
                                    r+=no;
                              
                                if(r<=B && i<r)
                                    {
                                        flag=0;
                                        for(h=0;h<q;h++)
                                        if(arr[h]==r)
                                        flag=1;
                                        if(!flag)
                                        count++; 
                                    arr[q]=r;
                                    q++;
                                   
                                     }
                                    no=i;
                            }                              
            }
            printf("Case #%d: %d\n",k,count);
            k++;
            T--;
            
    }
}
