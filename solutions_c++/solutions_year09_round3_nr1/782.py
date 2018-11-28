#include<iostream>
#include<fstream>
using namespace std;

ofstream fout("A-large.out");
ifstream fin("A-large.in");

long long tcase,num,ans;
char a[255];
int b[255];
int main()
{
    char s[256];
    long long i,j,k,t;
    long long l;
    fin>>tcase;fin.getline(s,255);
    
    for (i=1;i<=tcase;i++)
    {
        fin.getline(s,255);
        
        num=0;memset(b,0,sizeof(b));
        for (j=0;j<strlen(s);j++)
        {
            if (num==0) {num++;a[num]=s[j];}
            else 
            {
                 t=0;
                 for (k=1;k<=num;k++)       if (a[k]==s[j]) {t=1;break;}
                 if (t==0) {num++;a[num]=s[j];}
            }            
        }
        b[1]=1;b[2]=0;
        if (num>=3)
        for (j=3;j<=num;j++) b[j]=j-1;
        ans=0;l=1;
        int ll=num;
        if (ll==1)  ll=2;
        for (j=strlen(s)-1;j>=0;j--)
        {
            for (k=1;k<=num;k++) if (a[k]==s[j]) {ans+=b[k]*l;}
            l*=ll;
        }
        //fout<<s<<endl;
        fout<<"Case #"<<i<<": "<<ans<<endl;
        //fout<<endl;
        
    }
    //cin>>i;
    return 0;
}
