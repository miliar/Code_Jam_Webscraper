#include <iostream>
#include <cstdio>
#include<cstdlib>

using namespace std;

int main(){

int i,map[26];

for(i=0;i<26;i++){
map[i]=-1;
}
map['y'-'a']='a'-'a';
map['e'-'a']='o'-'a';
map['q'-'a']='z'-'a';
char a[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char b[]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
for(i=0;a[i]!='\0';i++)
{
if(a[i]!=' ')
map[a[i]-'a']=b[i]-'a';
}
int sum=0;
for(i=0;i<26;i++){
if(map[i]!=-1)
sum+=map[i];
}
int missing_b= 13*25-sum;
for(i=0;i<26;i++){
if(map[i]==-1)
{
map[i]=missing_b;
}

}


char temp[20];
int test;
fgets(temp,sizeof(temp),stdin);
test=atoi(temp);
int t=0;
while(t<test){
char c[200];

fgets(c,sizeof(c),stdin);
//cout<<c<<"\n";
printf("Case #%d: ",t+1);
for(i=0;c[i]!='\0';i++)
{
if(c[i]==' ')
printf(" ");
else if(c[i]>='a'&&c[i]<='z'){
printf("%c",map[c[i]-'a']+'a');
}
}
printf("\n");
t++;
}
return 0;
}

