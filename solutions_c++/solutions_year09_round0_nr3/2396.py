#include<iostream>
#include<string>
#include<stdio.h>


using namespace std;


char s[]="welcome to code jam";
char str[500];
int ctr=0;
int size=0;

void func(int pos)
{
    //getchar();
    //cout<<size<<' ';
    if(s[size]=='\0')
    {
        //size--;
      //  cout<<size<<' ';
        //cout<<'!';
        ctr++;
        return;
    }

    for(int i=pos;str[i]!='\0';i++)
    {

        if(str[i]==s[size])
        {
            //cout<<"\ninner:"<<str[i];
           //cout<<str[i];//<<' ';
           //if(size==13) cout<<"#";
           size++;
           func(i+1);
           size--;
           //i++;

        }
    }

    return;
}


int main()
{
int n,ca=1,ans[4];

cin>>n;

getchar();

while(n-->0)
{
    ctr=0;
    size=0;
    str[0]='\0';

    gets(str);
    func(0);

    for(int i=3;i>=0;i--)
    {
        ans[i]=ctr%10;
        ctr/=10;
    }

    cout<<"Case #"<<ca++<<": "<<ans[0]<<ans[1]<<ans[2]<<ans[3]<<'\n';


}

}




