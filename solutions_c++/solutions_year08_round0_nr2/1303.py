#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int chtoint(string s)
{
    int t=0;
    t+=s[4]-'0';
    t+=(s[3]-'0')*10;
    int tt = 0;
    tt+=s[1]-'0';
    tt+=(s[0]-'0')*10;
    t+=tt*60;
    return t;
}

void rsort(int a1[], int a2[], int a3[], int len)
{
    for (int i = 0; i < len; i++) {
       for(int j = 0; j < len - 1; j++) {
           if(a1[j] > a1[j+1]) {
               int x = a1[j];
               a1[j] = a1[j+1];
               a1[j+1] = x;
               x = a2[j];
               a2[j]=a2[j+1];
               a2[j+1]=x;
               x=a3[j];
               a3[j]=a3[j+1];
               a3[j+1]=x;
           }
       }
    }
    return;
}

int main()
{
//    ifstream cin("in1.in");
 //   ifstream cin("B-small-attempt0.in");
  ifstream cin("B-large.in");
    
    ofstream cout("out.txt");
    
    int n;
    cin>>n;
    for(int u=1;u<=n;u++){
       int t;
       cin>>t;
       int na,nb;
       cin>>na>>nb;
       int a1[102];
       int a2[102];
       int a3[102];
       int b1[102];
       int b2[102];
       int b3[102];
       string s1, s2;

       for (int i=0;i<na;i++) {
          cin>>s1>>s2;
          a1[i] = chtoint(s1);
          a2[i] = chtoint(s2);
          a3[i]=0;
       }
       for(int i=0;i<nb;i++){
          cin>>s1>>s2;
          b1[i]=chtoint(s1);
          b2[i]=chtoint(s2);
          b3[i]=0;
       }

       int ra=0;
       int rb=0;

       rsort(a1, a2, a3, na);
       rsort(b1, b2, b3, nb);

       int ap = 0;
       int bp = 0;
       while(ap<na||bp<nb){
          if(bp >= nb || (ap < na && a1[ap] < b1[bp])) {
             int time = a2[ap];
             time += t;
             for(int i=0;i<nb;i++){
                if(b1[i]>=time){
                   b3[i]++;
                   break;
                }
             }
             int f=0;
             for(int i=0;i<=ap;i++){
                if(a3[i]>0){
                   f=1;
                   a3[i]--;
                   break;
                }
             }
             if(f==0)
               ra++;
             ap++;
          }else {
             int time=b2[bp];
             time+=t;
             for(int i=0;i<na;i++){
                if(a1[i]>=time){
                   a3[i]++;
                   break;
                }
             }
             int f=0;
             for(int i=0;i<=bp;i++){
                if(b3[i]>0){
                   f=1;
                   b3[i]--;
                   break;
                }
             }
             if(f==0)
                rb++;
             bp++;
          }
       }
       cout<<"Case #"<<u<<": "<<ra<<" "<<rb<<endl;
    } 
}
