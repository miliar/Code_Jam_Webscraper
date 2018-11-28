#include <iostream>
#include <fstream>
#include <vector>

#pragma optimize("O2",on)
#pragma comment(linker, "/STACK:167772160")
using namespace std;

class Summator {
	vector <long> s;
    long prev(long number) {return number & (number-1);};
    long next(long number) {return (number<<1)-(number & (number-1));};
public:
    Summator(long size) {
        s.resize(size+1);
	    for (int i=0;i<size+1;i++)	s[i]=0;
    };
    void change(long position, long value) {
	    long curent_position=position;
	    while (curent_position<s.size()){
		    s[curent_position]+=value;
		    curent_position=next(curent_position);
	    }
    };
    long findsum(long left, long right) {
	    long curent_position=right;
	    long result=0;
	    while (curent_position>0) {
		    result+=s[curent_position];
		    curent_position=prev(curent_position);
	    }
	    //curent_position=left-1;
	    //while (curent_position>0) {
		   // result-=s[curent_position];
		   // curent_position=prev(curent_position);
	    //}
	    return result;
    };
};

int a[1000100];

int main() {
#ifndef ONLINE_JUDGE
	ifstream cin("C-large.in");
    ofstream fout("C-large.out");
#endif
    int T; cin>>T;
    for (int o=1; o<=T; o++) {
        cout<<o<<endl;
        memset(a,0,sizeof a);
        int n,t,pos=0; cin>>n; 
        Summator s(n);
        for (int i=1; i<=n; i++)
            s.change(i,1);
        for (int num=1; num<=n; num++) {
            int k=(s.findsum(1,pos)+num)%(n-num+1);
            if (k==0) k=n-num+1;
            int l=1,r=n,x;
            while (l+1<r) {
                x=(l+r)/2;
                int t=s.findsum(1,x);
                if (s.findsum(1,x)>=k) r=x; else l=x;
            }
            if (s.findsum(1,l)==k) x=l; else x=r;
            a[x]=num; s.change(x,-1); pos=x;
        }
        int k; cin>>k;        
        fout<<"Case #"<<o<<": ";
        for (int i=0; i<k; i++) {
            cin>>t; fout<<a[t]<<" ";
        }
        fout<<endl;
    }
	return 0;
}