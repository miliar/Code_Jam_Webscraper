#include<fstream>
#include<iostream>
using namespace std;
int q[100];
int dyn[10001][10001];
int p;
int n;
int sh(int a, int b) {
 //  cout<<"Tsekataan "<<a<<","<<b<<": "<<dyn[a][b]<<endl;
    if(dyn[a][b]>=0) return dyn[a][b];
    int ans=999999999;
    int temp=-1;
        if(b==a) return 0;
    for(int i=0;i<n;i++) {
        if(q[i]<a) {
        }
        else if(q[i]==a) {
            temp=b-a+sh(a+1,b);
            if(temp<ans) ans=temp;

        } else if(q[i]>a&&q[i]<b) {
     //       cout<<a<<","<<b<<": Katotaan "<<q[i]<<endl;
            temp=b-a+sh(a,q[i]-1)+sh(q[i]+1,b);
            if(temp<ans) ans=temp;

        } else if(q[i]==b) {
            temp=b-a+sh(a,b-1);
            if(temp<ans) ans=temp;

        } else {
            if(temp==-1) {
                dyn[a][b]=0;
                return 0;
            }
            dyn[a][b]=ans;
            return ans;
        }

    }
    if(temp==-1) {
        dyn[a][b]=0;
        return 0;
    }
    dyn[a][b]=ans;
    return ans;

}


int main() {
    int tim;
    ifstream fin("cinput.txt");

    fin>>tim;

    for(int i=0;i<tim;i++) {
        fin>>p>>n;
        for(int j=0;j<=p;j++) for(int k=0;k<=p;k++) dyn[j][k]=-1;
        for(int j=0;j<n;j++) fin>>q[j];
        cout<<"Case #"<<(i+1)<<": "<<sh(1,p)<<endl;
    }


}
