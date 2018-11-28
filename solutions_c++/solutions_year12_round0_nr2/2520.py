#include <iostream>
#include <vector>
using namespace std;
vector<int>googleers;

int main(void){
    int t,n,s,p,cnt=0;
    cin>>t;
    while(t--){
        googleers.clear();
        int c=0;
        cin>>n>>s>>p;
        int _n=n;
        while(_n--){
            int x;
            cin>>x;
            googleers.push_back(x);
        }
        for(int i=0;i<n;++i){
            int b=googleers[i]/3;
            if(googleers[i]%3==0){
                if(b>=p)c++;
                else if(s>0 && b>0 && b+1>=p){
                    c++;s--;
                }
            }else if(googleers[i]%3==1){
                if(b>=p || b+1>=p) c++;
                else if(s>0 && b+1>=p){
                    c++;s--;
                }
            }else if(googleers[i]%3==2){
                if(b+1 >=p || b>=p){
                    c++;
                }else if(s>0 && b+2>=p){
                    c++;s--;
                }
            }
        }
        cout<<"Case #"<<++cnt<<": "<<c<<" "<<endl;
    }
    return 0;
}
