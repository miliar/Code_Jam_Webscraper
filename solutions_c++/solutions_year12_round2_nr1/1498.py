      #include<iostream>
        #include<stdlib.h>
 
 
        using namespace std;
 
 
 
        int main()
        {
                int a,c,t,i,j,k=0,n;
                long double *b,sum=0,m,check=0,check2=0;
                cin>>t;
                while(t--)
                {
                        k++;
                        cin>>n;
                        b=new long double[n+1];
                        for(i=0;i<n;i++)
                        {
                                cin>>b[i];
                                sum=sum+b[i];
                        }
                        cout<<"Case #"<<k<<": ";
                        for(i=0;i<n;i++)
                        {
                                m=100*(((2*sum)-(b[i]*n))/(sum*n));
                                if(m<0)
                                {m=0;check2++;}
                                b[i]=m;
                                check=check+b[i];
                                
                        }
                        
                        check=(100-check)/(n-check2);
                                for(i=0;i<n;i++)
                        {
                                m=b[i]+check;
                                if(m<0)
                                        m=0;
                                printf("%.6Lf " , m);
                        }
 
                        cout<<endl;
                        check=check2=sum=0;
                        free(b);
                }
 
 
                
                return 0;
        }