#include<iostream>
#include<cmath>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
    ifstream in;
    in.open("input.txt");
    ofstream out;
    out.open("output.txt");
    int t;
    char c[100];
    in>>t;
    for(int prob=0;prob<t;prob++)
    {
            in>>c;
            cout<<c<<endl;
            int len=strlen(c);
            char t[100];
            int count=0,signal=0;
            for(int i=0;i<len;i++)
            {
                    signal=0;
                    for(int j=0;j<count;j++)
                    {
                            if(c[i]==t[j])
                            {signal=1;break;}
                    }
                    if(signal==0)
                    {t[count]=c[i];count++;}
            }
            //cout<<count<<endl;
            long long unsigned int n=0;
            if(count>1){
            char temp=t[0];
            t[0]=t[1];
            t[1]=temp;
            
            for(int i=0;i<len;i++)
            {
                         
                         for(int j=0;j<count;j++)
                         {
                                 if(c[i]==t[j])
                                 n=n+j*(long long unsigned int)(pow((double)count,(double)(len-1-i)));
                         }
                    
            }}
            else
            {
                if(prob==9)
                cout<<"hii"<<endl;
                for(int i=0;i<len;i++)
                n=n+(long long unsigned int)(pow(2.0,(double)(len-1-i)));
            }
            
            
            
            cout<<"Case #"<<prob+1<<": "<<n<<endl;
            out<<"Case #"<<prob+1<<": "<<n<<endl;
    }
    
    in.close();
    out.close();
    system("pause");
    return 0;
}
