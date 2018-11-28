#include<stdlib.h>
#include<iostream>
#include<math.h>
#include<vector>
#include<string>
#include<fstream>
#include<algorithm>

using namespace std;

int max(vector<int> v){
  if(v.size()==0) return 0;
  int s=v[0];
  for(int i=0;i<v.size();i++){
    if(v[i]>s) s=v[i];
  }
  return s;
}

int min(vector<int> v){
  if(v.size()==0) return 1000000;
  int s=v[0];
  for(int i=0;i<v.size();i++){
    if(v[i]<s) s=v[i];
  }
  return s;
}

int trovadove(vector<int> s,int c){
  for(int i=0; i<s.size();i++){
    if(s[i]>=c) return i;}
}

vector<int> quanti_treni(vector<int>& pa,vector<int>& pb,vector<int>& aa,vector<int>& ab){
  if(min(ab)<=max(pa)){
    pa.erase(pa.begin()+trovadove(pa,min(ab)));
    ab.erase(ab.begin());
    return quanti_treni(pa,pb,aa,ab);
    }
  if(min(aa)<=max(pb)){
    pb.erase(pb.begin()+trovadove(pb,min(aa)));
    aa.erase(aa.begin());
    return quanti_treni(pa,pb,aa,ab);
    }
  vector<int> v;
    v.push_back(pa.size());
    v.push_back(pb.size());
    return v;
}


main(){
ifstream f("input.txt");
ofstream o("output.txt");

int num_casi;
int num_ricorr;
int num_a,num_b;

vector<int> partenze_a;
vector<int> partenze_b;
vector<int> arrivi_a;
vector<int> arrivi_b;

f>>num_casi;

for(int zum=1;zum<=num_casi;zum++){

f>>num_ricorr;
f>>num_a;
f>>num_b;

for(int i=0;i<num_a;i++){
  int x; int y;
  f>>x; f>>y;
  partenze_a.push_back(x*60+y);
  f>>x; f>>y;
  arrivi_a.push_back(x*60+y+num_ricorr);
}

for(int i=0;i<num_b;i++){
  
  int x; int y;
  f>>x; f>>y;
  partenze_b.push_back(x*60+y);
  f>>x; f>>y;
  arrivi_b.push_back(x*60+y+num_ricorr);
}

if(num_a==0){
    o<<"Case #"<<zum<<": "<<0<<" "<<num_b<<endl; partenze_a.erase(partenze_a.begin(),partenze_a.end());
    partenze_b.erase(partenze_b.begin(),partenze_b.end());
    arrivi_a.erase(arrivi_a.begin(),arrivi_a.end());
    arrivi_b.erase(arrivi_b.begin(),arrivi_b.end());
    continue;}
    
if(num_b==0){
   o<<"Case #"<<zum<<": "<<num_a<<" "<<0<<endl;
   partenze_a.clear();
   partenze_b.clear();
   arrivi_a.clear();
   arrivi_b.clear();
   continue;}

sort(partenze_a.begin(),partenze_a.end());
sort(partenze_b.begin(),partenze_b.end());
sort(arrivi_a.begin(),arrivi_a.end());
sort(arrivi_b.begin(),arrivi_b.end());

for(int i=0;i<partenze_a.size();i++) cout<<partenze_a[i]<<" ";
cout<<endl;

for(int i=0;i<arrivi_a.size();i++) cout<<arrivi_a[i]<<" ";
cout<<endl;

for(int i=0;i<partenze_b.size();i++) cout<<partenze_b[i]<<" ";
cout<<endl;

for(int i=0;i<arrivi_b.size();i++) cout<<arrivi_b[i]<<" ";
cout<<endl;


vector<int> s=quanti_treni(partenze_a,partenze_b,arrivi_a,arrivi_b);
o<<"Case #"<<zum<<": "<<s[0]<<" "<<s[1]<<endl;

partenze_a.clear();
partenze_b.clear();
arrivi_a.clear();
arrivi_b.clear();
}


}
