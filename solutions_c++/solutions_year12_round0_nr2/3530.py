#include <cstdlib>
#include <iostream>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{

    int T;
    int t;
    int i;
    cin>>T;
    string translation;
   
    for(t=0;t<T;t++)
    {
        cin.ignore(256, '\n');
        int N;
        cin>>N;
        int S;
        cin>>S;
        int p;
        cin>>p;
        int result=0;
        int scores [N];
        for(int n=0;n<N;n++)
        {
                cin>>scores[n];
                if(scores[n] / 3 >= p || (scores[n]%3!=0 && scores[n]/3>=(p-1) && scores[n]!=0 ))
                {result++;}
                else if(29>scores[n] && scores[n]>1)
                {
                    if(scores[n]%3==0 && S>0 && scores[n]/3>=(p-1))
                    {
                         S--;
                         result++;
                    }
                    else if(scores[n]%3==2 && scores[n]/3>=(p-2) && S>0)  
                    {
                         S--;
                         result++;
                    }                   
                }         
        }
        
        cout<<"Case #"<<t+1<<": "<<result<<"\n";
    }        
    
    

    
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
