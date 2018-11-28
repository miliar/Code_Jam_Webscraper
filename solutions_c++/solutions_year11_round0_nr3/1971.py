#include<iostream>
#include<vector>


using namespace std;


int main(){
    int cases;
    cin>>cases;
    for(int cas=1;cas<=cases;cas++){
        int n;
        cin>>n;
        vector<int> candy;

        int x=0;
        int m = 10000000;
        int sum=0;
        for(int i=0;i<n;i++){
            int c;
            cin>>c;
            candy.push_back(c);
            x^=c;
            sum+=c;
            m = min(m,c);
        }
        if(x!=0){
            cout<<"Case #"<<cas<<": NO\n";
        }else{
            cout<<"Case #"<<cas<<": "<<(sum-m)<<"\n";
        }

    }
}
