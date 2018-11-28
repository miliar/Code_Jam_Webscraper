#include <iostream>
#include <stdio.h>
#include <vector>
#include <windows.h>
#include <conio.h>

using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)

typedef vector<int> vi;

int main() {
    freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);

    int tcnr=0;
    cin>>tcnr;

    rep(nr,tcnr){

        int googlers=0, cheat=0, pNum=0, res=0;

        cin>>googlers>>cheat>>pNum;

        int defCheat=cheat;
        int values[googlers];
        rep(i,googlers)
            cin>>values[i];

        int hatarValue = 3*(pNum-1);
        int minValue = 3*(pNum-2)+1;
        if(pNum==1)
            minValue=0;

        rep(i,googlers){
            if(values[i]>hatarValue)
                res++;
            else
                if(values[i]>minValue && cheat>0)
                {
                    res++;
                    cheat--;
                }
        }

        cout<<"Case #"<<(nr+1)<<": "<<res; // <<"  "<<hatarValue<<"..."<<minValue<<" dancers:"<<googlers<<" cheat:"<<defCheat<<" p:"<<pNum<<endl;
//        rep(i,googlers)
//            cout<<"   values:"<<values[i]<<", "<<endl;
        if(nr<tcnr-1)
            cout<<endl;

    }
}
