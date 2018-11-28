#include<iostream>
using namespace std;

FILE *in,*out;

long long t,tt,l,p,c,n,i,test[1000],tmp;

int main()
{
	in=freopen("B-large.in","r",stdin);
    out=freopen("B-large.out","w",stdout);
    
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        memset(test,0,sizeof(test));
        cin>>l>>p>>c;
        n=1;
        tmp=c;
        while (l*tmp<p)
        {
            n++;
            tmp*=c;
        }
        test[1]=0;
        test[2]=1;
        test[3]=2;
        for (i=4;i<=n;i++)
        {
            if (i%2==0)
                test[i]=test[i/2]+1;
            else
                test[i]=test[(i-1)/2+1]+1;
        }
        cout<<"Case #"<<tt<<": "<<test[n]<<endl;
    }
    fclose(in);
    fclose(out);
	return 0;
}
