#include<iostream>
using namespace std;

main()
{
      int t,no=1;
      scanf("%d",&t);
      while(t--)
      {
                int n;
                scanf("%d",&n);
//                cout<<n;
                int b[n];
                char p[n], c;
                int i,j,k,l;
                for(i=0;i<n;i++)
                {
                                scanf(" %c %d",&c,&k);
//                                cout<<c<<" "<<k<<endl;
                                p[i]=c;
                                b[i]=k;
                }
                
                int posb=1,poso=1,mo=0,mb=0,moves=0;
                
                for(i=0;i<n;i++)
                {
                                if(p[i]=='O')
                                {
                                             k=abs(poso-b[i])+1;
                                             poso=b[i];
                                             moves=max(mo+k,moves+1);
                                             mo=moves;
                                }
                                else if(p[i]=='B')
                                {
                                             k=abs(posb-b[i])+1;
                                             posb=b[i];
                                             moves=max(mb+k,moves+1);
                                             mb=moves;
                                }
                                else
                                {
                                    cout<<"Invalid Input"<<endl;
                                }
                
                }
//                cout<<"Moves: "<<moves<<endl;
//                      printf("Hello\n");
                        printf("Case #%d: %d\n", no++,moves);
      }
//system("PAUSE");
}
