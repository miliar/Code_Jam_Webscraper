#include<iostream>
#include<conio.h>


using namespace std;

int main()

{
        freopen("read.txt","r",stdin);
freopen("write.txt","w",stdout);

    int t,i,i1=0;
    char a[100];
    //cin>>t;
    scanf("%d\n",&t);
    while(t--)
    {
        i1++;
        gets(a);
        i=0;cout<<"Case #"<<i1<<": ";
        while(a[i]!=NULL)
        {
            if(a[i]=='a') cout<<"y";
            if(a[i]=='b') cout<<"h";
            if(a[i]=='c') cout<<"e";
            if(a[i]=='d') cout<<"s";
            if(a[i]=='e') cout<<"o";
            if(a[i]=='f') cout<<"c";
            if(a[i]=='g') cout<<"v";
            if(a[i]=='h') cout<<"x";
            if(a[i]=='i') cout<<"d";
            if(a[i]=='j') cout<<"u";
            if(a[i]=='k') cout<<"i";
            if(a[i]=='l') cout<<"g";
            if(a[i]=='m') cout<<"l";
            if(a[i]=='n') cout<<"b";
            if(a[i]=='o') cout<<"k";
            if(a[i]=='p') cout<<"r";
            if(a[i]=='q') cout<<"z";
            if(a[i]=='r') cout<<"t";
            if(a[i]=='s') cout<<"n";
            if(a[i]=='t') cout<<"w";
            if(a[i]=='u') cout<<"j";
            if(a[i]=='v') cout<<"p";
            if(a[i]=='w') cout<<"f";
            if(a[i]=='x') cout<<"m";
            if(a[i]=='y') cout<<"a";
            if(a[i]=='z') cout<<"q";
            if(a[i]==' ') cout<<" ";
            i++;
        }
        cout<<"\n";
    }
    
}
