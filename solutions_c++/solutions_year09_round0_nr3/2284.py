#include <iostream>
#include <string>
using namespace std;


int main()
{
int tab[19],pom[200][4];
int N,i,j,p,k;
string s;
for(i=0;i<200;i++)
  pom[i][0]=0;
//welcome to code jam
pom['e'][0]=3;
pom['e'][1]=1;
pom['e'][2]=6;
pom['e'][3]=14;
pom['l'][0]=1;
pom['l'][1]=2;
pom['c'][0]=2;
pom['c'][1]=3;
pom['c'][2]=11;
pom['o'][0]=3;
pom['o'][1]=4;
pom['o'][2]=9;
pom['o'][3]=12;
pom['m'][0]=2;
pom['m'][1]=5;
pom['m'][2]=18;
pom[' '][0]=3;
pom[' '][1]=7;
pom[' '][2]=10;
pom[' '][3]=15;
pom['t'][0]=1;
pom['t'][1]=8;
pom['d'][0]=1;
pom['d'][1]=13;
pom['j'][0]=1;
pom['j'][1]=16;
pom['a'][0]=1;
pom['a'][1]=17;
cin>>N;
cin.ignore();
for(i=0;i<N;i++)
 {
 getline(cin,s);
 p=s.length();
 for(j=0;j<19;j++)
   tab[j]=0;
 for(j=0;j<p;j++)
   {   
   if (s[j]=='w')
     {
     //cout<<"aaaaaaaaaaa";
     tab[0]++;
     tab[0]=tab[0]%10000;
     }
   else
     for(k=1;k<=pom[s[j]][0];k++){
       tab[pom[s[j]][k]]+=tab[pom[s[j]][k]-1];
       tab[pom[s[j]][k]]=tab[pom[s[j]][k]]%10000;
     }
    /*cout<<s[j]<<endl; 
    for(k=0;k<19;k++)
      cout<<tab[k]<<" ";
    cout<<endl;*/
   }
 cout<<"Case #"<<i+1<<": ";
 if (tab[18]<1000) 
   cout<<"0";
 if (tab[18]<100)
   cout<<"0";
 if (tab[18]<10)
   cout<<"0";
 cout<<tab[18]<<endl;
 }
}