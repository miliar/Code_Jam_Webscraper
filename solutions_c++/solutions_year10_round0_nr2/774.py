#include <iostream>
#include <vector>

using namespace std;

long int gcd(long int a, long int b)
{
        if(b == 0)
        {
                return a;
        }
        else
        {
                return gcd(b, a % b);
        }
}

int main(int argc, char *argv[])
{
    int T,N;
    int i,j;
    long int temp,val,min;
    vector <long int>t,g;
    
    cin>>T;
    for(i=0;i<T;i++)
    {
                    cin>>N;
                    t.clear();
                    
                    cin>>min;
                    t.push_back(min);
                    
                    for(j=1;j<N;j++)
                    {
                                    cin>>temp;
                                    t.push_back(temp);
                                    if(min > temp)
                                           min = temp;
                    }
                    t[0] -= min;
                    temp = t[0];
                    for(j=1;j<N;j++)
                    {
                                    t[j] -= min;
                                    temp = gcd(temp,t[j]);
                    }
                    
                    val = min%temp;
                    
                    cout<<"Case #"<<i+1<<": ";
                    (val==0)?cout<<"0":cout<<temp-val;
                    cout<<endl;
    }
}
