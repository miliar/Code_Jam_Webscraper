#include<iostream>
#include<sstream>
#include<math.h>
#include<stdlib.h>
using namespace std;
char greaterlessthan(long long index,char str1[10],char str2[10],long long len)
{
    long long k,ind,ii=index,jj=len-1,run=0;
    while(jj>=0)
    {
        if(str1[ii]!=str1[jj])
            run=1;
        ii--;
        if(ii<0)
            ii=len-1;
        jj--;
    }
    if(run==0)
        return 'x';

    if(str1[index]>str2[len-1])
        return 'g';
    else if(str1[index]==str2[len-1])
    {
        k=1;
        ind=index-1;
        if(ind<0)
            ind=len-1;
        while(k<len && str1[ind]==str2[len-1-k])
        {
            k++;
            ind--;
            if(ind<0)
                ind=len-1;
        }
        if(k<len)
        {
            if(str1[ind]>str2[len-1-k])
                return 'g';
            else
                return 'l';
        }
        else
        {
            return 'e';
        }
    }
    else
        return 'l';

}
long long getcount(long long n,long long a,long long b)
{
    long long count=0,i,len=0,j,k=n,rep=0;
    char strn[10],strb[10],stra[10],sym=0;;
    while(n && b && a)
    {
        strn[len]=(char)(n%10 + 48);
        strb[len]=(char)(b%10 + 48);
        stra[len]=(char)(a%10 + 48);
        n/=10;
        b/=10;
        a/=10;
        len++;
    }
    for(i=0;i<len-1;i++)
    {
        char x=greaterlessthan(i,strn,strn,len),y=greaterlessthan(i,strn,strb,len);
        if(x=='g')
        {
            if(y=='l' || y=='e')
            {
                count++;
                if(len==4)
                    if(strn[0]==strn[2] && strn[1]==strn[3])
                    {
                        if(rep==0)
                            count-=1;
                        rep=1;
                    }
                if(len==6)
                {
                    if(strn[0]==strn[2] && strn[2]==strn[4] && strn[1]==strn[3] && strn[3]==strn[5] )
                    {
                        if(rep==0)
                            count-=2;
                        rep=1;
                    }
                    if(strn[0]==strn[3] && strn[1]==strn[4] && strn[2]==strn[5])
                    {
                        if(rep==0)
                            count-=2;
                        rep=1;
                    }
                }

            }
        }
    }
    return count;
}
int main()
{
    long long t,i,a,b,j,count,k;
    cin>>t;
    cin.ignore();
    for(i=1;i<=t;i++)
    {
        count=0;
        cin>>a>>b;
        for(j=a;j<=b;j++)
        {
            count+=getcount(j,a,b);
            //cout<<j<<" "<<getcount(j,a,b)<<endl;
        }
        cout<<"Case #"<<i<<": "<<(count)<<endl;
    }
    return 0;
}

