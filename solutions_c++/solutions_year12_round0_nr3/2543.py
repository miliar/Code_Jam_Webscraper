#include<iostream>
#include<math.h>
#include<set>

using namespace std;

int main ()
{
    unsigned int t,a,b,i,j,k,temp,len=0,ans=0;
    set<int> s;
    cin>>t;
    for ( j = 0; j < t ; j++ )
    {
    cin>>a;
    cin>>b;
    temp=a;
    len=0;
    ans=0;
    while( temp!=0)
    {
           temp=temp/10;
           len++;
    }
    //cout<<len<<endl<<endl;
    for ( i=a ; i<=b ; i++)
    {
	s.clear();
        temp=i;
        for ( k=1 ; k<=len ; k++)
        {
		temp=((temp%10)*(pow(10,(len-1))))+(temp/10);
       // 	cout<<k<<"\t"<<temp<<endl;
		if(i<temp && temp<=b)
		s.insert(temp);
        }
	ans=ans+s.size();
    }
    cout<<"Case #"<<j+1<<": "<<ans<<endl;
}
    return 0;
}
