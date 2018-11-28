#include<iostream>
#include<cstdio>
#include<memory.h>
#include<iostream>
#include<string.h>
using namespace std;
void Add(char * a)
{
    int len=strlen(a);
    a[len-1]++;
    for(int i=len-1;i>=1;i--)
    {
        if(a[i]>='0'+10) {a[i]-=10;a[i-1]++;}
        else return;
    }
}
int f[1000001];
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.out","w",stdout);
    char c1[100],c2[100],A[100],B[100],c11[100];
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cin>>A>>B;
        int ans=0,len=strlen(A);
        memset(f,-1,sizeof(f));
        int x=1,a=0,b=0;
        for(int j=len-1;j>=0;j--)
        {
            a+=x*(A[j]-'0');
            b+=x*(B[j]-'0');
            x*=10;
        }
        for(int j=0;j<b-a;j++)
        {

            strcpy(c11,A);
            strcpy(c1,c11);
            strcat(c1,c11);
            for(int k=1;k<=len-1;k++)
            {
                bool fa,fb;
                fa=true;fb=true;
                for(int p=0;p<len;p++)
                    {
                        if(c1[k+p]>A[p]) break;
                        if(c1[k+p]<A[p]) {fa=false;break;}
                        if(p==len-1&&c1[k+p]==A[p]) {fa=false;break;}
                    }
                for(int p=0;p<len;p++)
                    {
                        if(c1[k+p]<B[p]) break;
                        if(c1[k+p]>B[p]) {fb=false;break;}
                    }
                if(fa&&fb)
                {
                    int x=1,c=0;
                    for(int p=len-1;p>=0;p--)
                    {
                        c+=x*(c1[k+p]-'0');
                        x*=10;
                    }
                    if(f[c]<j)
                    {
                        ans++;
                        f[c]=j;
                    }
                }
            }
            Add(A);
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
	return 0;
}


