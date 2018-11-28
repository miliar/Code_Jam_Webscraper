#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int counter=0;
    while(t>0)
    {
        counter++;
        long long int n,i;
        cin>>n;
        vector <int> num(n);
        int k=0;
        long long int sum=0;
        int min=1000000;
        for(i=0;i<n;i++)
        {
                cin>>num[i];
                if(num[i]<min)
                                min=num[i];
                sum+=num[i];
                k=k^num[i];
        }
        if(k!=0)
                cout<< "Case #"<<counter<<": NO"<<endl;
        else
        {
                //sort(num.begin(),num.end());
                cout<<"Case #"<<counter<<": "<<sum-min<<endl;
        }
        t--;
        }
    }
        
        
