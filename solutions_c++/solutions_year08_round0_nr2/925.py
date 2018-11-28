#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

#define PII pair<int,int> 

int main(){
    int ncases;
    cin >> ncases;
    for(int x=1;x<=ncases;x++){
        int t,na,nb;
        vector<PII> trainsa,trainsb;
        vector<PII> av1,av2;
        cin >> t >> na >> nb;
        int buf1,buf2;
        for(int i=0;i<na;i++){
            cin >> buf1;
            cin.ignore();
            cin >> buf2;
            trainsa.push_back(PII (buf1,buf2));
            cin >> buf1;
            cin.ignore();
            cin >> buf2;
            buf1 += (buf2+t)/60;
            buf2 = (buf2+t)%60;
            av2.push_back(PII (buf1,buf2));
        }
        for(int i=0;i<nb;i++){
            cin >> buf1;
            cin.ignore();
            cin >> buf2;
            trainsb.push_back(PII (buf1,buf2));
            cin >> buf1;
            cin.ignore();
            cin >> buf2;
            buf1 += (buf2+t)/60;
            buf2 = (buf2+t)%60;
            av1.push_back(PII (buf1,buf2));
        }
        //system("pause");
        sort(trainsa.begin(),trainsa.end());
        sort(trainsb.begin(),trainsb.end());
        sort(av1.begin(),av1.end());
        sort(av2.begin(),av2.end());
        int need1=0,need2=0;
        int act1=0,act2=0;
        for(int i=0;i<24;i++){
            for(int j=0;j<60;j++){
                if(!av1.empty()) while(av1[0]==PII(i,j)){
                    //cout << " Time: " << i << ":" << j << "; Train arrived at A" << endl;
                    act1++;
                    av1.erase(av1.begin());
                    if(av1.empty()) break;
                }
                if(!av2.empty()) while(av2[0]==PII(i,j)){
                    //cout << " Time: " << i << ":" << j << "; Train arrived at B" << endl;
                    act2++;
                    av2.erase(av2.begin());
                    if(av2.empty()) break;
                }
                if(trainsa.size()>0) while(trainsa[0]==PII (i,j)){
                    //cout << " Time: " << i << ":" << j << "; Train from A, act: " << act1 << endl;
                    act1--;
                    if(act1==-1){
                        act1=0;
                        need1++;
                    }
                    trainsa.erase(trainsa.begin());
                    if(trainsa.size()==0) break;
                }
                if(trainsb.size()>0) while(trainsb[0]==PII (i,j)){
                    //cout << " Time: " << i << ":" << j << "; Train from B, act: " << act2 << endl;
                    act2--;
                    if(act2==-1){
                        act2=0;
                        need2++;
                    }
                    trainsb.erase(trainsb.begin());
                    if(trainsb.size()==0) break;
                }
            }
        }
        cout << "Case #" << x << ": " << need1 << " " << need2 << endl;
    }
}
