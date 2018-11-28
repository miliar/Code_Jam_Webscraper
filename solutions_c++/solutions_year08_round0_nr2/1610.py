#include<iostream>
#include<conio.h>
#include<algorithm>
#include<fstream>
using namespace std;
int convert(string &s){
    int hrs=(s[0]-48)*10+(s[1]-48);
    hrs=hrs*60;
    hrs+=(s[3]-48)*10+(s[4]-48);
}
class node{
      public:
            int start,end;char c;
            int index;bool mark;
      public:
             node(){}
             node(int a,int b,char d,int i):start(a),end(b),c(d),index(i),mark(1)
             {
             }
             bool operator<(const node &n)const{
                  return (start<n.start);
                  }
};
int main(){
    ifstream  din("B-large.in");
    ofstream dout("out1.txt");
    int nt;
    din>>nt;
    for(int g=1;g<=nt;g++){
            int offset,n,m,ans=0;
            din>>offset>>n>>m;
            string s;
            bool arr[n];bool brr[m];
            node a[n+m];string str1,str2;
            for(int i=0;i<n;i++){
                    din>>str1>>str2;
                    a[i]=node(convert(str1),convert(str2),'a',i);
                    arr[i]=1;
            }
            for(int i=0;i<m;i++){
                    din>>str1>>str2;
                    a[n+i]=node(convert(str1),convert(str2),'b',i);
                    brr[i]=1;
            }
            int count=n+m;int ans1=n,ans2=m;int ind=-1;
            sort(a,a+n+m);
            while(count!=0){
                            ind++;
                          
                            if(a[ind].c=='a'){
                                                count--;int indi=-1;
                                                a[ind].end+=offset;
                                                int temp=m+n-1;
                                                while(temp>ind){
                                                                if(a[temp].c=='b'){
                                                                if(a[temp].start>=a[ind].end&&brr[a[temp].index])
                                                                  indi=temp;
                                                                
                                                                }
                                                                  temp--;
                                                                
                                               }
                                                if(indi!=-1){
                                                ans2--;
                                                brr[a[indi].index]=0;                                                                             
                                              }
                                              
                            }
                              if(a[ind].c=='b'){
                                                count--;int indi=-1;
                                                a[ind].end+=offset;
                                                int temp=m+n-1;
                                                while(temp>ind){
                                                                if(a[temp].c=='a'){
                                                                if(a[temp].start>=a[ind].end&&arr[a[temp].index]){
                                                                indi=temp;
                                                                }
                                                                }
                                                                  temp--;
                                                                
                                               }
                                                if(indi!=-1){
                                                ans1--;
                                                arr[a[indi].index]=0;                                                                             
                                              }
                                              
                            }
              }
              dout<<"Case #"<<g<<": "<<ans1<<" "<<ans2<<endl;
//              cout<<"Case #"<<g<<": "<<ans1<<" "<<ans2<<endl;
              
    }           
return 0;
}
