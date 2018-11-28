#include<iostream>
using namespace std;

int main()
{
    int n, num=1;
    string input, x="welcom tdja", in, welcome="Xwelcome to code jam";
    string out;
    
    cin >>n;
    
    getline(cin, input);
    
    while(n--)
    {
        getline(cin, input);
        
        in="X";
        out="0000";
        
        for (int i=0;i<input.length();i++)
        {
            for (int j=0;j<x.length();j++)
                if(input[i]==x[j])
                {
                    in+=x[j];
                    break;
                }
        }
        
        int ar[20][in.length()];
        
        for (int i=0;i<20;i++)
        {
            for (int j=0;j<in.length();j++)
            {
                if (i==0)
                {
                    ar[i][j]=1;
                    continue;
                }
                
                if (j==0)
                {
                    ar[i][j]=0;
                    continue;
                }
                
                if (welcome[i]==in[j])
                    ar[i][j]=ar[i-1][j]+ar[i][j-1];
                else
                    ar[i][j]=ar[i][j-1];
                    
                ar[i][j]%=10000;
            }
        }
        
        int tmp=ar[19][in.length()-1];
        
        for (int i=3;i>=0;i--)
        {
            out[i]='0'+(tmp%10);
            tmp/=10;
        }
        
        printf("Case #%d: ", num++);
        cout <<out <<endl;
    }
    
    return 0;
}
