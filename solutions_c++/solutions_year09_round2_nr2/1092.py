#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<fstream>
using namespace std;
string swapchar(string,int,int);
string dosort(string,int);
int main(){
 int i,j,k,n,pos,flag,total=0,count=0;
 char ch,small,current;
 char input[101];
ifstream instream("/home/condor/GCJ/large.in");
ofstream outstream("/home/condor/GCJ/large.out");
instream.getline(input,100);
	for(int i=0;input[i];++i)
		total = total*10 + (input[i]-'0');
 while(count<total){
  asdfsdf:
  count++;
  string s="";
  instream.getline(input,100);
 for(int b=0;input[b];++b) s+=(char)input[b];
  n=s.size()-1;
  if(n==0){
   s=s+'0';
   goto x;
  }
  if(s[n]>s[n-1])
  {
   s=swapchar(s,n,n-1);
   goto x;
  }
  flag=1;
  for(i=0;i<=n;i++){
   if(s[i]<s[i+1]){
    flag=0;
    break;
   }
  }
  if(flag){
   sort(s.begin(),s.end());
   for(i=0;i<=n;i++){
    if(s[i]!='0')
     break;
   }
   s='0'+s;
   s=swapchar(s,0,i+1);
   goto x;
   
  }
 
  for(i=n;i>0;i--){
   if(s[i]>s[i-1]){
    small=s[i-1];
    k=s[i];
    pos=i;
    for(j=i;j<=n;j++){
     if(s[j]>small&&s[j]<=k){
      k=s[j];
      pos=j;
     }
    }
    s=swapchar(s,i-1,pos);
    break;
   }
  } 
  s=dosort(s,i);
  x:
   outstream<<"Case #"<<count<<": "<<s<<endl;  
 }
 return 0;
}    
string swapchar(string s,int p,int q){
 char ch;
 ch=s[p];
 s[p]=s[q];
 s[q]=ch;
 return s;
}
string dosort(string s,int pos){
 int i,j,n=s.size();
 vector<int> a;
 for(i=pos;i<n;i++)
  a.push_back(s[i]-'0');
 sort(a.begin(),a.end());
 for(i=pos,j=0;i<n;i++,j++)
  s[i]=a[j]+'0';
 return s;
}
  






 


















