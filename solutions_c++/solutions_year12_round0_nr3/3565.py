
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int t;
int main ()
{
    freopen("C-small-attempt0.in","r",stdin);   
    freopen("C-small-attempt0.out","w",stdout);
    cin>>t;
    for (int trial = 1; trial<=t; trial++)
    {
        cout<<"Case #"<<trial<<": ";
        int a, b;
        cin>>a>>b;
        
        long long ans = 0;
        
        for (int n=a;n<b;++n)
        {
            //We'll 'recycle' at every possible digit of n and see if the answer is BETWEEN N AND B (inclusive of B, exclusive of N)
            int digit = 1;//Start at the first digit
            int toPowerDigit = 1;
            while (toPowerDigit < n)
            {
             //Get all the digits up till the digitth digit
             int index = 1;
             int backNum = 0;
             int modder = 10;
             int temp  = n;             
             while (index<=digit)     
             {
                   backNum += (temp%modder);
                   modder = modder*10;
                   index++;
                   temp = temp - backNum;
             }     
             
             int frontNum = (n-backNum)/(modder/10);
            //cout<<n<<" "<<frontNum<<" "<<backNum<<"\n";
            //int TEMP = modder;
             modder = 1;
             while (modder<=frontNum)
                   modder = modder * 10;
                   
             int newNum = frontNum + modder * backNum;
             
             if (n<newNum & newNum<=b)
             {
                //cout<<n<<" "<<newNum<<" "<<frontNum<<" "<<backNum<<" "<<TEMP<<"\n";
                ans++;
             }
             toPowerDigit = toPowerDigit * 10;
             digit++;      
            }
            
        }
        cout<<ans<<"\n";    
    }
    return 0;   
}
