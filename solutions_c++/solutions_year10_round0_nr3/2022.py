#include<iostream>
#include<string.h>
#include<vector>
#include<math.h>
#include<limits.h>
using namespace std;




class Roller 
{
    public:
    long long int solve(long long int r, long long int k, long long int n);

};

//R times a day
//K people at once
//N groups
long long int Roller::solve(long long int r, long long int k, long long int n)
{
    vector<long long int> g;
    long long int temp = 0;
    for(long long int i=0;i<n;i++)
    {
        cin>>temp;
        g.push_back(temp);
    }

    vector<long long int> sumGroup(n,0);
    vector<long long int> endGroup(n,0);
    for(long long int i=0;i<n;i++)
    {
       long long int sum = g[i];
       long long int j = i;
       while(1)
       {
         if((j+1)%n == i)
            break;
         if((sum+g[(j+1)%n])>k) 
            break;
          else
            sum+=g[(j+1)%n];

        j=(j+1)%n;
       }
       endGroup[i] = j;
       sumGroup[i] = sum;
    }

    long long int p= 0;long long int total = 0;
    long long int rounds = 0;

    while(rounds<r)
    {
//        cout<<"round "<<rounds<<" adding "<<sumGroup[p]<<endl;
        total = total + sumGroup[p];
        p = (endGroup[p]+1)%n;
        rounds++;
    }
    return total;

}

int main()
{

    Roller roller;
//    string ans = sn.solve(1,0);
//    cout<<"the ans is "<<ans;
    long long int t,r,n,k;
    cin>>t;
    for(long long int i=0;i<t;i++)
    {
        cin>>r; cin>>k; cin>>n;
        cout<<"Case #"<<(i+1)<<": "<<roller.solve(r,k,n)<<endl;
    }

}


