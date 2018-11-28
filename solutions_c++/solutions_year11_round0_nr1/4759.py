#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    int t,i,j,n;
    long long k,kk;
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    fin>>t;//cout<<t;
    #define cin fin
    #define cout fout

    int iO=1,iB=1,ic,prev=0;char prevc;
    long long s=0;
    for(i=0;i<t;++i)
    {
        cin>>n;s=0;iO=1;iB=1;prev=0;prevc='C';
        for(j=0;j<n;++j)
        {
            char c;
            cin>>c>>kk;

            if(c=='O'){ic=iO;iO=kk;}else{ic=iB;iB=kk;}

            k=ic-kk;//cout<<" "<<ic<<" ";ic=kk;
            if(k<0)k=-k;

            if(c==prevc)
            {
                prev+=k+1;
            }else{k-=prev;/*cout<<prev<<"z"<<k<<"x";*/if(k<0)k=0;prev=k+1;}
            s+=k+1;
            //cout<<k+1<<" ";
            prevc=c;
        }
        cout<<"Case #"<<i+1<<": "<<s<<endl;
    }fin.close();fout.close();
    return 0;
}
