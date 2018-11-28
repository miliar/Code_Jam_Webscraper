#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t,k=1;
    cin >> t;
    while(t--)
    {
        int n,x=0;
        cin >> n ;
        vector <int> arr(n);
        long long int sum = 0 ;
        for(int i=0;i<n;i++)
        {
            cin >> arr[i];
            x = x ^ arr[i];
            sum +=arr[i] ;
        }
        if(x)
        {
             cout << "Case #"<<k++<<": NO"<< endl;
             continue;
        }
        sum-=*min_element(arr.begin(),arr.end());
        cout << "Case #"<<k++<<": "<<sum<<endl;
    }
}
