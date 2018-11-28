#include<iostream>
#include<fstream>

using namespace std;
int main()
{
    int T = 0;
    
    int N = 0;
    
    int sur = 0;
    
    int max = 0;
    
    int total = 0;
    
    int score[3];
    
    int nmax = 0;
    
    int count = 1;
    
    ifstream inFile("inp",ios::in);
    ofstream outFile("oup",ios::out);
        
    inFile >> T;
    
    while( T > 0)
    {
        inFile >> N;
        inFile >> sur;
        inFile >> max;
        nmax  = 0;
        while( N > 0)
        {            
            inFile >> total;
            
            if(total % 3 == 0)
            {
                if(total/3 >= max)
                {
                    if(sur > N-1)
                    {
                        sur--;
                    }
                    nmax++;
                }
                else
                {
                    if(total != 0)
                    {
                        if(total/3 + 1 >= max && sur > 0)
                        {
                            nmax++;
                            sur--;
                        }
                        else
                        {
                            if(sur > N-1)
                            {
                                sur--;
                            }
                        }
                    }   
                }
            }
            else if(total % 3 == 1)
                {
                    if(total/3 >= max ||total/3 + 1 >= max)
                    {                    
                        nmax++;
                    }                                
                }
                else if(total % 3 == 2)
                    {
                        if(total/3 >= max || total/3 + 1 >= max)
                        {                    
                            nmax++;
                            if(sur > N-1)
                            {
                                sur--;
                            }
                        } 
                        else
                        {
                            if(total/3 + 2 >= max && sur > 0)
                            {
                                nmax++;
                                sur--;
                            } 
                        }
                    }
            N--;
        }
        T--;
        outFile<<"Case #"<<count<<": "<<nmax<<endl;
        count++;
    }
}
   
