#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int C,n,k,b,t;
    cin >> C;
    for(int ww =1; ww <=C;ww++){
        cout << "Case #"<<ww<< ": ";
        
        cin >> n >> k >> b >>t;
        vector<int>x,v;
        for(int i =0;i<n;i++){
            int temp;
            cin >>temp;
            x.push_back(temp);
        }
        for(int i =0;i<n;i++)
        {
            int temp;
            cin >>temp;
            v.push_back(temp);
        }
/*        int i=0;
        while(i<x.size()){
            if(x[i]+v[i]*t<b){
                x.erase(x.begin()+i);
                v.erase(v.begin()+i);
            }
            else i++;
        }
        if(x.size()<k){*/
        long long get = 0,ans=0;
        for(int i =n-1;i>=0;i--)
        {
            if(get == k)break;
            if(x[i]+v[i]*t<b){
                ans+=k-get;
            }
            else get++;
        }
        if(get <k)cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
}

            
        
