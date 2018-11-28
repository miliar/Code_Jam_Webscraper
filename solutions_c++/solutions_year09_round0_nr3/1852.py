#include<iostream>
#include<cstdio>
using namespace std;
int check(char s[505],int p,char str[20],int pos){
if((pos==19))return 1;
int count=0,j;
for(j=p;s[j]!='\0';j++){
    if(s[j]==str[pos]){
        count+=check(s,j+1,str,pos+1);
        count=count%1000;
    }
}
return count;
}

int main()
{
    char str[]="welcome to code jam";
    char s[505];
    int count,t,tno=1;
    cin>>t;
    s[0]=getchar();
    while(tno<=t){
    cin.getline(s,500,'\n');
    count=check(s,0,str,0);
    //cout<<s;
    printf("Case #%d: %04d\n",tno,count);
    tno++;
    }
    return 0;
}
    
