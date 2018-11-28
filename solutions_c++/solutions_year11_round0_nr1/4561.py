#include "cstdio"
#include "iostream"
#include "conio.h"
using namespace std;
main()
{
      long t,u,v,n,vt1,vt2,kq1,kq2,k,kq;
      FILE *f1;
      FILE *f2;
      f1=fopen("A-large.in","r");
      f2=fopen("quan.out","w");
      char c;
      fscanf(f1,"%ld\n",&t);
      for (u=1;u<=t;u++)
       {
                        fscanf(f1,"%ld ",&n);
                        vt1=1;
                        vt2=1;
                        kq1=0;
                        kq2=0;
                        kq=0;
                        for (v=1;v<=n;v++)
                         {
                                          fscanf(f1,"%c %ld ",&c,&k);
                                          if (c=='O')
                                            {
                                            kq1=kq1+abs(k-vt1)+1;
                                            if (kq1<=kq)
                                             {
                                                        kq=kq+1;
                                                        kq1=kq;
                                             }
                                            else kq=kq1;
                                            vt1=k;
                                            }
                                          if (c=='B')
                                            {
                                            kq2=kq2+abs(k-vt2)+1;
                                            if (kq2<=kq)
                                             {
                                                        kq=kq+1;
                                                        kq2=kq;
                                             }
                                            else kq=kq2;
                                            vt2=k;
                                            }
                         }
                        //cout<<"Case #"<<t<<": "<<kq<<"\n";
                        fprintf(f2,"Case #%ld: %ld\n",u,kq);
                        //if (kq1>kq2) cout<<"Case #"<<t<<": "<<kq1<<"\n"; else cout<<"Case #"<<t<<": "<<kq2<<"\n";
       }
      //getch();
}
