#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int T;
    cin>>T;
    
    for(int num = 1; num <= T; num++) {
        int N;
        vector<int> C;
        int total_sum = 0, total_xor = 0;
        int least = 1000001;
        int maximum = 0;
        
        cin>>N;
        for(int i=0;i<N;i++) {
            int value;
            cin>>value;
            C.push_back(value);
            if(value < least)
                least = value;
            total_sum = total_sum + value;
            total_xor = total_xor ^ value;
        }
        
        if(total_xor == 0) {
            maximum = total_sum - least;
        }
        
        cout<<"Case #"<<num<<": ";
        if(maximum != 0)
            cout<<maximum<<endl;
        else
            cout<<"NO"<<endl;
    }
    return 0;
}
