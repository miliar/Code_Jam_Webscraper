#include <iostream>
#include<algorithm>
using namespace std;
int main(int argc, char **argv)
{
	int t,m,x,s,n,c;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>n;
        m=10000000;
        s=0;
        x=0;
        while(n--){
            cin>>c;
            m=min(m,c);
            x^=c;
            s+=c;
        }
        cout<<"Case #"<<i<<": ";
        if(x){
            cout<<"NO\n";
        }else{
            cout<<s-m<<"\n";
        }
    }
	return 0;
}

