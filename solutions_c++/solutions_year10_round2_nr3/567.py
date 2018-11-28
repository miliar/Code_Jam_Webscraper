#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;
int gg=0;
bool testall[30];


int N=25;
void read() {
	cin>>N;
    testall[0]=false;
    testall[1]=false;
    testall[N]=true;
}

void go() {
    vector<int> z;
    for(int i=0;i<30;i++) if(testall[i]) z.push_back(i);
    int cur=N;
            //cout<<"Koklataa ";
//            for(int i=0;i<z.size();i++) cout<<z[i]<<" ";
  //          cout<<endl;
    while(true) {
        if(cur==1) {
    //        for(int i=0;i<z.size();i++) cout<<z[i]<<" ";
       //     cout<<endl;
            gg++;
            if(gg>=100003) gg%=100003;
            return;
        }
        bool d=false;
        for(int i=0;i<z.size();i++) {
            if(z[i]==cur) {
            	int pr=cur;
                cur=i+1;
                if(cur==pr) return;
                d=true;
            }
        }
        if(!d) return;
    }
}

void rec(int a) {
    if(a==N) {
        go();
    } else {
        testall[a]=false;
        rec(a+1);
        testall[a]=true;
        rec(a+1);
    }
}

void solve() {
    rec(2);   
}

void write() {
    cout<<gg<<endl;

}


int main() {
    read();
    solve();
    write();
}
