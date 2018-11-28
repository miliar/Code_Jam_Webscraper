# include<iostream>
# include<vector>
# include<math.h>

using namespace  std;

int main()
{
    int a,b,c,n,k,j;
    vector<int> arr;
    cin>>a;
    c=a;
    while(a--)
    {
              cin>>n;
             cin>>k;
             b=(int)pow (2,n);
             j=(k+1)%b;
             if(j==0)
             cout<<"Case #"<<c-a<<": ON\n";
             else
             cout<<"Case #"<<c-a<<": OFF\n";
    }
    return 0;
}
