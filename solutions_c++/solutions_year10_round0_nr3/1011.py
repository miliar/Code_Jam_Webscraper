#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cmath>

using namespace std;

const int maxn=1001;

ifstream fin("C-large.in");
ofstream fout("C-large.out");
int n,N,r,k;
int q[maxn],qnext[maxn],qnum[maxn];

int main()
{
    fin>>N;
    int tmp=N;
    long long res,tmp1,tmp2;
    while (N!=0){
        fin>>r>>k>>n;
        N--;tmp1=0;
        for (int i=0;i<n;i++) {fin>>q[i];tmp1+=q[i];}
        if (tmp1<=k) res=tmp1*r;
        else{
            for (int i=0;i<n;i++) {
                tmp1=0;
                tmp2=i;
                while (tmp1+q[tmp2]<=k)
                 {tmp1+=q[tmp2];tmp2=(tmp2+1)%n;}
                qnext[i]=tmp2;
                qnum[i]=tmp1;
            }
            tmp1=0;res=0;
            for (int i=0;i<r;i++){
                res+=qnum[tmp1];
                tmp1=qnext[tmp1];
            }
        }
        fout<<"Case #"<<tmp-N<<": "<<res<<endl;
    }
    return 0;
}
