# include <iostream.h>
# include <stdio.h>

struct grid{ int x;int y;};

int main()
    {
    int C;
    long long A[1000];
    int M[1000], N[1000];
    
    cin>>C;
    for (int i=0;i<C;i++)
        {
        cin>>N[i]>>M[i]>>A[i];
        }
        
     
              
        
    long long Area;
    int break1,solved;
     grid G[2601];
    for (int i=0;i<C;i++)
    {
   
     int count=0;
     for (int a=0;a<=M[i];a++)
         for (int b=0;b<=N[i];b++)
             {G[count].y=a;G[count++].x=b;}    
        
    break1=1,solved=0;
    if (M[i]*N[i]<A[i])
       {
       cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
       continue;
       }
                       
    for (int p1=0;p1<count && break1 ;p1++)
        {
                 for (int p2=p1+1;p2<count && break1 ;p2++)
                     {
                              for (int p3=p2+1;p3<count && break1 ;p3++)
                                  {
                        
                                               Area=abs((G[p2].x*G[p3].y-G[p3].x*G[p2].y)-(G[p1].x*G[p3].y-G[p3].x*G[p1].y)+ (G[p1].x*G[p2].y-G[p2].x*G[p1].y));
                                               if (Area==A[i])
                                                  {
                                                  cout<<"Case #"<<i+1<<": "      <<G[p1].x<<" "
                                                                                 <<G[p1].y<<" "
                                                                                 <<G[p2].x<<" "
                                                                                 <<G[p2].y<<" "
                                                                                 <<G[p3].x<<" "
                                                                                 <<G[p3].y<<" "<<endl;
                                                  break1=0;                               
                                                  solved=1;
                                                  }
                                                  }
                                                  }
                                                  }
                                               if (solved==0)  
                                                   cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;    
                                               }                                               
                                                    

    }
