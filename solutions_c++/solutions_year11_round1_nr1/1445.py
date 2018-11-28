#include <iostream>

//#define min(a,b) ((a<=b)?a:b)

using namespace std;

int main()
{

    int T;
    long long N;
    int Pd, Pg;
    bool cut;

    cin>>T;
    
    for (int i=0; i<T; i++) {
        cin>>N>>Pd>>Pg;
        
        cout<<"Case #"<<i+1<<": ";
        
        if (Pg == 100) {
            if (Pd < 100) cout<<"Broken"<<endl;
            else cout<<"Possible"<<endl;
        }
        else if (Pg == 0) {
            if (Pd > 0) cout<<"Broken"<<endl;
            else cout<<"Possible"<<endl;
        }
        else {
            if (N >= 100) cout<<"Possible"<<endl;
            else {
                cut = false;
                for (int j=1; j<=N && !cut; j++) {
                    if ((j*Pd)%100 == 0) {
                        cut = true;
                        cout<<"Possible"<<endl;
                    }
                }
                if (!cut) cout<<"Broken"<<endl;
            }
        }
    }

    return 0;

}
