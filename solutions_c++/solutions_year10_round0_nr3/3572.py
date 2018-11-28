#include<iostream>
#include<list>
using namespace std;
void display (list<int> a)
{
list<int>::iterator p;
for ( p = a.begin( ); p != a.end( ); p++ )
{
cout<<*p<< " ";
}

}

int sum_list(list<int> a)
{
int s=0;
list<int>::iterator p;
for ( p = a.begin( ); p != a.end( ); p++ )
s+=*p;
return s;

}

int main()
{
int test;
int val,r,k,n,money,sum,count=0;
cin>>test;

list<int> a;
while(test--)
{
count++;
cin>>r>>k>>n;
a.clear();
for(int i=0;i<n;i++)
{
cin>>val;
a.push_back(val);
}

money=0;
if(sum_list(a)>k)
{
for(int i=0;i<r;i++)
{
sum=0;

for(int i=0;i<k;i++)
{
val=a.front();
if((sum+val)<=k)
{
money=money+val;
sum=sum+val;
a.pop_front();
a.push_back(val);
//cout<<"\n";

//display(a);
}
else break;

}

//cout<<"Money : "<<money;
//cout<<"\n";
//display(a);


}
cout<<"Case #"<<count<<": "<<money;
}
else
cout<<"Case #"<<count<<": "<<r*sum_list(a);
cout<<"\n";
//system("pause");

}
}

