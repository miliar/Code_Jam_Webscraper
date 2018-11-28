#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int a;
    cin>>a;
    for(int q=0;q<a;q++)
    {
        int n,i,len=0;
        cin>>n;
        vector<int> s(n); 
        
        vector<int> arr(n);
        for(i=0;i<n;i++)
        {
                 cin>>s[i];
        }
        arr=s;
        sort(arr.begin(),arr.end());
        for(i=0;i<n;i++)
        {
                        if(arr[i]==s[i])
                           len++;
        }
        float p=(n-len);
        printf("Case #%d: %.6f\n",q+1,p);
    }
    return 0;
}                                                 
