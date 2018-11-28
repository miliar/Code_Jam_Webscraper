#include<iostream>
#include<vector>
#include<queue>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int p=1;p<=t;p++){
        vector< vector<int> > li;
        int n;
        cin>>n;
        int c=0;
        for(int i=0;i<n;i++){
                int arr[2];
                cin>>arr[0]>>arr[1];
                
                for(int j=0;j<li.size();j++){
                         if((arr[0]<li[j][0] && arr[1]>li[j][1])||(arr[0]>li[j][0] && arr[1]<li[j][1]))
                                      c++;                            
                }
                vector<int> temp;
                temp.push_back(arr[0]);
                temp.push_back(arr[1]);
                li.push_back(temp);
                
        }
        cout<<"Case #"<<p<<": "<<c<<"\n";
    }
}
