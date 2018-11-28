#include<iostream>
using namespace std;
char arr[6000][6000],dict[6000][6000];
int main()
{
    long long n,d,l,i,j,count,count1,flag,k,m;
    cin>>l>>d>>n;
    for(i=0;i<d;i++)
       cin>>dict[i];
    for(i=0;i<n;i++)
         cin>>arr[i];
    for(i=0;i<n;i++)
    {
        count=0;
        count1=0;
        j=0;
        long long storage[26][20]={0};
        while(j<strlen(arr[i]))
        {
             if(arr[i][j]!='(')
                {
                   storage[arr[i][j]-97][count++]=1;
                }
             else if(arr[i][j]=='(')
                {
                     j=j+1;
                     while(arr[i][j]!=')')
                     {
                         
                         storage[arr[i][j]-97][count]=1;
                         j=j+1;
                     }
                     
                     count++;
                }
                j=j+1;
        }
        count1=0;
       for(k=0;k<d;k++)
       {
         m=0;
         flag=1;
         while(m<strlen(dict[k]))
          {
             if(storage[dict[k][m]-97][m]!=1)
             {
                flag=0;
                break;
             }
             m=m+1;
           }
          if(flag==1)
            count1++;
        }
        cout<<"Case #"<<i+1<<": "<<count1<<endl;
    }
    return 0;
}
