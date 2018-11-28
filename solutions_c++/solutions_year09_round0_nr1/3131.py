#include<iostream>
#include<string.h>
 using namespace std;
 int check(char* , char*,int);
 int main()
 {
     int l,d,n,i,count,x=1;
     char dict[5001][16],signal[100000];
     cin>>l>>d>>n;
     for(int i=0;i<d;i++)
                        cin>>dict[i];
     for(int i=0;i<n;i++)
                        {
                               count=0;
                               cin>>signal;
                               for(int j=0;j<d;j++)
                               {
                                       if(check(signal,dict[j],l))
                                       count++;
                               }
                               cout<<"Case #"<<x<<": "<<count<<endl;
                               x++;
                        } 
 return 0;
}
int check(char *s , char *d,int a)
{
    int c=0,j;
    for(int i=0,j=0;i<a;i++)
    {
            if(s[j]==d[i])
            {c++;j++;}
            else if(s[j] == '(')
            {j++;
                 while(s[j]!=')')
                 {
                                 if(d[i]==s[j])
                                 {c++;j++;break;}
                                 j++;
                 }
                 while(s[j]!=')')j++;j++;
            }
}
if(c==a)
return 1;
else 
return 0;
}
