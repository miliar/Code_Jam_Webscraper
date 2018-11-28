#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;
/*
bool myfunction (int i,int j)
{
    return (i<j);

}
*/

int main()
{


int num,ca=1;

cin>>num;



while(num-->0)
{

char ch[25];

cin>>ch;

vector<int>n;

for(int i=0;ch[i];i++)
{
    n.push_back(ch[i]-'0');
}


int len=n.size();
int flag=0;

for(int i=len-2;i>=0;i--)
{
    int pos=i,cur=n[i],minmax=10;

    for(int j=i+1;j<len;j++)
    {

        if(n[j]>cur && n[j]<=minmax)
        {
            pos=j;
            flag=1;
            minmax=n[j];
        }
    }

    if(flag==1)
    {
        int temp=n[pos];

        swap(n[i],n[pos]);
        //n.erase(n.begin()+pos);
        //n.insert(n.begin()+i,temp);

        sort(n.begin()+i+1,n.end());
        break;


    }

}


if(flag==0)
{
    sort(n.begin(),n.end());

    int ctr=0;
    int temp;
    for(ctr=0;n[ctr]==0;ctr++);

    temp=n[ctr];

    n[ctr]=0;
    n.insert(n.begin(),temp);
}




//cout<<'\n';

cout<<"Case #"<<ca++<<": ";
for(int i=0;i<n.size();i++)
    cout<<n[i];

cout<<'\n';


}

}
