#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;

int main()
{
int T;
long long v;
cin>>T;
char s[65];

int n = 1;
while(n<=T)
{
v = 0;
int i;
char t[65];
int a[65];
int count;
bool flag;


cin>>s;

count = 0;
for(i = 0;s[i]!='\0';i++)
{       

        flag = true;
        for(int j = 0;j < count;j++)
        {
                if(t[j] == s[i])
                {
                        flag = false;                     
                        break;
                }
        }
        if(flag)
        {      t[count++] = s[i];
        }        
}

if(s[1] == '\0')       cout<<"Case #"<<n<<": "<<1<<endl;
            
else
{
a[0] = 1;

for(i = 1;s[i]!= '\0' ;i++)
    if(s[i] == s[0])                        
        a[i] = 1;
       
for(i = 1;s[i] == s[0];i++);
if(s[i]!='\0')
        a[i] = 0;
        
i++;
int q = 2;

for(;s[i]!='\0';i++)
{
        flag = true;
        for(int j = 0;j<i;j++)
        {
                if(s[j] == s[i])
                {       
                        a[i] = a[j];
                        flag = false;
                        break;
                }
        }
        if(flag)
                a[i] = q++;
}



if(count == 1)
        count = 2;

for(i = 0;s[i]!='\0';i++);
        
        
int x = i-1;

for(i = 0;s[i]!='\0';i++)
        v+=a[i]*pow(count,x--);
                       
cout<<"Case #"<<n<<": "<<v<<endl;   

}

n++;

}
return 0;
}
