#include<iostream>
#include<string>
#include<cstring>
#include<stdlib.h>

using namespace std;

string str[1050],diff[1050];


string gcd(string a,string b);
string substract(string a,string b);
string _mod(string a,string b);
string div(string a,string b);
void mysort(string str[],int N);
int bigger(string a,string b);
string multiply(string b,int m);
string remove_trail(string rem);

int main()
{
    freopen("B_large.in","r",stdin);
    freopen("B_large_out.txt","w",stdout);

    int test,N,i,_case=1;
    string gcd_res,res,temp;

    scanf("%d",&test);

    while(test--)
    {
        scanf("%d",&N);
        for(i=0;i<N;i++)
            cin>>str[i];
        mysort(str,N);

        for(i=1;i<N;i++)
            diff[i-1]=substract(str[i],str[i-1]);
        mysort(diff,N-1);

        gcd_res=diff[0];
        for(i=1;i<N-1;i++)
            gcd_res=gcd(gcd_res,diff[i]);

        temp=_mod(str[0],gcd_res);

        if(temp=="0")
        {
            res="0";
        }
        else
        {
            res=substract(gcd_res,temp);
        }
        cout<<"Case #"<<_case++<<": "<<res<<endl;

    }


    return 0;
}

string gcd(string a,string b)
{
    if(b=="0") return a;
    return gcd(b,_mod(a,b));
}

string substract(string a,string b)
{
    int i,j,borrow=0,v;
    string res,res1;

    for(i=a.size()-1,j=b.size()-1;i>=0;i--,j--)
    {
        if(j>=0)
            v=a[i]-b[j]-borrow;
        else v=a[i]-borrow-48;
        if(v<0){
            v+=10;
            borrow=1;
        }
        else borrow=0;
        res.push_back(v+48);
    }

    reverse(res.begin(),res.end());
    res=remove_trail(res);
    return res;
}

string _mod(string a,string b)
{
    int v=bigger(b,a);
    if(v==1) return a;
    return div(a,b);
}

string div(string a,string b)
{
    string rem,t1,t2,rem1;
    int i,j,k;

    j=a.size();
    for(i=0;i<j;i++)
    {
        rem.push_back(a[i]);
        rem=remove_trail(rem);

        if(bigger(rem,b))
        {
            t1=b;
            for(k=2;;k++)
            {
                t2=multiply(b,k);
                if(bigger(t2,rem)==1)
                    break;
                t1=t2;
            }
            rem=substract(rem,t1);
        }
    }
    rem=remove_trail(rem);

    return rem;
}

void mysort(string str[],int N)
{
    int i,j;
    string temp;

    for(i=0;i<N-1;i++)
        for(j=0;j<N-1;j++)
            if(bigger(str[j],str[j+1])==1)
            {
                temp=str[j];
                str[j]=str[j+1];
                str[j+1]=temp;
            }
}

int bigger(string a,string b)
{
    int i,j;

    if(a.size()>b.size())   return 1;
    else if(a.size()<b.size()) return 0;

    j=a.size();
    for(i=0;i<j;i++)
        if(a[i]>b[i]) return 1;
        else if(a[i]<b[i]) return 0;
    return -1;
}

string multiply(string b,int m)
{
    string res;
    int i,j,v,carry=0;

    for(i=b.size()-1;i>=0;i--){
        v=(b[i]-48)*m+carry;
        res.push_back(v%10+48);
        carry=v/10;
    }
    while(carry)
    {
        res.push_back(carry%10+48);
        carry/=10;
    }
    reverse(res.begin(),res.end());
    return  res;

}

string remove_trail(string rem)
{
    string res;
    int i,j=rem.size();

    for(i=0;i<j;i++)
        if(rem[i]!='0') break;
    for(i;i<j;i++)
        res.push_back(rem[i]);
    if(res=="")
        res.push_back('0');

    return res;
}
