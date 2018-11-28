# include <iostream.h>
# include <stdio.h>

int main()
{
    int N;
    cin>>N;
    
    int P[100],K[100],L[100];
    int List[100][1000];
    int min[100];
    //input
    for(int i=0;i<N;i++)
    {
            cin>>P[i]>>K[i]>>L[i];
            for(int j=0;j<L[i];j++)
                    cin>>List[i][j];
    }
    
    
    //sorting the lists
    
    for(int i=0;i<N;i++)
    {
            
            for(int j=1;j<L[i];j++)
            {
                    for(int k=0;k<L[i]-j;k++)
                    {
                            if (List[i][k]<List[i][k+1]) 
                               {
                               int temp=List[i][k+1];
                               List[i][k+1]=List[i][k];
                               List[i][k]=temp;
                               }
                    }
            }
            /*cout<<"\nprint list:\n";
            for(int j=0;j<L[i];j++)
                    cout<<List[i][j]<<" ";*/
            
    }
    
    //calculating answers
    for(int i=0;i<N;i++)
    {
            min[i]=0;
            int count=0;
            for(int j=0;j<P[i];j++)
                    for (int k=0;k<K[i];k++)
                        min[i]=min[i]+(List[i][count++]*(j+1));
          
    }
    
    //ouput
    
    for(int i=0;i<N;i++)
          
               cout<<"Case #"<<i+1<<": "<<min[i]<<endl;
          
            

}
                        
    
    
             
            
    
    
    
                    

            
              
                              
          
