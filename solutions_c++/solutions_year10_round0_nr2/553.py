#include<iostream>
#include<string>
using namespace std;
const int Maxn=1000+10;
const int Maxk=50+1;
typedef long long LL;
string a[Maxn],b[Maxn];
int N;
bool biger(string a,string b){
     if (a.size()>b.size()) return true;
     if (a.size()<b.size()) return false;
     for (int i=0;i<a.size();i++)
     if (a[i]>b[i]) return true;else
     if (a[i]<b[i]) return false;
     return false;
}
string cha(string a,string b){
     string x=a;
     string y=b;
     if (biger(y,x)) {
            string tmp;
            tmp=x;
            x=y;
            y=tmp;
     }
     int left=0;
     while (y.size()<x.size()) y="0"+y;
     for (int i=y.size()-1;i>=0;i--){
         if (x[i]-y[i]-left>=0) x[i]=x[i]-y[i]-left+'0',left=0;else{
                x[i]=10+x[i]-y[i]-left+'0';
                left=1;
         }
     }
     while (x.size()>1 && x[0]=='0') x.erase(0,1);
     return x;
}
string Mod(string a,string b){
       while (biger(a,b) || a==b){
             string s="";
             for (int i=0;i<b.size();i++)
             s=s+a[i];
             int i;
             if (biger(s,b) || s==a) i=b.size();else i=b.size()+1,s=s+a[i-1];
             while (i--) a.erase(0,1);
             while (biger(s,b) || s==b)
             s=cha(s,b);
             a=s+a;
             while (a.size()>1 && a[0]=='0') a.erase(0,1);
       }
       return a;
}
string gcd(string a,string b){
       if (a=="0") return b;
       if (b=="0") return a;
       return gcd(b,Mod(a,b));
}
int main(){
freopen("1.in","r",stdin);
freopen("1.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int i=1;i<=T;i++){
        printf("Case #%d: ", i);
        scanf("%d ", &N);
        for (int j=1;j<=N;j++) cin>>a[j];
        for (int j=1;j<N;j++) 
        b[j]=cha(a[j+1],a[j]);
        for (int j=N-1;j>1;j--) b[j-1]=gcd(b[j],b[j-1]);
        a[1]=Mod(a[1],b[1]);
        string Ans;
        if (a[1]!="0") Ans=cha(b[1],a[1]);else
        Ans="0";
        cout<<Ans<<endl;
    }
    return 0;
}
