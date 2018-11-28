#include<iostream>
using namespace std;
int encrypt[]={25,8,5,19,15,3,22,24,4,21,9,7,12,2,11,18,26,20,14,23,10,16,6,13,1,17};
char str[110];
int main()
{
    int t,a=1;
    cin>>t;
    gets(str);
    while(t--)
    {
        gets(str);        
        int len=strlen(str);
        printf("Case #%d: ",a++);
        for(int i=0;i<len;i++)
        {
           if(str[i]!=' ')
           {
              int no=(int)str[i]-97;
              cout<<(char)(encrypt[no]+96);          
           }     
           else cout<<str[i];
        }      
        cout<<"\n";
    }
}
