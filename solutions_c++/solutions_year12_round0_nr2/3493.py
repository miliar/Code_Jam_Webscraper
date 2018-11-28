#include<iostream>
using namespace std;
#include<cstring>
#include<vector>

int main(){
    int t,cases=1;
    cin>>t;
    
    while(t--){int n,s,p,k=0,inp;
                   cin>>n>>s>>p;
                   int a[n];
                   for(int i=0;i<n;i++) {cin>>inp;a[i]=inp;}
              /*process*/
              int min=3*p-2;if(p==0) min=0;
              int min_s=3*p-4;if(p==1) min_s=2;
              vector<int> v;
              for(int i=0;i<n;i++) { if(a[i]>=min) k++;
                                     else  if(a[i]<min && a[i]>=min_s ) v.push_back(a[i]);
                                   }
               if(s<v.size()) k+=s;
               else k+=(v.size());
               cout<<"Case #"<<cases++<<": ";
               cout<<k<<endl;
               }
               //system("pause");
    return 0;
}
