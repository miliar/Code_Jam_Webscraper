#include<iostream>
using namespace std;
int main()
{
    int t ,n ,k ,i =0,j,m;
    unsigned int *power,*state;
    cin >> t ;
    while(i < t )
    {
            cin >> n >> k;
            power = new unsigned int [n+1];
            state = new unsigned int [n+1];
            for(j=0 ;j < n ;j++)
            {
                    if(j==0)
                    {
                            power[j] =1;
                            state[j] =0;
                    }
                    else
                    {
                        power[j] =0;
                        state[j] =0;
                    }
            }       
            for(j = 0; j < k ;j++)
            {
                   
                  for(m = 0 ;m < n ; m++)
                  {
                        if(power[m] == 1)
                        //state[m] = ~state[m];
                        {
                                   if(state[m]==0)
                                   state[m]=1;
                                   else if(state[m]==1)
                                   state[m]=0;
                                   }         
                  }
                  for(m = 1 ;m < n ;m++)
                  {
                        if( power[m-1]& state[m-1])
                        power[m]=1;
                        else
                        power[m]= 0;
                  }
            }
                  
            
            if(power[n-1] & state[n-1])
            {
                          cout << "Case #"<<i+1<<": ON\n";
            }
            else
            {
                         cout <<"Case #"<<i+1<<": OFF\n";
            }
            i++;
    }   
    //system("pause");
    return 0;
}
                  
