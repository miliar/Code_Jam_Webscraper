# include <iostream>
# include <vector>

using namespace std;

int main ()
{
    int test;
    cin>>test;
    for (int testid = 1;testid <=test;testid++)
    {
        int num;
        cin>>num;
        int temp;
        int ans = 0;
        int min = 1000001;
        int xorresult = 0;
        for (int i = 0;i < num;i++)
        {
            cin>>temp;
            if (min > temp)
               min = temp;
            ans+=temp;
            xorresult = xorresult ^ temp;    
        }    
        if (xorresult == 0)
        {
           ans = ans - min;
           cout<<"Case #"<<testid<<": "<<ans<<endl;
        }   
        else
           cout<<"Case #"<<testid<<": NO"<<endl; 
    }
    return 0;
}           
        
