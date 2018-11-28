#include<iostream>
using namespace std;
int main()
{
int l;
cin>>l;
for(int i=1;i<=l;i++)
{
int r,k,n;
cin>>r>>k>>n;
int ar[n];
for(int j=0;j<n;j++)
cin>>ar[j];
int pr=0,pppr;
long long int tot=0,kkk=0;
for(int j=0;j<r;j++)
{
        kkk=0;
        pppr=pr;
        while(1)
        {
                if(ar[pr]+kkk>k)
                break;
                kkk+=ar[pr];
                pr=pr+1;
                if(pr>=n)
                pr=0;
                if(pppr==pr)
                break;
                }
                tot+=kkk;
        
        
        
        



}

cout<<"Case #"<<i<<": ";
cout<<tot<<"\n";

}
return 0;
}
