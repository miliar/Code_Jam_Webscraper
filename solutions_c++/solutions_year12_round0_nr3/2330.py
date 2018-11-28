#include<iostream.h>

int main()
{
    long T=0,arr[101],A,B,i,j=1,tmp,z,f,tmp2,tmp3,tmp4,c,counter;
    cin>>T;
    while(T>0)
    {
         cin>>A>>B;
         counter=0;
         for(i=A;i<=B;i++)
         {     
               tmp=i;
               do
               {
                            z=tmp%10;
                            if(z!=0)
                            {
                            f=tmp/10;
                            tmp2=f;
                            c=1;
                            while(tmp2!=0)
                            {
                                          tmp2/=10;
                                          c*=10;
                            }
                            f+=(c*z);
                            }
                            else
                            {
                                tmp2=tmp/10;
                                c=10;
                                while(tmp2%10==0)
                                {
                                                 tmp2/=10;
                                                 c*=10;
                                }
                                c*=10;
                                tmp3=tmp%c;
                                tmp2/=10;
                                tmp4=tmp2;
                                c=1;
                                while(tmp2!=0)
                                {
                                              tmp2/=10;
                                              c*=10;
                                }
                                f=tmp3*c+tmp4;
                            }
                            if(f<=B && f>=A && f>i)
                                    counter++;
                        //    cout<<i<<" "<<counter<<" \n";
                            tmp=f;
               }
               while(tmp!=i);
         }
         cout<<"Case #"<<j++<<": "<<counter<<"\n";
         T--;
    }
    return 0;
}
