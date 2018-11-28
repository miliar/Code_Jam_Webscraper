#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<string>
#include<cmath>

using namespace std;

int* digits(int num,int &len)
{
    int i=0,*y,*z,c=0;
    y=new int[10];z=new int[10];
    while(num>0)
    {
        y[i++]=num%10;
        num=num/10;
    }
    for(int j=i-1;j>=0;j--)
        z[c++]=y[j];
    len=i;
    return z;
}

int len(int num)
{
    int i=0,*y;
    y=new int[10];
    while(num>0)
    {
        y[i++]=num%10;
        num=num/10;
    }
    return i;
}

int main(int argc, char* argv[])
{
    int test_case,*digit,*n1,*n2,a,b,count;
    string in;
    freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);
	cin>>test_case;
	getline(cin,in);
	for(int i=0;i<test_case;i++)
    {
        cin>>a>>b;
        count=0;
        int len1,len2;
        n1=digits(a,len1);n2=digits(b,len2);
        if(len1 ==1)
        {
            if(len2 ==1)
                cout<<"Case #"<<(i+1)<<": "<<'0'<<endl;
            else
            {
                for(int j=11;j<=b;j++)
                {
                    int c=0,num,num1,num2,length;
                    digit=digits(j,length);
                    while(c<length)
                    {
                        num=0;num1=0;num2=0;
                        for(int p=0;p<=c;p++)
                            num1=num1*10+digit[p];
                        for(int k=c+1;k<length;k++)
                            num2=num2*10+digit[k];
                        num=num2*pow(10,c+1)+num1;
                        if(num>j && num<=b)
                        {
                            if(num2%num1!=0)
                                count++;
                            else
                            {
                                if(len(num1)==len(num2) && len(num1)>1)
                                    count=count;
                                else
                                    count++;
                            }
                        }
                        c++;
                    }
                }
                cout<<"Case #"<<(i+1)<<": "<<count<<endl;
            }
        }
        else
        {
            for(int j=a;j<=b;j++)
            {
                int c=0,num,num1,num2,length;
                digit=digits(j,length);
                while(c<length)
                {
                    num=0;num1=0;num2=0;
                    for(int p=0;p<=c;p++)
                        num1=num1*10+digit[p];
                    for(int k=c+1;k<length;k++)
                        num2=num2*10+digit[k];
                    num=num2*pow(10,c+1)+num1;
                    if(num>j && num<=b)
                    {
                        if(num2%num1!=0)
                            count++;
                        else
                        {
                            if(len(num1)>1)
                                count=count;
                            else
                                count++;
                        }
                    }
                    c++;
                }
            }
            cout<<"Case #"<<(i+1)<<": "<<count<<endl;
        }
    }
}
