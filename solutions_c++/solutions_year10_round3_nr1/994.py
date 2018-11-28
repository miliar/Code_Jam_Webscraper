#include<iostream>
#include<vector>
using namespace std;

int main(){
    freopen("A-large.in","rt",stdin);
    freopen("output.out","wt",stdout);
    int T;
    cin>>T;
    for (int i=0 ; i<T ; i++){
        int N;
        cin>>N;
        int res=0;
        vector<pair<int,int> > pairs;
        for (int j=0 ; j<N ; j++){
            int A,B;
            cin>>A>>B;
            
            pairs.push_back(make_pair(A,B));
        }
        for (int j=0 ; j<N ; j++){
            for (int k=j+1 ; k<N ; k++)
                if (pairs[j].first < pairs[k].first && pairs[j].second > pairs[k].second)res++;
                else if (pairs[j].first > pairs[k].first && pairs[j].second < pairs[k].second)res++;
        }
        cout<<"Case #"<<i+1<<": "<<res<<endl;
    }
    //system("pause");
    return 0;
}
