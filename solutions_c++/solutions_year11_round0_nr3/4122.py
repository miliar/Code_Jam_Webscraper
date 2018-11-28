#include<iostream>
using namespace std;
long long ans,n;
long long num[1500];
void DFS( long long sum1,long long sum2 ,long long w ,long long sum3 ,long long sum4){
    long long a=sum1^num[w];
    long long a1=sum3+num[w];
    long long b=sum2^num[w];
    long long b1=sum4-num[w];
    if(a==b){
        if(a1 >= b1 && b1< ans && b1!=0)
           ans=b1;
        else if(a1<b1 && a1<ans && a1!=0)
            ans=a1;
        return;
    }
    for(int i=w+1; i<n; ++i){
        DFS(a,b,i,a1,b1);
    }
}
int main(){
    freopen("C-large (1).in","r",stdin);
    freopen("C-large (1).out","w",stdout);

    int t;
    cin >> t;
    for(int k=1; k<=t; ++k ){ 
        cin >> n;
        long long sum=0;
        long long uu=0;
        for(int i=0; i<n; ++i){
            cin >> num[i];
            sum^=num[i];
            uu+=num[i];
        }
        if(sum){
            cout << "Case #" << k << ": ";
            cout << "NO" << endl;
            continue;
        }
        ans=INT_MAX;
        sort(num,num+n);
        for(int i=0; i<n; ++i ){
            DFS(sum,0,i,0,uu);
        }
        cout << "Case #" << k << ": ";
        if(ans==INT_MAX) cout << "NO" << endl;
        else cout << uu-ans << endl;
    }
    return 0;
}
