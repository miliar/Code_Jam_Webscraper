#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

#define pb push_back

int main() {
    int a,b,c,p,count;
    ifstream fin;
    ofstream fout;
    fin.open("in.txt");
    fout.open("out.txt");
    bool prime[1001];
    prime[0]=false;
    prime[1]=false;    
    for(int i=2;i<=1000;i++)
        prime[i]=true;
    for(int i=2;i<=1000;i++)
        if(prime[i]) 
            for(int j=2;i*j<=1000;j++) 
                prime[i*j]=false;
    fin>>c;
    for(int i=1;i<=c;i++) {
        cout<<i<<"-----\n";
        fin>>a>>b>>p;
        int n=b-a+1;
        vector <int> set(n);
        for(int j=0;j<n;j++)
            set[j]=j;
        count=n;
        for(int j=a;j<b;j++) 
            for(int k=j+1;k<=b;k++) 
                for(int l=p;l<=j;l++)  {
                    if(prime[l] &&  j%l==0 && k%l==0) {
                        int t1=set[k-a],t2=set[j-a];
                        for(int m=0;m<n;m++) {
                            if(set[m]==t1 || set[m]==t2)
                                set[m]=count;
                        }                        
                        count++;
                    }
                }
        
        int ret=0;
        for(int j=0;j<n;j++) {
            cout<<set[j]<<"\n";
            bool count=false;
            for(int k=0;k<j;k++) {
                if(set[j]==set[k]) {
                    count=true;
                    break;
                }
            }
            if(!count)
                ret++;
        }
        cout<<"\n\n";
        fout<<"Case #"<<i<<": "<<ret<<"\n";
    }
    system("pause");
    fout.close();
}
