#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int t,n,i,j,k,l,ctr;
    int arr[1000];
        
    fstream fin,fout;
    fin.open("a.in",ios::in);
    fout.open("a.out",ios::out);
    
    fin >> t;
    for(i=0;i<t;i++)
    {
        fin>>n;
        ctr=0;
        for(j=0;j<n;j++)
        {
            fin>>arr[j];     
        }
        vector<int> vec (arr, arr+n);   
        vector<int> vec2 (arr, arr+n); 
        sort (vec.begin(), vec.end());
        for(j=0;j<n;j++)
        {
            //cout<<'/';
            
            if(find(vec.begin(), vec.end(),arr[j])-vec.begin()==find(vec2.begin(), vec2.end(),arr[j])-vec2.begin())
                ctr++;
        }
        fout<<"Case #"<<i+1<<": "<<(n-ctr)<<endl;
    }
    cout<<"Done";
    cin>>l;
    return 0;
}
