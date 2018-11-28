#include<iostream>
#include<algorithm>

using namespace std;
int N,T,mat[45],mats[45],swapc;

void swap(int i,int j) {
//    cout<<i<<":"<<j<<endl;
    int t=mat[i];
    mat[i]=mat[j];
    mat[j]=t;
    swapc++;
}

int main() {
    cin>>T;
    for(int t=1;t<=T;t++) {
        cin>>N;
        swapc=0;
        for(int i=0;i<N;i++) {
            mat[i]=0;
            for(int j=0;j<N;j++) {
                char ch;
                cin>>ch;
                if(ch=='1') mat[i]=j;
            }
            mats[i]=mat[i];
        }
        sort(mats,mats+N);
        for(int i=0;i<N;i++) {
            int j;
            if(mat[i]<=i) continue;
            for(j=i;mat[j]>i&&j<N;j++) ;
            if(j==N) {
                cerr<<"bad"<<t<<"\n";
//                for(j=i;j>mat[i];j--) swap(j,j-1);
            }
            for(;j>i;j--) swap(j,j-1);
//            if(mat[i]!=mats[i]) {
//                bool swapped=false;
//                for(int j=mat[i];j<N;j++)
//                    if(mat[j]==mats[i]) {
//                        swap(i,j);
//                        swapped=true;
//                        break;
//                    }
//                if(swapped==false) {
//                    for(int j=mat[i]-1;j>i;j--)
//                        if(mat[j]==mats[i]) {
//                            swap(i,j);
//                            swapped=true;
//                            break;
//                        }
//                }
//            }
        }
        cout<<"Case #"<<t<<": ";
        cout<<swapc<<"\n";
    }
    return 0;
}
