
#include <iostream>

using namespace std;
int T, N;
char bot;

int pos;


int main() {
    cin>>T;
    for (int t=1; t<=T; t++) {  
        cin>>N;
        int ltb = 0;
        int lto = 0;
        int time = 0;
        int lb = 1;
        int lo = 1;
        
        int delta = 0;
        for (int n=0; n<N; n++) {
            cin >> bot;
            cin >> pos;
            
            if (bot == 'B') {
                delta = abs(pos - lb);
                if (delta > time - ltb)
                    time = delta+ltb;
                time+=1;
                ltb = time;
                lb = pos;
                //cout << 'B' << pos << " " << time;
            }
            else {
               delta = abs(pos - lo);
             
                if (delta+lto > time)
                    time = delta+lto;
                time+=1;
                lto = time;
                lo = pos;
                //cout << 'O' << pos << " " << time;   
            }
        }
        //cout << endl;
        
        
        cout<<"Case #"<<t<<": "<<time<<endl;     
    }
  
    
  return 0;

}


