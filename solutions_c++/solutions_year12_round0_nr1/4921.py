#include<iostream>
#include<string>
#include<conio.h>
using namespace std;
int main()
{
    struct alpha
    {
           char x,y;
    }a[26];
    a[1].x='a';
    a[1].y='y';
    
    a[2].x='b';
    a[2].y='n';
    
    a[3].x='c';
    a[3].y='f';
    
    a[4].x='d';
    a[4].y='i';
    
    a[5].x='e';
    a[5].y='c';
    
    a[6].x='f';
    a[6].y='w';
    
    a[7].x='g';
    a[7].y='l';
    
    a[8].x='h';
    a[8].y='b';
    
    a[9].x='i';
    a[9].y='k';
    
    a[10].x='j';
    a[10].y='u';
    
    a[11].x='k';
    a[11].y='o';
    
    a[12].x='l';
    a[12].y='m';
    
    a[13].x='m';
    a[13].y='x';
    
    a[14].x='n';
    a[14].y='s';
    
    a[15].x='o';
    a[15].y='e';
    
    a[16].x='p';
    a[16].y='v';
    
    a[17].x='q';
    a[17].y='z';
    
    a[18].x='r';
    a[18].y='p';
    
    a[19].x='s';
    a[19].y='d';
    
    a[20].x='t';
    a[20].y='r';
    
    a[21].x='u';
    a[21].y='j';
    
    a[22].x='v';
    a[22].y='g';
    
    a[23].x='w';
    a[23].y='t';
    
    a[24].x='x';
    a[24].y='h';
    
    a[25].x='y';
    a[25].y='a';
    
    a[26].x='z';
    a[26].y='q';
    
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {       string str;   
            if(i==1)         
            getline(cin,str);
            getline(cin,str);
            cout<<"Case #"<<i<<": ";
            for(int j=0;j<str.length();j++)
            {
                    if(str[j]==' ')
                    cout<<" ";
                    else
                    {
                        for(int k=1;k<=26;k++)
                        {
                            
                            if(str[j]==a[k].y)
                            cout<<a[k].x;
                        }
                    }
            }
            cout<<endl;
    }
    return 0;
}
                    
