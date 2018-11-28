#include<iostream>
using namespace std;
int main() {
    int i,j,T,N,t;
    int pos,time;
    int lastPos[100],lastTime[100];
    int lastGlobalTime;
    char c;
    cin>>T;
    for(i=0;i<T;i++) {
                      cin>>N;
                      lastGlobalTime=0;
                      lastPos['O']=lastPos['B']=1;
                      lastTime['O']=lastTime['B']=0;
                      for(j=0;j<N;j++) {
                                        cin>>c>>pos;
                                        t=lastPos[c]-pos;
                                        t=t<0?-t:t;
                                        //cout<<t<<endl;
                                        t+=lastTime[c]+1;
                                        time=(t>lastGlobalTime)?t:(lastGlobalTime+1);
                                        lastGlobalTime=time;
                                        lastPos[c]=pos;
                                        lastTime[c]=time;
                                        //cout<<c<<" "<<pos<<" "<<time<<endl;
                      }
                      cout<<"Case #"<<i+1<<": "<<time<<endl;
                     }
    return 0;
}
