#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;
main(){
        int nt;
        cin>>nt;
        for(int g=1;g<=nt;g++){
                printf("Case #%d: ",g);
                int n;
                cin>>n;
                vector<pair<int,int> > A(n);
                for(int i=0;i<n;i++){
                        cin>>A[i].first>>A[i].second;
                }
                sort(A.begin(),A.end());
                int count=0;
                for(int i=0;i<n;i++){
                        for(int j=i+1;j<n;j++){
                                if(A[i].second>A[j].second)
                                        ++count;
                        }
                }
                cout<<count<<endl;
        }
}
